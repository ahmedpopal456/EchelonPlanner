from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import logging

# For Dev Purposes Only. This logger object can be identified as 'apps.view'
logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    return home(request)  # We'll have it hardcoded for now...


def home(request):
    assert isinstance(request, HttpRequest)
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


def login2(request):
    return render(
        request,
        'app/login.html'
    )


def register(request):
    return render(
        request,
        'app/register.html'
    )


def register2(request):
    return render(
        request,
        'app/register.html'
    )


@login_required
def menu(request):
    if request.user.is_authenticated():
        return render(
            request,
            'app/menu.html'
        )
    else:
        return register2(request)


def loginhandler(request):
    # Handle login at any level and redirect to Menu.html
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            # If successful,
            login(request, user)
            return render(request, 'app/menu.html', {'hasMessage': False, 'message': str()})
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

# TODO: Remove this method and correctly handle HTTP Post requests for login/register!


def nullhandler(request):
    # This method does nothing other than print out the stuff it is receiving
    html = "<html><body>Transaction Logged</body></html>"
    logger.debug(str(request.POST))
    return HttpResponse(html)

