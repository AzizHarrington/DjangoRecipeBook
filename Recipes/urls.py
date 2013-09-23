from django.conf.urls import patterns, include, url
from dishes.views import Home, List, Detail, New, Edit, Delete

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Recipes.views.home', name='home'),
    # url(r'^Recipes/', include('Recipes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home.as_view()),
    url(r'^list/', List.as_view()),
    url(r'^detail/(?P<pk>\d+)$', Detail.as_view()),
    url(r'^new/', New.as_view()),
    url(r'^edit/(?P<pk>\d+)$', Edit.as_view()),
    url(r'^delete/(?P<pk>\d+)$', Delete.as_view()),
)
