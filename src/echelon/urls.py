from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin

# This file tells Django to map the URL strings to a particular method to call.
# Preferably all methods should be in the views.py file

# Examples:
# url(r'^blog/', 'app.views.index') || So, url([regular expression], [function to call])

urlpatterns = patterns('',
    # SUDO
    url(r'^admin/', include(admin.site.urls)),
    # DEV ONLY URLS!!!!!!
    url(r'^nullhandler/', 'app.views.nullhandler'),
    url(r'^work_in_progress/', 'app.views.work_in_progress'),

    # User Management and general navigation
    url(r'^$', 'app.views.index'),
    url(r'^register/', 'app.views.register'),
    url(r'^menu/', 'app.views.menu'),
    url(r'^logout/', 'app.views.logouthandler'),
    url(r'^login_handler', 'app.views.login_handler'),
    url(r'^user_profile/', 'app.views.user_profile'),
    url(r'^change_details/', 'app.views.change_details'),
    url(r'^change_pass/', 'app.views.change_pass'),
    url(r'^change_email/', 'app.views.change_email'),
    url(r'^student_record/','app.views.student_record'),

    # Schedule URLs
    url(r'^sched_gen_1/', 'app.views.sched_gen_1'),                 # Schedule Generation Selector (Manual v. Auto)
    url(r'^schedule_generator/', 'app.views.schedule_generator'),   # Manual Mode
    url(r'^sched_gen_auto/', 'app.views.sched_gen_auto'),           # Auto Mode
    url(r'^schedule_select/', 'app.views.schedule_select'),         # Select after Auto.
    url(r'^schedule_view/$', 'app.views.schedule_view', {'render_type': 'normal'}),       # Display Main Schedule
    url(r'^schedule_print_view/$', 'app.views.schedule_view', {'render_type': 'basic'}),  # Print View of Main Schedule
    # Selective Schedule View URLs
    url(r'^schedule_view/recent/(?P<specific>[0-9]{1,16})/$', 'app.views.schedule_view', {'render_type': 'normal', 'search_mode': 'recent'}),
    url(r'^schedule_view/saved/(?P<specific>[0-9]{1,16})/$', 'app.views.schedule_view', {'render_type': 'normal','search_mode': 'saved'}),
    url(r'^schedule_print_view/recent/(?P<specific>[0-9]{1,16})/$', 'app.views.schedule_view', {'render_type': 'basic','search_mode': 'recent'}),
    url(r'^schedule_print_view/saved/(?P<specific>[0-9]{1,16})/$', 'app.views.schedule_view', {'render_type': 'basic','search_mode': 'saved'}),
    # Probably Deprecated.
    url(r'^schedule_make/', 'app.views.schedule_make'),





    # Course URLs
    url(r'^browse_all_courses/', 'app.views.browse_all_courses'),
    url(r'^browse_specific_course/(?P<deptnum>[A-z]{4}[0-9]{3})', 'app.views.browse_specific_course'),
    url(r'^course_create/', 'app.views.course_create'),
    url(r'^course_data/','app.views.serializeCourseForSemester'),

    # Misc
    url(r'^concordia_resources/', 'app.views.concordia_resources'),
    url(r'^help/', 'app.views.help_site'),
    url(r'^404/', 'app.views.error_404'),
    url(r'^about/', 'app.views.about'),
    url(r'^credits/', 'app.views.credits_page'),
    url(r'^favicon.ico$', RedirectView.as_view(url='/static/favicon.ico')),

    # REST API URLs
    url(r'^course/(?P<deptnum>[A-z]{4}[0-9]{3})','app.views.course_dispatcher'),

    # Email confirmation URLs
    url(r'^emailconfirmation/(?P<hasheduser>[\w{}.-]{64})','app.views.index'),
)
