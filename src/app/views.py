from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .subsystem import *

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
        # 'title':'Home Page',
        #     'year':datetime.now().year,
        # })
    )


def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    # If it's a HTTP POST, we're interested in processing form data.

    if request.method == 'POST':
        # Attempt to grab information from the raw form information.

        studentuser = Student()
        message = []
        isregistered = False

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if username == "":
            message.append("Please enter a valid username")

        if password1 == "" or password2 == "":
            message.append("Please fill in both password blocks")

        if firstname == "" or lastname == "":
            message.append("Please fully fill in your name and last name")

        if email == "":
            message.append("Please fill in the email address block")

        if (password1 == password2) and (message == ""):
            studentuser.user.set_password(password1)
            studentuser.user.set_username(username)
            studentuser.user.set_email(email)
            studentuser.user.set_firstname(firstname)
            studentuser.user.set_lastname(lastname)
            studentuser.user.set_is_active(1)
            studentuser.user.set_is_staff(0)
            studentuser.user.set_is_superuser(0)
            studentuser.user.save()
            studentuser.save()
            isregistered = True

            return render(request,
                      'app/login.html',
                      {'hasMessage': True, 'message': ['Registration is successful.'], 'registered': isregistered})
        # Something failed :/
        else:
            return render(request,
                      'app/register.html',
                      {'hasMessage': True, 'message': message, 'registered': isregistered})

    # end If Request==Post

    else:  # Request is not Post, just serve the damn page
        return render(request,
                  'app/register.html')

        # End Register Method


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
def error_404(request):
    return render(
        request,
        'app/error_404.html'
    )


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
    if request.method == 'POST':
        # There should be post parameters with certain parameters to throw at the course catalogue
        # the return would be, therefore be a subset of the full course set.
        print()
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
        print(str(some.deptnum) + ":" + str(some.name))
    logger.debug(str(request.POST))
    return HttpResponse(html)

