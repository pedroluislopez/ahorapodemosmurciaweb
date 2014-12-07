'''
Created on 29/11/2014

@author: plopez
'''

from django.conf.urls import patterns, url

from blog import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='blog-index'),
    url(r'^(?P<num_page>[\d]+)$', views.index, name='blog-index'),
    url(r'^post/(?P<slug>[-\w]+)/$', views.post, name='blog-post'),
)