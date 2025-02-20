from django.urls import re_path
from . import views

app_name = 'tours'


urlpatterns = [

    re_path(r'^$', views.home, name='home'),
    re_path(r'^about_us/$', views.about_us, name='about_us'),

]