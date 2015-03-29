from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
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


def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw POST information.
        studentUser = Student()
        standardUser = User()
        message = []
        isregistered = False

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['email']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        studentID = request.POST['idnum']

        # Log Everything
        logger.debug(str(request.POST))

        if username == "":
            message.append("Please enter a valid username")

        if password1 == "" or password2 == "":
            message.append("Please fill in both password blocks")

        if firstname == "" or lastname == "":
            message.append("Please fully fill in your name and last name")

        if email == "" or '@' not in str(email):
            message.append("Please fill in the email address block")

        if studentID is None or len(studentID) > 8 or len(studentID) < 7:
            message.append("The ID Number provided is invalid")

        if (password1 == password2) and (message == []):
            # Everything checks out and is all working fine :)
            # Create the Standard User first and try storing it in the database
            standardUser.set_password(password1)
            standardUser.username = username
            standardUser.email = email
            standardUser.first_name = firstname
            standardUser.last_name = lastname
            standardUser.is_active = True
            standardUser.is_staff = False
            standardUser.is_superuser = False
            try:
                standardUser.save() # Save the Django user in the Database.
                # Now let's try putting that Student user in the DB
                studentUser.user = standardUser
                # standardUser.save()
                studentUser.save()
                isregistered = True
            except IntegrityError as problem:
                # Student or auth_user was duplicate
                isregistered = False
                logger.warn(str(problem.args))
                message.append("User already Exists!")
        # end last If check

        if isregistered:
            return render(request,
                      'app/login.html',
                      {'hasMessage': True, 'message': ['Registration is successful.'], 'registered': isregistered})

        else:  # User was not registered
            return render_to_response(
                      'app/register.html',
                      {'hasMessage': True, 'message': message, 'registered': isregistered},
                      context_instance=RequestContext(request))

        # end If Request==Post

    else:  # Request is not Post, just serve the damn page
        return render(request,
                  'app/register.html')
# End Register Method


@login_required
def user_profile(request):
    # Request Dictionary
    all_info = {}
    specific_info ={}
    # Get all user information
    mainProfile = request.user
    all_info['firstname'] = mainProfile.first_name
    all_info['lastname'] = mainProfile.last_name
    all_info['email'] = mainProfile.email
    all_info['dateJoined'] = mainProfile.date_joined
    all_info['lastLogin'] = mainProfile.last_login

    # Check for specific info
    a = Student.objects.get(user_id=mainProfile.id)
    if a:
        specificProfile = a
        specific_info = specificProfile.__unicode__()
        specific_info['professor']=False

    all_info.update(specific_info)

    logger.debug(all_info)
    return render(
        request,
        'app/user_profile.html',
        all_info
    )
# end user_profile


@login_required
def change_pass(request):
    loadPage = 'app/change_pass.html'
    message = str()

    if request.method=='POST':
        password1 = request.POST['password1']
        if password1==request.POST['password2']:
            request.user.set_password(password1)
            request.user.save()
            message = "Password Successfully Updated"
            loadPage = str() # Automatically redirects to main profile page
        else:
            message = "Error: Inputs did not match. Please Try Again."
    # end if request is POST

    return render(
        request,
        'app/user_profile.html',
        {'alternate': loadPage, 'message': message}
    )
# end change_pass


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
        '404.html'
    )


@login_required
def change_details(request):
    if request.method == 'POST':
        address = request.POST['address']
        homePhone = request.POST['homePhone']
        cellPhone = request.POST['cellPhone']
        request.user.student.address.__setattr__(address)
        request.user.student.homephone.__setattr__(homePhone)
        request.user.student.cellphone.__setattr__(cellPhone)
        request.user.save();
    return render(
        request,
        'app/change_details.html'
    )


@login_required
def change_email(request):
    if request.method == 'POST':
        email1 = request.POST['email1']
        email2 = request.POST['email2']
        if email1 == email2:
            request.user.email.__setattr__(email1)
            request.user.save();
        else:
            message = "Error: Inputs did not match. Please Try Again."

    return render(
        request,
        'app/change_email.html'
    )


@login_required
def schedule_make(request):#Needs to be looked at
    numberOfElectives = Option.option + Option.type  # How many electives are needed. Not sure if this is the method that should be used.
    availableElectives = Option.course #Not sure if this is the method
    if request.method == 'POST':
        prelim_choices = request.POST['choice'] # Since there may be more than one span with that name, this results in the needed array, right?
        schedule_select(prelim_choices) # Need to send prelim_choices to schedule select. This is probably not how it is done.

    return render(
        request,
        'app/schedule_make.html',
        {'numberOfElectives': numberOfElectives},
        {'availableElectives' : availableElectives}
    )


@login_required
def schedule_select(request): #Needs to be looked at
    partialSelection = set(prelim_choices).union(database.academicprogram.course) #I want it to show the union between the courses in the academic program, but  I want it to exclude any other optional course not present in the prelim_choices. This does not do that.
    if request.method == 'Post':
        rawSchedule = request.POST('choice') #Needs to send the selected radio buttons' values to schedule_select_continue
    return render(
        request,
        'app/schedule_select.html',
        {'partialSelection' : partialSelection},
        {'maxYear' : 4} #hardcorded max years
    )


@login_required
def schedule_view(request):
    # Hardcoded Timeslot Values (No reason to generate them anew each time)
    # These were generated by the following Bash command
    # for i in {7..20}:{00..59..15}; do completeList=$completeList","`echo \"$i\"`; done
    timeSlots=["7:00","7:15","7:30","7:45","8:00","8:15","8:30","8:45","9:00","9:15","9:30","9:45","10:00","10:15","10:30","10:45","11:00","11:15","11:30","11:45","12:00","12:15","12:30","12:45","13:00","13:15","13:30","13:45","14:00","14:15","14:30","14:45","15:00","15:15","15:30","15:45","16:00","16:15","16:30","16:45","17:00","17:15","17:30","17:45","18:00","18:15","18:30","18:45","19:00","19:15","19:30","19:45","20:00","20:15","20:30","20:45"]

    return render(
        request,
        'app/schedule_view.html',
        {'timeSlots': timeSlots}
    )

@login_required
def course_create(request):
    if request.method == 'POST':
        name = request.POST('name')
        number = request.POST('number')
        department = request.POST('department')
        type = request.POST('type')
        credits = request.POST('credits')
        prerequisites = request.POST('prerequisites')
        equivalence = request.POST('equivalence')
        yearSpan = request.POST('yearSpan')
        newCourse = courses.Course.new()
        newCourse.course.department = department
        newCourse.course.type = type
        newCourse.course.number = number
        newCourse.course.credits = credits
        newCourse.course.name = name
        newCourse.course.prerequisites = prerequisites
        newCourse.course.equivalence = equivalence
        newCourse.course.yearSpan = yearSpan
        database.coursecatalog.addCourse(name, number, department, credits)
    return render(
        request,
        'app/course_create.html',
    )


@login_required
def browse_all_courses(request):
    courseList = Course.objects.all()  # List of all courses
    if request.method == 'POST':
        course_credits = request.POST['credits']
        department = request.POST['department']
        search_string = request.POST['custom_string']

        if search_string == "":
            department_list = CourseCatalog.searchCourses(department)
            credit_list = CourseCatalog.searchCoursesByCredits(0, course_credits)
            intersection_set = set(department_list).intersection(credit_list)
            courseList = list(intersection_set)

        else:
            courseList = CourseCatalog.searchCourses(search_string)
        print(request.POST)
        print(courseList)
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

