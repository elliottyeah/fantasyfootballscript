"""fantasyfootball URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^criteria/', include('criteria.urls')),
    url(r'^players/', include('players.urls')),
	url(r'^$','home.views.index'),
	url(r'^home','home.views.index'),
    url(r'^player-search','home.views.find_player'),
    url(r'^player-results','home.views.find_player'),
    url(r'^test/','home.views.test'),
    url(r'^about','home.views.about'),
    url(r'^contact','home.views.contact'),
    url(r'^thanks','home.views.thanks'),



]
