from flask import Flask, Response, request, render_template
from prometheus_client import start_http_server, Counter, Gauge, Summary, Histogram
import prometheus_client
from nltk import word_tokenize, download
from nltk.corpus import stopwords
from gensim import models
from gensim.similarities import WmdSimilarity
import pandas as pd
import re
import time
import random
download('stopwords')
download('punkt')

app = Flask(__name__)

# Prometheus Monitoring
c_index = Counter('app_index_access', 'Counter for main page')
c_res= Counter('app_results_page', 'Counter for results page')
e = Counter('app_exceptions_total', 'How many times an exception has been issued')
g_inprogress = Gauge('app_page_access_in_progress', 'Visits in progress')
g_last = Gauge('app_page_accesses_last_time_seconds', 'The last time results_page was accessed')
l = Summary('app_latency_in_seconds', 'Time required for a request')
h = Histogram('app_python_requests_duration_seconds', 'Histogram for the duration in seconds', buckets=(0.005, 0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1, 2, 5, 7, 10))

# Preprocessing 
def pre_processing_text(text):
    # lowercase
    text = text.lower()
    # extra lines
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r"\'", "", text)
    # punctuations and symbols
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    # hastags
    text = text.replace("#", "")
    # hyperlinks
    text = re.sub(
        "(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)", '', text)
    text = re.sub("http", '', text)
    # retweets
    text = re.sub(r'^RT @.+\:', '', text)
    text = re.sub('@', '', text)
    # stopwords
    return [word for word in word_tokenize(text) if word not in stop_words]

# Word2Vec pretrained model
stop_words = stopwords.words('english')
model = models.Word2Vec.load('word2vec.model')

# Dataframe creation and model implementation
df = pd.read_csv('tweets.csv')
df_text = pd.DataFrame()
df.text = df.text.apply(pre_processing_text(df.text))
df_text['Text'] = df.text
similarity_index = WmdSimilarity(df_text['Text'], model, num_best=20)

# Flask
@app.route('/')
def index():
    c_index.inc()
    with e.count_exceptions():
        if random.random() < 0.2:
            raise Exception 
    return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        c_res.inc()
        g_inprogress.inc()
        c_index.inc()
        start = time.time()
        answer = request.form['Answer']
        clean_answer = pre_processing_text(answer)
        similar = similarity_index[clean_answer]
        text_results = list()
        score_results = list()
        for i in range(len(similar)):
            text_results.append(df_text['Text'][similar[i][0]])
            score_results.append(similar[i][1])
        score_results = ["{:.2f}".format(score) for score in score_results]
        end = time.time()
        g_last.set(end)
        g_inprogress.dec()
        l.observe(end - start)
        h.observe(end - start)
        return render_template('results.html', results=zip(text_results,score_results))
    return render_template('index.html')

if __name__ == "__main__":
    start_http_server(8010)
    app.run(host='0.0.0.0')
