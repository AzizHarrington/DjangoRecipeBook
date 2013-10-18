from django.conf.urls import patterns, include, url
from dishes.views import List, Detail, New, Edit, Delete

urlpatterns = patterns('',
    url(r'^list/?', List.as_view(), name="list"),
    url(r'^detail/(?P<pk>\d+)/?$', Detail.as_view(), name="detail"),
    url(r'^new/?', New.as_view(), name="new"),
    url(r'^edit/(?P<pk>\d+)/?$', Edit.as_view(), name="edit"),
    url(r'^delete/(?P<pk>\d+)/?$', Delete.as_view(), name="delete"), 
)