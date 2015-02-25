from django.shortcuts import render
from django.http import HttpRequest
# from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import logging

#For Dev Purposes Only. This logger object can be identified as 'apps.view'
logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
	return home(request) #We'll have it hardcoded for now...

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/login2.html'
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
        'app/login2.html'
    )

def register(request):
    return render(
        request,
        'app/register2.html'
    )

def register2(request):
    return render(
        request,
        'app/register2.html'
    )

def menu(request):
    # TODO: More Elegantly, Block access to menu with a sign-in
    if request.user.is_authenticated():
        return render(
            request,
            'app/menu.html'
        )
    else:
        return register2(request)

# TODO: Remove this method and correctly handle HTTP Post requests for login/register!

def nullhandler(request):
    # This method does nothing other than log the request it receives.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            html = "<html><body>Your request was processed correctly and you are logged in</body></html>"
        else:
            # print ("Invalid login details: {0}, {1}".format(username, password))
            html = "<html><body>There was a problem with your request</body></html>"
    logger.debug( str(request.POST) )
    return HttpResponse(html)

def logouthandler(request):
    logout(request)
    html = "<html><body>Your request was processed correctly and you are logged out</body></html>"
    return(html)

