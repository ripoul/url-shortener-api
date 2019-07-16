from django.urls import path

from . import views

urlpatterns = [
    path("tinyurl", views.tinyurl, name="tinyurl"),
    path("rebrandly", views.rebrandly, name="rebrandly"),
]
