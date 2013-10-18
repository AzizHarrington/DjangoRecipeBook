from django.conf.urls import patterns, include, url
from dishes.views import Home

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
    url(r'^$', Home.as_view(), name="home"), 
    url(r'^recipes/', include('dishes.urls')),
)
