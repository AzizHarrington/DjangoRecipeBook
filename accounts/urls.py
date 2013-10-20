from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^login/$', 'accounts.views.login', name='login'),
    url(r'^auth/$', 'accounts.views.auth_view', name='auth_view'),
    url(r'^loggedin/$', 'accounts.views.loggedin', name='loggedin'),
    url(r'^invalid/$', 'accounts.views.invalid_login', name='invalid'),
    url(r'^logout/$', 'accounts.views.logout', name='logout'),
    url(r'^register/$', 'accounts.views.register_user', name='register'),
    url(r'^success/$', 'accounts.views.register_user', name='success'),
)