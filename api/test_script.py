import unittest
from api.app import app


class YourAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_valid_form_one(self):
        data = {
            'user_name': 'Kseniya',
            'user_email': 'example@example.com',
            'user_phone': '+7 999 999 99 99',
            'createdAt': '2023-11-01',
            'address': 'Moscow',
        }
        response = self.app.post('/get_form', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"template_name": "OrderForm"})

    def test_valid_form_two(self):
        data = {
            'user_name': 'Kseniya',
            'user_email': 'example@example.com',
            'user_phone': '+7 999 999 99 99',
            'createdAt': '2023-11-01',
            'address': 'Moscow',
            'status': 'Paid',
        }
        response = self.app.post('/get_form', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"template_name": "OrderForm"})

    def test_valid_form_three(self):
        data = {
            'fullName': 'Kseniya Petrova',
            'email': 'example@example.com',
            'phone': '+7 999 999 99 99',
            'createdAt': '2023-11-01',
            'address': 'Moscow',
            'city': 'Moscow',

        }
        response = self.app.post('/get_form', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"template_name": "UserForm"})

    def test_invalid_form_one(self):
        data = {
            'email': 'example@example.com',
            'phone': '+ 7 999 999 99 99',
            'name': 'Ivan',
            'address': 'Moscow',
        }
        response = self.app.post('/get_form', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'email': 'email', 'name': 'text', 'phone': 'phone', 'address': 'text'})

    def test_invalid_form_two(self):
        data = {
            'email': 'example@example.com',
            'phone': '+ 7 999 999 99 99',
            'fullName': 'Ivan Ivanov',
        }
        response = self.app.post('/get_form', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'email': 'email', 'fullName': 'text', 'phone': 'phone'})

    def test_invalid_form_three(self):
        data = {
            'email': 'example@example.com',
            'phone': '999 999 99 99',
            'fullName': 'Ivan Ivanov',
            'address': 'Moscow',
        }
        response = self.app.post('/get_form', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'email': 'email', 'fullName': 'text', 'phone': 'text', 'address': 'text'})


if __name__ == '__main__':
    unittest.main()
