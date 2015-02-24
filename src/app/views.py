from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
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
    #TODO: Block access to menu with a sign-in
    return render(
        request,
        'app/menu.html'
    )

#TODO: Remove this method and correctly handle HTTP Post requests for login/register!
@csrf_exempt
def nullHandler(request):
    #This method does nothing other than log the request it receives.
    html = "<html><body>Your request was processed</body></html>"
    logger.debug( str(request.POST) )
    return HttpResponse(html)


