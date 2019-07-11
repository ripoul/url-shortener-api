from django.test import TestCase, Client
import json

class tinyurlCase(TestCase):
    def setUp(self):
        pass

    def test_url_contains_tinyurl(self):
        c = Client()
        response = c.get('/api/tinyurl', {'url': 'https://www.google.fr'})
        url = response.json()["url"]
        self.assertTrue("tinyurl" in url)
    
    def test_if_no_param(self):
        c = Client()
        response = c.get('/api/tinyurl')
        self.assertEqual(response.status_code, 400, "unexpected return code")