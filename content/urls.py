from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ContentDisplayList.as_view()),
    url(r'^all$', views.ContentDisplayList.as_view()),
    url(r'^(?P<tag>.+)$', views.ContentDisplayList.as_view()),

    url(r'^show/(?P<content_id>.+)$', views.ContentDisplay.as_view()),
]
