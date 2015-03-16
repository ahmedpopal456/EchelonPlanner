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
    url(r'^nullhandler/', 'app.views.nullhandler', name='nullhandler'),
    url(r'^logout/', 'app.views.logouthandler'),
    url(r'^loginhandler/','app.views.loginhandler'),
    url(r'^work_in_progress/', 'app.views.work_in_progress'),
    url(r'^user_profile/', 'app.views.user_profile',name = 'user_profile'),
    url(r'^changeDetails/','app.views.changeDetails',name = 'changeDetails'),
    url(r'^changePass/','app.views.changePass',name = 'changePass'),
    url(r'^changeEmail/','app.views.changeEmail',name = 'changeEmail'),
)
