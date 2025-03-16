from django.urls import re_path
from . import views

app_name = 'blog'


urlpatterns = [

    re_path(r'^$', views.blog, name='blog'),
    re_path(r'^posts/(?P<topic_id>\d+)/(?P<topic_title>[-\w]+)/$', views.topic, name='topic'),
    re_path(r'^posts/(?P<topic_id>\d+)/(?P<entry_id>\d+)/(?P<entry_title>[-\w]+)/$', views.topic_entry, name='topic_entry'),

    # Creating and editing Posts and Post Entries
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    re_path(r'^(?P<topic_id>\d+)/edit_topic/$', views.edit_topic, name='edit_topic'),
    re_path(r'^(?P<topic_id>\d+)/new_entry/$', views.new_topic_entry, name='new_topic_entry'),
    re_path(r'^(?P<entry_id>\d+)/edit_post/$', views.edit_topic_entry, name='edit_topic_entry'),
    re_path(r'^topic/(?P<topic_id>\d+)/delete_topic/$', views.delete_topic, name='delete_topic'),
    re_path(r'^posts/(?P<entry_id>\d+)/delete_entry/$', views.delete_topic_entry, name='delete_topic_entry'),


]