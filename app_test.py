import unittest
from unittest.mock import patch
from app import app, ProductModel

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('app.ProductModel.select')
    def test_get_products(self, mock_select):
        mock_select.return_value = [ProductModel(id=1, name="Test Product", price=10.0)]
        response = self.app.get('/api/products')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Product', response.data)

    @patch('app.create_product')
    def test_add_product(self, mock_create):
        mock_create.return_value = ProductModel(id=1, name="Test Product", price=10.0)
        response = self.app.post('/api/products', json={"name": "Test Product", "price": 10.0})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Test Product', response.data)

    @patch('app.get_product_by_id')
    def test_get_product(self, mock_get):
        mock_get.return_value = ProductModel(id=1, name="Test Product", price=10.0)
        response = self.app.get('/api/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Product', response.data)

if __name__ == '__main__':
    unittest.main()
