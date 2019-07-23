from django.test import TestCase, Client
import json


class tinyurlCase(TestCase):
    def setUp(self):
        pass

    def test_url_contains_tinyurl(self):
        c = Client()
        response = c.get("/api/tinyurl", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("tinyurl" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/tinyurl")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/tinyurl")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class RebrandlyCase(TestCase):
    def setUp(self):
        pass

    def test_url_contains_rebrandly(self):
        c = Client()
        response = c.get("/api/rebrandly", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("rebrand.ly" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/rebrandly")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/rebrandly")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class ProviderCase(TestCase):
    def setUp(self):
        pass

    def test_nb_providers(self):
        c = Client()
        response = c.get("/api/providers")
        url = response.json()
        self.assertTrue(len(url) == 4)

    def test_only_get(self):
        c = Client()
        response = c.post("/api/providers")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class cuttlylCase(TestCase):
    def setUp(self):
        pass

    def test_url_contains_cuttly(self):
        c = Client()
        response = c.get("/api/cuttly", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("cutt.ly" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/cuttly")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/cuttly")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class bitlylCase(TestCase):
    def setUp(self):
        pass

    def test_url_contains_cuttly(self):
        c = Client()
        response = c.get("/api/bitly", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("bit.ly" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/bitly")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/bitly")
        self.assertEqual(response.status_code, 405, "unexpected return code")
