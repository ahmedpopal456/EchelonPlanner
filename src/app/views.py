import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import RequestContext
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import hashers
from django.contrib.sessions.backends.base import SessionBase
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


def login_handler(request):
    # Handle login_handler at any level and redirect to Menu.html
    if request.method == 'POST':
        print(str(request.POST))
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            # If successful,
            login(request, user)
            if "remember-me" not in request.POST:
                request.session.set_expiry(0) # Basically, close after the browser closes.
            return HttpResponseRedirect('/')  # This eliminates the login_handler from the path

        else:
            # print ("Invalid login_handler details: {0}, {1}".format(username, password))
            return render(request,
                          'app/login.html',
                          {'hasMessage': True, 'message': 'Login not successful. Check your username and password.'})
    else:
        return home(request)
# End login_handler()


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
                newRecord = StudentRecord()
                newRecord.save()
                studentUser.academicRecord = newRecord
                # We need to create and save a main schedule as well to the student
                mainSchedule = Schedule()
                mainSchedule.save()
                studentUser.academicRecord.mainSchedule = mainSchedule
                # Student ID must also be saved
                studentUser.IDNumber = studentID
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

    a = StudentCatalog.getStudent(mainProfile.username)


    # Check for specific info
    #a = Student.objects.get(user_id=mainProfile.id)
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
        # Take the input Password
        password1 = request.POST['password1']
        # 1. Check their old passwords
        if hashers.check_password(request.POST['oldPass'], request.user.password):
            # 2. Check if user submitted the same password
            if password1==request.POST['password2']:
                request.user.set_password(password1)
                request.user.save()
                message = "Password Successfully Updated"
                loadPage = str() # Automatically redirects to main profile page
            else: # Submitted Passwords were incorrect
                message = "Error: Inputs did not match. Please Try Again."
        else: # User was not authenticated succesfully
            message = "Error: Your old password was wrong. We cannot update your password"
    # end if request is POST

    return render(
        request,
        'app/user_profile.html',
        {'alternate': loadPage, 'message': message}
    )
# end change_pass


def logouthandler(request):
    logout(request)
    return HttpResponseRedirect('/', {'hasMessage': True, 'message': 'Logout succesful. We hope to see you again!'})
    return render(request,
                  'app/login.html',
                  {'hasMessage': True, 'message': 'Logout succesful. We hope to see you again!'})


@login_required
def concordia_resources(request):
    return render(
        request,
        'app/concordia_resources.html'
    )


@login_required
def error_404(request):
    return render(
        request,
        '404.html'
    )


@login_required
def change_details(request):
    loadPage = 'app/change_details.html'
    message = str()

    oldCellPhone = request.user.student.cellphone
    oldHomePhone = request.user.student.homephone
    oldAddress = request.user.student.address


    if request.method == 'POST':
        print(request.POST)
        address = request.POST['address']
        homePhone = request.POST['homePhone']
        cellPhone = request.POST['cellPhone']
        # TODO: check if Empty and avoid updating field
        request.user.student.address = address
        request.user.student.homephone = homePhone
        request.user.student.cellphone = cellPhone
        request.user.student.save()
        loadPage = str()
    return render(
        request,
        'app/user_profile.html',
        {'alternate': loadPage, 'message': message,
        'homePhone': oldHomePhone,
        'cellPhone': oldCellPhone,
        'address': oldAddress}
    )
# end change_details


@login_required
def change_email(request):
    message = str()
    loadPage = 'app/change_email.html'
    if request.method == 'POST':
        email1 = request.POST['email1']
        email2 = request.POST['email2']
        if email1 == email2:
            request.user.email =email1
            request.user.save()
            loadPage = str()
        else:
            message = "Error: Inputs did not match. Please Try Again."

    return render(
        request,
        'app/user_profile.html',
        {'alternate': loadPage, 'message': message}
    )


@login_required
def schedule_make(request):  # Might as well rework this method from scratch, but you can see what the logic was intended to be
    numberOfElectives = [1,2,3,4,5,6,7,8,9]  # Need to create list containing how many choices user gets to make
    availableElectives = CourseCatalog.searchCoursesThroughPartialName("SOEN")  # Not sure what method to use to call electives related to the user's academic program
    if request.method == 'POST':
        prelim_choices = []
        print(request.POST)
        for item in range(1, 12):
            prelim_choices.append(request.POST("choice " + str(item)))

    return render(
        request,
        'app/schedule_make.html',
        {'numberOfElectives': numberOfElectives,
         'availableElectives': availableElectives}
    )


@login_required
def schedule_select(request): #Needs to be looked at
    partialSelection = set(prelim_choices).union(database.academicprogram.course) #I want it to show the union between the courses in the academic program, but  I want it to exclude any other optional course not present in the prelim_choices. This does not do that.
    if request.method == 'Post':
        rawSchedule = request.POST('choice') #Needs to send the selected radio buttons' values to schedule_select_continue
    return render(
        request,
        'app/schedule_select.html',
        {'partialSelection': partialSelection,
         'maxYear': 4} # hardcorded max years
    )


@login_required
def schedule_view(request):
    # Hardcoded Timeslot Values (No reason to generate them anew each time)
    # These were generated by the following Bash command
    # for i in {7..20}:{00..59..15}; do completeList=$completeList","`echo \"$i\"`; done
    timeSlots=["8:45","9:00","9:15","9:30","9:45","10:00","10:15","10:30","10:45","11:00","11:15","11:30","11:45","12:00","12:15","12:30","12:45","13:00","13:15","13:30","13:45","14:00","14:15","14:30","14:45","15:00","15:15","15:30","15:45","16:00","16:15","16:30","16:45","17:00","17:15","17:30","17:45","18:00","18:15","18:30","18:45","19:00","19:15","19:30","19:45","20:00","20:15","20:30","20:45","21:00","21:15","21:30","21:45","22:00","22:15","22:30","22:45","23:00"]
    len(timeSlots)
    max_years = [1, 2, 3, 4, 5]
    semesterCycle=["Summer 1", "Summer 2", "Fall", "Winter"]
    feasable_courses = CourseCatalog.searchCoursesThroughPartialName("SOEN")

    return render(
        request,
        'app/schedule_view.html',
        {'timeSlots': timeSlots,
        'max_years': max_years,
         'feasable_courses': feasable_courses,
         'semesterCycle': semesterCycle}
    )

@login_required
def schedule_generator(request):
    # Loads Schedule Generator Page when we need to loop through semesters in a year and through all 4 years
    max_courses = [1, 2, 3, 4, 5]
    max_years = [1, 2, 3, 4, 5]
    feasable_courses = CourseCatalog.searchCoursesThroughPartialName("SOEN")
    for allCourses in feasable_courses:
        pass  # build some diction

    testTestList=["a","b","c"]
    if request.method == "POST":
        print(str(request.POST))

    semesterCycle=["Summer1","Summer2", "Fall", "Winter"]
    return render(
        request,
        'app/schedule_generator.html',
        {'max_courses': max_courses,
         'max_years': max_years,
         'feasable_courses': feasable_courses,
         'testTestList':testTestList,
         'semesterCycle':semesterCycle
        }
    )

@login_required
def sched_gen_1(request):

    if request.method == "POST": # get the response back
        #If POST, then
        max_courses = [1, 2, 3, 4, 5]
        # request.POST['semester'] # will return given semester!
        # TODO: CHECK FEASIBLE COURSES AGAINST SEMESTER SUPPLIED
        currentSemester = request.POST['semester']
        currentYear = request.POST['year']
        student = StudentCatalog.getStudent(request.user.username)

        if student:
            student = request.user.student  # Should be the primary key of student in database
            feasable_courses = CourseCatalog.coursesWithMetPrereqs(student, currentSemester, currentYear)  # INJECT "coursesWithMetPrereqs"
            # Supply curren

        else:
            feasable_courses= CourseCatalog.searchCoursesThroughPartialName("SOEN")

        testTestList=["a","b","c"] # REMOVE
        print(request.POST) # DEBUGGING

        # Check if automatic
        if request.POST['gen-type'] == "Automatic":
            return render(
                request,
                'app/schedule_generator_auto.html',
                {'max_courses': max_courses,
                 'feasable_courses': feasable_courses,
                 'testTestList': testTestList,
                 'currentYear': currentYear,
                 'currentSemester': currentSemester}
            )

        return render(
            request,
            'app/schedule_generator.html',
            {'max_courses': max_courses,
             'feasable_courses': feasable_courses,
             'testTestList': testTestList,
             'currentYear': currentYear,
             'currentSemester': currentSemester}
        )
    # end if request is POST

    # Phase 1: Ask for Semester.
    semesterCycle=["Summer1","Summer2", "Fall", "Winter"]
    max_years = [1, 2, 3, 4, 5]

    return render(
        request,
        'app/sched_gen_1.html',
        {'max_years': max_years,
         'semesterCycle': semesterCycle}
    )
#end sched_gen_1

#TODO: CLEANUP
@login_required
def glorious_schedule_assembly(request):
    max_courses = [1, 2, 3, 4, 5]
    feasable_courses = CourseCatalog.searchCoursesThroughPartialName("SOEN")  # Not sure what method to use to call electives related to the user's academic program
    if request.method == 'POST':
        prelim_choices = []
        print(request.POST)
        for item in range(1, 12):
            prelim_choices.append(request.POST["choice" + str(item)])
    testTestList=["a","b","c"]
    return render(
        request,
        'app/glorious_schedule_assembly.html',
        {'max_courses': max_courses,
         'feasable_courses': feasable_courses,
        'testTestList':testTestList}
    )

@login_required
def course_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        department = request.POST['department']
        type = request.POST['type']
        credits = request.POST['credits']
        prerequisites = request.POST['prerequisites']
        equivalence = request.POST['equivalence']
        yearSpan = request.POST['yearSpan']
        newCourse = courses.Course.new()
        newCourse.course.department = department
        newCourse.course.type = type
        newCourse.course.number = number
        newCourse.course.credits = credits
        newCourse.course.name = name
        newCourse.course.prerequisites = prerequisites
        newCourse.course.equivalence = equivalence
        newCourse.course.yearSpan = yearSpan
        CourseCatalog.addCourse(name, number, department, credits)
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
            if not department == "":
                department_list = list(Course.objects.filter(department=department))
            else:
                department_list = Course.objects.all()
            credit_list = CourseCatalog.searchCoursesByCredits(0, course_credits)
            intersection_set = set(department_list).intersection(credit_list)
            courseList = list(intersection_set)

        else:
            courseList = CourseCatalog.searchCoursesThroughPartialName(search_string)
        print(request.POST)
        print(courseList)

    return render(
        request,
        'app/browse_all_courses.html',
        {'courseList': courseList}  # Send it off to the template for rendering
    )
# end browse_all_courses


def browse_specific_course(request, deptnum=""):
    if deptnum == "":
        return browse_all_courses(request)

    else:
        specificcourse = CourseCatalog.searchCoursesThroughPartialName(deptnum)
        # If the list comes up empty, do a hard redirect!
        if len(specificcourse) == 0:
            return browse_all_courses(request)

        specificcourse = specificcourse[0]

        course_info = CourseCatalog.seralizeCourseForSemester(specificcourse)

        return render(
            request,
            'app/browse_specific_course.html',
            course_info
        )
# end browse_specific_course

@login_required()
def course_dispatcher(request, deptnum=""):
    if not deptnum == "":
        specificCourse = CourseCatalog.searchCoursesThroughPartialName(deptnum)
        # specificCourse = specificCourse
        data = serializers.serialize("json", specificCourse)
        return HttpResponse(data)
    if request.method == "POST":
        print(request.POST)
    # else:
    return HttpResponseNotFound()
# end course_dispatcher

##################################################################################################
# Serialization methods for classes
"""
This method sends back the serialized Course Model for parsing on the frontend
"""
def serializeCourse(request):
    if request.method == "POST":
        specificCourse = CourseCatalog.searchCoursesThroughPartialName(request.POST['course'])
        # specificCourse = specificCourse
        data = serializers.serialize("json", specificCourse)
        return HttpResponse(data)
    else:
        # We should make a public API with this stuff....
        # For now, I guess we'll redirect.
        return HttpResponseRedirect('/')
    pass

"""
This method sends back a dictionary with ALL serialized subcourse objects (Lecture/Lab/Tutorials) of a given Course
"""
def serializeSubCourseItems(request):
    # TODO: CHECK AGAINST A 'semester' PARAMATER SUPPLIED IN COURSE.
    # TODO: REfactor and use   CourseCatalog.seralizeCourseForSemester(specificcourse, semester):
    if request.method == "POST":
        print(request.POST)
        # 1. Get the Course
        specificCourse = CourseCatalog.searchCoursesThroughPartialName(request.POST['course'])
        specificCourse = specificCourse[0]
        # 2. Get its subcourse items
        # NOTE: small hack here, we ask Django to neatly serialize the models before
        courses_lectures = serializers.serialize("json", specificCourse.allLectures())
        courses_tutorials = serializers.serialize("json", specificCourse.allTutorials())
        courses_labs = serializers.serialize("json", specificCourse.allLabs())

        # 3. Build a Dictionary and send it off!
        full_course_data = {}
        full_course_data = { 'deptnum': specificCourse.deptnum }
        full_course_data["lectures"] = courses_lectures
        full_course_data["tutorials"] = courses_tutorials
        full_course_data["labs"] = courses_labs
        # NOTE: we serialize everything again to complete the response package.
        data = json.dumps(full_course_data)

        print(full_course_data)
        return HttpResponse(data)
    else:
        # We should make a public API with this stuff....
        # For now, I guess we'll redirect.
        return HttpResponseRedirect('/')
    pass

def serializeCourseCompletely(request):
    pass



##################################################################################################
# Dev methods to test features and not break flow


def work_in_progress(request):
    html = "<html><body>The website template you requested is currently being worked on</body></html>"
    return HttpResponse(html)

@csrf_exempt
def nullhandler(request):
    # This method does nothing other than print out the stuff it is receiving
    print(request.build_absolute_uri())
    if request.method == "POST":
        print(str(request.POST))

    html = "<html><body>Transaction Logged</body></html>"

    # for some in Course.objects.all():
    #     print(str(some.deptnum) + ":" + str(some.name))
    return HttpResponse(html)

