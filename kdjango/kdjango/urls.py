"""kdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from boards import views
from accounts import views as accounts_views

#  Sidenote: PK or ID?
# 
# PK stands for Primary Key. It's a shortcut for accessing a model's primary key. 
# All Django models have this attribute.
# 
# For the most cases, using the pk property is the same as id. 
# That's because if we don't define a primary key for a model, 
# Django will automatically create an AutoField named id, 
# which will be its primary key.
# 
# If you defined a different primary key for a model, for example, 
# let's say the field email is your primary key. 
# To access it you could either use obj.email or obj.pk.
urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^admin/', admin.site.urls),
]