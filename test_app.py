import unittest
import requests
import app


class TestApp(unittest.TestCase):

    def test_a_base(self):
        response = requests.get('http://localhost:5000')
        self.assertEqual(response.status_code, 200)

    def test_result(self):
        Answer = "*The american people are tired of women!*/"
        res = app.pre_processing_text(Answer)
        self.assertEqual(res, ['american', 'people', 'tired', 'women'])
    
    def test_response(self):

        params = {
            'Answer': 'China? CHINA! China'
        }
        response = requests.post('http://localhost:5000/result', data=params)
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
