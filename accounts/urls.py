from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^login/$', 'accounts.views.login', name='login'),
    url(r'^auth/$', 'accounts.views.auth_view', name='auth_view'),
    url(r'^loggedin/$', 'accounts.views.loggedin', name='loggedin'),
    url(r'^invalid/$', 'accounts.views.invalid_login', name='invalid'),
    url(r'^logout/$', 'accounts.views.logout', name='logout'),
    url(r'^register/$', 'accounts.views.register_user', name='register'),
    url(r'^success/$', 'accounts.views.register_success', name='success'),
    url(r'^reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
            'accounts.views.reset_confirm', name='reset_confirm'),
    url(r'^reset/$', 'accounts.views.reset', name='reset'),
)