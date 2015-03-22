from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout
from app.subsystem.courses.course import *
import logging

# For Dev Purposes Only. This logger object can be identified as 'apps.view'
logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    return home(request)  # We'll have it hardcoded for now...


@cache_control(no_cache=True, must_revalidate=True)
def home(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated():
        return menu(request)
    # else, then redirect
    return render(
        request,
        'app/login.html'
        # #Below info is not needed for now.
        # context_instance = RequestContext(request,
        # {
        #     'title':'Home Page',
        #     'year':datetime.now().year,
        # })
    )


def register(request):
    return render(
        request,
        'app/register.html'
    )


@login_required
@cache_control(no_cache=True, must_revalidate=True)
def menu(request):
    if request.user.is_authenticated():
        return render(
            request,
            'app/menu.html'
        )
    else:
        return register(request)


def loginhandler(request):
    # Handle login at any level and redirect to Menu.html
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            # If successful,
            login(request, user)
            return HttpResponseRedirect('/')  # This eliminates the loginhandler from the path

        else:
            # print ("Invalid login details: {0}, {1}".format(username, password))
            return render(request,
                          'app/login.html',
                          {'hasMessage': True, 'message': 'Login not successful. Check your username and password.'})
    # End loginhandler()

def logouthandler(request):
    logout(request)
    return render(request,
                  'app/login.html',
                {'hasMessage': True, 'message': 'Logout succesful. We hope to see you again!'})

##################################################################################################
# Methods yet to be correctly implemented


@login_required
def user_profile(request):
    return render(
        request,
        'app/user_profile.html'
    )


@login_required
def change_details(request):
    return render(
        request,
        'app/change_details.html'
    )


@login_required
def change_pass(request):
    return render(
        request,
        'app/change_pass.html'
    )


@login_required
def change_email(request):
    return render(
        request,
        'app/change_email.html'
    )


@login_required
def schedule_make(request):
    return render(
        request,
        'app/schedule_make.html'
    )


@login_required
def schedule_select(request):
    return render(
        request,
        'app/schedule_select.html'
    )


@login_required
def schedule_view(request):
    return render(
        request,
        'app/schedule_view.html'
    )

@login_required
def browse_all_courses(request):
    courseList = Course.objects.all()  # List of all courses
    return render(
        request,
        'app/browse_all_courses.html',
        {'courseList': courseList}  # Send it off to the template for rendering
    )

##################################################################################################
# Dev methods to test features and not break flow


def work_in_progress(request):
    html = "<html><body>The website template you requested is currently being worked on</body></html>"
    return HttpResponse(html)


def nullhandler(request):
    # This method does nothing other than print out the stuff it is receiving
    html = "<html><body>Transaction Logged</body></html>"
    for some in Course.objects.all():
        print(str(some.deptnum)+":"+str(some.name))
    logger.debug(str(request.POST))
    return HttpResponse(html)

