from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin

# This file tells Django to map the URL strings to a particular method to call.
# Preferably all methods should be in the views.py file

# Examples:
# url(r'^blog/', 'app.views.index') || So, url([regular expression], [function to call])

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.index'),
    url(r'^register/', 'app.views.register'),
    url(r'^menu/', 'app.views.menu'),
    url(r'^nullhandler/', 'app.views.nullhandler'),
    url(r'^logout/', 'app.views.logouthandler'),
    url(r'^login_handler', 'app.views.login_handler'),
    url(r'^work_in_progress/', 'app.views.work_in_progress'),
    url(r'^user_profile/', 'app.views.user_profile'),
    url(r'^change_details/', 'app.views.change_details'),
    url(r'^change_pass/', 'app.views.change_pass'),
    url(r'^change_email/', 'app.views.change_email'),
    url(r'^schedule_make/', 'app.views.schedule_make'),
    url(r'^schedule_select/', 'app.views.schedule_select'),
    url(r'^schedule_view/', 'app.views.schedule_view'),
    url(r'^browse_all_courses/', 'app.views.browse_all_courses'),
    url(r'^course_create/', 'app.views.course_create'),
    url(r'^glorious_schedule_assembly/', 'app.views.glorious_schedule_assembly'),
    url(r'^concordia_resources/', 'app.views.concordia_resources'),
    url(r'^schedule_generator/', 'app.views.schedule_generator'),
    url(r'^sched_gen_1/', 'app.views.sched_gen_1'),
    url(r'^favicon.ico$', RedirectView.as_view(url='/static/favicon.ico'))
)
