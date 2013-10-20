from django.conf.urls import patterns, include, url
from dishes.views import list_view, detail, new, edit, delete

urlpatterns = patterns('',
    url(r'^list/?', list_view, name="list"),
    url(r'^detail/(?P<pk>\d+)/?$', detail, name="detail"),
    url(r'^new/?', new, name="new"),
    url(r'^edit/(?P<pk>\d+)/?$', edit, name="edit"),
    url(r'^delete/(?P<pk>\d+)/?$', delete, name="delete"), 
)