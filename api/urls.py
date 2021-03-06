from django.urls import path

from . import views

urlpatterns = [
    path("providers", views.providers, name="providers"),
    path("tinyurl", views.tinyurl, name="tinyurl"),
    path("rebrandly", views.rebrandly, name="rebrandly"),
    path("cuttly", views.cuttly, name="cuttly"),
    path("bitly", views.bitly, name="bitly"),
    path("m360us", views.m360us, name="m360us"),
    path("osdblink", views.osdblink, name="osdblink"),
    path("isgd", views.isgd, name="isgd"),
    path("chilpit", views.chilpit, name="chilpit"),
    path("clckru", views.clckru, name="clckru"),
    path("dagd", views.dagd, name="dagd"),
    path("qpsru", views.qpsru, name="qpsru"),
    path("tinycc", views.tinycc, name="tinycc"),
    path("shrturi", views.shrturi, name="shrturi"),
    path("cleanuri", views.cleanuri, name="cleanuri"),
    path("relink", views.relink, name="relink"),
    path("qrcode", views.qrcode_view, name="qrcode"),
    path("kuttit", views.kuttit, name="kuttit"),
    path("vgd", views.vgd, name="vgd"),
    path("zwsim", views.zwsim, name="zwsim"),
]
