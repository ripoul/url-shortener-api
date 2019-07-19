import os
from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.urls import reverse
import json


def providers(request):
    try:
        host = request.META["HTTP_HOST"]
    except:
        host = ""

    ret = [
        {
            "name": "rebrandly",
            "url": request.scheme + "://" + host + reverse(rebrandly),
        },
        {"name": "tinyurl", "url": request.scheme + "://" + host + reverse(tinyurl)},
        {"name": "cuttly", "url": request.scheme + "://" + host + reverse(cuttly)},
        {"name": "test", "url": request.scheme + "://" + host + reverse(cuttly)},
    ]
    return HttpResponse(json.dumps(ret), content_type="application/json")


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
            "apikey": os.getenv("rebrandlyAPI"),
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
            ret = json.dumps(
                {
                    "error": "error with the request to the rebrandly api",
                    "detail": r.text,
                }
            )
            return HttpResponse(ret, status=400, content_type="application/json")
    else:
        ret = json.dumps({"error": "url parameter missing"})
        return HttpResponse(ret, status=400, content_type="application/json")


def cuttly(request):
    url = request.GET.get("url", "")
    if url:
        payload = {"short": url, "key": os.getenv("cuttlyAPI")}
        r = requests.get("https://cutt.ly/api/api.php", params=payload)
        ret = json.dumps({"url": r.json()["url"]["shortLink"]})
        return HttpResponse(ret, content_type="application/json")
    else:
        ret = json.dumps({"error": "url parameter missing"})
        return HttpResponse(ret, status=400, content_type="application/json")
