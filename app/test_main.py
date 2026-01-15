import main
import unittest

class TestMainPage(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_message(self):
        response = self.app.get('/')
        message = main.page("Hello CGI!!! Welcome to the world of DevOps :)")
        self.assertEqual(response.data.decode("utf-8"), message)

if __name__ == '__main__':
    unittest.main()
