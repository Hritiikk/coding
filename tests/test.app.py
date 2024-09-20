import unittest
from app import app

class TestPricePrediction(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_predict(self):
        response = self.app.post('/predict', json={
            'origin': 'NYC', 
            'destination': 'LAX', 
            'date': '2024-12-01'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('predicted_price', data)

if __name__ == '__main__':
    unittest.main()
