from django.urls import path

from . import views

urlpatterns = [
    path("providers", views.providers, name="providers"),
    path("tinyurl", views.tinyurl, name="tinyurl"),
    path("rebrandly", views.rebrandly, name="rebrandly"),
    path("cuttly", views.cuttly, name="cuttly"),
    path("bitly", views.bitly, name="bitly"),
    path("m360us", views.m360us, name="m360us"),
]
