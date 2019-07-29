import os
from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.urls import reverse
import json
from django.views.decorators.http import require_http_methods
from .middleware import APIMiddleware
from django.utils.decorators import decorator_from_middleware


@require_http_methods(["GET"])
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
        {"name": "bitly", "url": request.scheme + "://" + host + reverse(bitly)},
        {"name": "m360us", "url": request.scheme + "://" + host + reverse(m360us)},
    ]
    return HttpResponse(json.dumps(ret), content_type="application/json")


@require_http_methods(["GET"])
@decorator_from_middleware(APIMiddleware)
def tinyurl(request):
    url = request.GET.get("url", "")
    payload = {"url": url}
    r = requests.get("http://tinyurl.com/api-create.php", params=payload)
    ret = json.dumps({"url": r.text})
    return HttpResponse(ret, content_type="application/json")


@require_http_methods(["GET"])
@decorator_from_middleware(APIMiddleware)
def rebrandly(request):
    url = request.GET.get("url", "")
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
            {"error": "error with the request to the rebrandly api", "detail": r.text}
        )
        return HttpResponse(ret, status=400, content_type="application/json")


@require_http_methods(["GET"])
@decorator_from_middleware(APIMiddleware)
def cuttly(request):
    url = request.GET.get("url", "")
    payload = {"short": url, "key": os.getenv("cuttlyAPI")}
    r = requests.get("https://cutt.ly/api/api.php", params=payload)
    ret = json.dumps({"url": r.json()["url"]["shortLink"]})
    return HttpResponse(ret, content_type="application/json")


@require_http_methods(["GET"])
@decorator_from_middleware(APIMiddleware)
def bitly(request):
    url = request.GET.get("url", "")
    linkRequest = {"long_url": url, "group_guid": os.getenv("bittlyAPIgroup")}

    requestHeaders = {
        "Content-type": "application/json",
        "Authorization": "Bearer " + os.getenv("bitlyAPI"),
    }

    r = requests.post(
        "https://api-ssl.bitly.com/v4/shorten",
        data=json.dumps(linkRequest),
        headers=requestHeaders,
    )

    if r.status_code == 200 or r.status_code == 201:
        link = r.json()
        ret = json.dumps({"url": link["link"]})
        return HttpResponse(ret, content_type="application/json")

    ret = json.dumps(
        {
            "error": "error with the request to the bitly api",
            "detail": r.text,
            "code": r.status_code,
        }
    )
    return HttpResponse(ret, status=400, content_type="application/json")


@require_http_methods(["GET"])
@decorator_from_middleware(APIMiddleware)
def m360us(request):
    url = request.GET.get("url", "")
    payload = {"link": url}
    r = requests.post("https://m360.us/add", data=payload)
    ret = json.dumps({"url": "http://"+r.text})
    return HttpResponse(ret, content_type="application/json")