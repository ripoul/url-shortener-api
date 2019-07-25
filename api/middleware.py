import json
from django.http import HttpResponse


class APIMiddleware:
    def process_request(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        url = request.GET.get("url", "")
        if not url:
            ret = json.dumps({"error": "url parameter missing"})
            return HttpResponse(ret, status=400, content_type="application/json")