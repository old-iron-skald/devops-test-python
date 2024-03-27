import unittest
from unittest.mock import patch
from app import app, ProductModel

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def tearDown(self):
        pass

    @patch('app.ProductModel.select')
    def test_get_products(self, mock_select):
        # Mocking the ProductModel.select function to avoid database interactions in the test
        mock_select.return_value = [{'id': 1, 'name': 'Test Product', 'price': 10.0}]

        # Sending a GET request to /api/products endpoint
        response = self.client.get('/api/products')

        # Asserting the response status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [{'id': 1, 'name': 'Test Product', 'price': 10.0}])

if __name__ == '__main__':
    unittest.main()