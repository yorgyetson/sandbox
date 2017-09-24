from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ContentDisplayList.as_view()),
    url(r'^tag/(?P<tag>.+)$', views.ContentDisplayList.as_view()),
    url(r'^display/(?P<content_id>.+)/$', views.ContentDisplay.as_view()),
]
