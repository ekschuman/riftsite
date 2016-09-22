"""riftlarp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import django.contrib.auth.views
import riftsite.views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^lore/', riftsite.views.lore_view),
    url(r'^stats/', riftsite.views.stats_view),
    url(r'^skills', riftsite.views.skills_view),
    url(r'^guide', riftsite.views.guide_view),
    url(r'^codex/', riftsite.views.codex_view),
    url(r'^factions/(?P<faction_id>[0-9]+)/$', riftsite.views.faction_show, name='faction_show'),
    url(r'^factions/', riftsite.views.factions_view),
    url(r'^characters/(?P<char_id>[0-9]+)/$', riftsite.views.character_show, name='character_show'),
    url(r'^characters/', riftsite.views.characters_view),
    url(r'^login/$', django.contrib.auth.views.login),
    url(r'^logout/$', django.contrib.auth.views.logout),
    url(r'^register/$', riftsite.views.register, name='register'),
    url(r'^register/complete/$', riftsite.views.registration_complete, name='registration_complete'),
    url(r'^', riftsite.views.home_view),
]
