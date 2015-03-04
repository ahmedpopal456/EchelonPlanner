from django.conf.urls import patterns, include, url
from django.contrib import admin

# This file tells Django to map the URL strings to a particular method to call.
# Preferably all methods should be in the views.py file

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'echelon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.index', name='index'),
    url(r'^login/','app.views.home',name = 'home'),
    url(r'^register/','app.views.register',name = 'register'),
    url(r'^menu/', 'app.views.menu', name='menu'),
    url(r'^login2/', 'app.views.login2', name='login2'),
    url(r'^register2/', 'app.views.register2', name='register2'),
    url(r'^nullhandler/', 'app.views.nullhandler', name='nullhandler'),
    url(r'^logout/', 'app.views.logouthandler'),
    url(r'^loginhandler/','app.views.loginhandler')
)
