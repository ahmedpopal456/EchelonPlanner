from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def index(request):
	return home(request) #We'll have it hardcoded for now...

def home(request):
    """Renders the home page."""
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

def register(request):
    return render(
        request,
        'app/register.html'
    )

def menu(request):
    return render(
        request,
        'app/menu.html'
    )


def login2(request):
    return render(
        request,
        'app/login2.html'
    )