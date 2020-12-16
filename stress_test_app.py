import unittest
import requests
import time
import os

class FlaskTests(unittest.TestCase):
    def setUp(self):
        os.environ['NO_PROXY'] = '0.0.0.0'
        pass

    def tearDown(self):
        pass

    def test_index(self):
        n = 1000
        resonses_urls = []

        for i in range(n):
            responses_urls.append(requests.get('http://localhost:5000'))

        start = time.time()
        end = time.time()
        t = end-start

        for i in range(n):
            self.assertEqual(responses_urls[i].status_code, 200)

        print("The {} requests took: {} seconds".format(n, t))


if __name__ == '__main__':
    unittest.main()
