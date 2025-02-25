from django.urls import re_path
from . import views

app_name = 'tours'


urlpatterns = [

    re_path(r'^$', views.home, name='home'),
    re_path(r'^about_us/$', views.about_us, name='about_us'),
    re_path(r'^our_tours/$', views.safari, name='our_tours'),
    re_path(r'^gallery/$', views.gallery, name='gallery'),
    re_path(r'^reviews/$', views.reviews, name='reviews'),
    re_path(r'^contacts/$', views.contacts, name='contacts'),
    re_path(r'^success/$', views.success, name='success'),
    re_path(r"our_tours/new_tour/$", views.new_tour, name="new_tour"),
    re_path(r"our_tours/edit_tour/(?P<tour_id>\d+)/$", views.edit_tour, name="edit_tour"),
    re_path(r"our_tours/delete_tour/(?P<tour_id>\d+)/$", views.delete_tour, name="delete_tour"),
    re_path(r"about_us/add_guide/$", views.add_guide, name="add_guide"),
    re_path(r"guide_bio/(?P<guide_id>\d+)/$", views.guide_bio, name="guide_bio"),
    re_path(r"remove_guide/(?P<guide_id>\d+)/$", views.remove_guide, name="remove_guide"),
    re_path(r"edit_guide-info/(?P<guide_id>\d+)/$", views.edit_guide_info, name="edit_guide_info"),
    re_path(r"our_tours/(?P<tour_id>\d+)/(?P<tour_title>[-\w]+)/$", views.tour_info, name="tour_info"),
    re_path(r"(?P<tour_id>\d+)/(?P<tour_title>[-\w]+)/photos/$", views.tour_photos, name="tour_photos"),
    re_path(r"photos/(?P<photo_id>\d+)/$", views.photo, name="photo"),
    re_path(r"photos/(?P<photo_id>\d+)/delete_photo/$", views.delete_photo, name="delete_photo"),
    re_path(r"add_photo/(?P<tour_title>[-\w]+)/(?P<tour_id>\d+)/$", views.add_photos, name="add_photos"),
    re_path(r'(?P<tour_id>\d+)/(?P<tour_title>[-\w]+)/new_review/$', views.new_review, name='new_review'),
    re_path(r'our_tours/(?P<review_id>\d+)/delete_review/$', views.delete_review, name='delete_review'),
    re_path(r'^transfers/$', views.transfers, name='transfers'),
    re_path(r'our_tours/beach_tours/$', views.beach_tours, name="beach_tours"),
    re_path(r'our_tours/city_tours/$', views.city_tours, name="city_tours"),
    re_path(r'our_tours/cultural_tours/$', views.cultural_tours, name="cultural_tours"),
]