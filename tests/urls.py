from django.conf.urls import patterns, include
import os


app_urls = []
for dir in os.listdir("tests/apps"):
   if os.path.isfile("tests/apps/%s/urls.py" % dir):
      app_urls += [(r'^%s/' % dir, include("tests.apps.%s.urls" % dir)),]

urlpatterns = patterns(
   '',
   *app_urls
)
