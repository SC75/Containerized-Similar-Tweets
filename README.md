# Containerized-Similar-Tweets

![alt text](https://zupimages.net/up/20/51/fnpx.png)

This is a dockerized flask web application using NLP. 

The user can submit a word to a form. The web app will return the top 20 most similar presidential tweets.
After cloning this repository, type this command:

    docker-compose up

A docker container will be created and the web app will be available on localhost port 5000.
Unit testing:

    python unit_tests.py

Sress testing: 

    python stress_tests.py

Monitoring is possible with the help of Prometheus, node_exporter and alert_manager. Dashboard can be used thanks to Grafana. 
