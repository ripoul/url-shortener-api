from django.shortcuts import render
import requests
from django.http import HttpResponse
import json


def tinyurl(request):
    url = request.GET.get("url", "")
    if url:
        payload = {"url": url}
        r = requests.get("http://tinyurl.com/api-create.php", params=payload)
        ret = json.dumps({"url": r.text})
        return HttpResponse(ret, content_type="application/json")
    else:
        ret = json.dumps({"error": "url parameter missing"})
        return HttpResponse(ret, status=400, content_type="application/json")


def rebrandly(request):
    url = request.GET.get("url", "")
    if url:
        linkRequest = {
            "destination": url,
            "domain": {"fullName": "rebrand.ly"}
            # , "slashtag": "A_NEW_SLASHTAG"
            # , "title": "Rebrandly YouTube channel"
        }


        requestHeaders = {
            "Content-type": "application/json",
            "apikey": "7b9459064585418cbcb1fc2538e2d2a9",
            "workspace": "3e8f5fd7ef014e58b9f605737d91c750",
        }

        r = requests.post(
            "https://api.rebrandly.com/v1/links",
            data=json.dumps(linkRequest),
            headers=requestHeaders,
        )

        if r.status_code == requests.codes.ok:
            link = r.json()
            ret = json.dumps({"url": link["shortUrl"]})
            return HttpResponse(ret, content_type="application/json")
        else:
            ret = json.dumps({"error": "error with the request to the rebrandly api", "detail": r.text})
            return HttpResponse(ret, status=400, content_type="application/json")
    else:
        ret = json.dumps({"error": "url parameter missing"})
        return HttpResponse(ret, status=400, content_type="application/json")
