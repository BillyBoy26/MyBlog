from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil/$', views.accueil, name="accueil"),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^article/(?P<id_article>\d+)-(?P<slug>.+)$', views.read_article, name="read_article"),
]
