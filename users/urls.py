from django.urls import re_path
from . import views

app_name = 'users'


urlpatterns = [
    re_path(r'^login/$', views.custom_login, name='login'),
    re_path(r'^logout/$', views.logout_view, name='logout'),
    re_path(r'register/$', views.register, name='register'),
    re_path(r'user_settings/$', views.user_settings, name='user_settings'),
    re_path(r'user_settings/edit_settings/(?P<user_id>\d+)/$', views.edit_settings, name='edit_settings'),

]