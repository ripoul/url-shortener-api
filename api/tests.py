from django.test import TestCase, Client
from unittest import skipIf
import json
from .utils import get_vars
import requests


class ProviderCase(TestCase):
    def test_nb_providers(self):
        c = Client()
        response = c.get("/api/providers")
        url = response.json()
        self.assertTrue(len(url) == 18)

    def test_only_get(self):
        c = Client()
        response = c.post("/api/providers")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class tinyurlCase(TestCase):
    def test_url_contains_provider(self):
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
    @skipIf(not get_vars("rebrandlyAPI"), "rebrandlyAPI env vars not set")
    def test_url_contains_provider(self):
        c = Client()
        response = c.get("/api/rebrandly", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        urlID = response.json()["id"]

        self.assertTrue("rebrand.ly" in url)

        requestHeaders = {
            "Content-type": "application/json",
            "apikey": get_vars("rebrandlyAPI"),
        }

        r = requests.delete(
            "https://api.rebrandly.com/v1/links/" + urlID, headers=requestHeaders
        )

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/rebrandly")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/rebrandly")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class cuttlylCase(TestCase):
    @skipIf(not get_vars("cuttlyAPI"), "cuttlyAPI env vars not set")
    def test_url_contains_provider(self):
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
    @skipIf(not get_vars("bitlyAPI"), "bitlyAPI env vars not set")
    @skipIf(not get_vars("bittlyAPIgroup"), "bittlyAPIgroup env vars not set")
    def test_url_contains_provider(self):
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


class m360usCase(TestCase):
    def test_url_contains_provider(self):
        c = Client()
        response = c.get("/api/m360us", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("m360.us" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/m360us")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/m360us")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class osdblinkCase(TestCase):
    def test_url_contains_provider(self):
        c = Client()
        response = c.get("/api/osdblink", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("http://osdb.link" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/osdblink")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/osdblink")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class isgdCase(TestCase):
    def test_url_contains_provider(self):
        c = Client()
        response = c.get("/api/isgd", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("https://is.gd/" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/isgd")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/isgd")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class chilpitCase(TestCase):
    def test_url_contains_provider(self):
        c = Client()
        response = c.get("/api/chilpit", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("http://chilp.it/" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/chilpit")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/chilpit")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class clckruCase(TestCase):
    def test_url_contains_provider(self):
        c = Client()
        response = c.get("/api/clckru", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("https://clck.ru/" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/clckru")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/clckru")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class dagdCase(TestCase):
    def test_url_contains_provider(self):
        c = Client()
        response = c.get("/api/dagd", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("https://da.gd/" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/dagd")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/dagd")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class qpsruCase(TestCase):
    def test_url_contains_provider(self):
        c = Client()
        response = c.get("/api/qpsru", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("https://qps.ru/" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/qpsru")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/qpsru")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class tinyccCase(TestCase):
    @skipIf(not get_vars("tinyccAPI"), "tinyccAPI env vars not set")
    @skipIf(not get_vars("tinyccLogin"), "tinyccLogin env vars not set")
    def test_url_contains_provider(self):
        c = Client()
        response = c.get("/api/tinycc", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("http://tiny.cc/" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/tinycc")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/tinycc")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class shrturiCase(TestCase):
    def test_url_contains_provider(self):
        c = Client()
        response = c.get("/api/shrturi", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("https://shrturi.com" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/shrturi")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/shrturi")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class cleanuriCase(TestCase):
    def test_url_contains_provider(self):
        c = Client()
        response = c.get("/api/cleanuri", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("https://cleanuri.com" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/cleanuri")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/cleanuri")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class relinkCase(TestCase):
    def test_url_contains_provider(self):
        c = Client()
        response = c.get("/api/relink", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("https://rel.ink/" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/relink")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/relink")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class qrcodeCase(TestCase):
    def test_url_contains_provider(self):
        c = Client()
        response = c.get("/api/qrcode", {"url": "https://www.google.fr"})
        ct = response["Content-type"]
        self.assertTrue(ct == "image/png")

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/qrcode")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/qrcode")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class kuttitCase(TestCase):
    @skipIf(not get_vars("kuttitAPI"), "I don't want to run this test yet")
    def test_url_contains_provider(self):
        c = Client()
        response = c.get("/api/kuttit", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("https://kutt.it/" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/kuttit")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/kuttit")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class vgdCase(TestCase):
    def test_url_contains_provider(self):
        c = Client()
        response = c.get("/api/vgd", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("https://v.gd/" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/vgd")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/vgd")
        self.assertEqual(response.status_code, 405, "unexpected return code")


class zwsimCase(TestCase):
    def test_url_contains_provider(self):
        c = Client()
        response = c.get("/api/zwsim", {"url": "https://www.google.fr"})
        url = response.json()["url"]
        self.assertTrue("https://zws.im/" in url)

    def test_if_no_param(self):
        c = Client()
        response = c.get("/api/zwsim")
        self.assertEqual(response.status_code, 400, "unexpected return code")

    def test_only_get(self):
        c = Client()
        response = c.post("/api/zwsim")
        self.assertEqual(response.status_code, 405, "unexpected return code")
