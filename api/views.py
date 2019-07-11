from django.shortcuts import render
import requests
from django.http import HttpResponse
import json

def tinyurl(request):
    payload = {'url': request.GET.get('url', '')}
    r = requests.get("http://tinyurl.com/api-create.php", params=payload)
    ret = json.dumps({'url': r.text})
    return HttpResponse(ret)
