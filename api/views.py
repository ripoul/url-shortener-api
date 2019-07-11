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
        return HttpResponse(ret, content_type='application/json')
    else:
        ret = json.dumps({"error": "url parameter missing"})
        return HttpResponse(ret, status=400, content_type='application/json')
