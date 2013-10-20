from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from .views import list_view, detail, new, edit, delete
from .api import RecipeResource

recipe_resource = RecipeResource()


urlpatterns = patterns('',
    url(r'^list/?', list_view, name="list"),
    url(r'^detail/(?P<pk>\d+)/?$', detail, name="detail"),
    url(r'^new/?', login_required(new), name="new"),
    url(r'^edit/(?P<pk>\d+)/?$', login_required(edit), name="edit"),
    url(r'^delete/(?P<pk>\d+)/?$', login_required(delete), name="delete"), 
    url(r'^api/', include(recipe_resource.urls)),
)