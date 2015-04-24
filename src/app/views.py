import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest
from django.template import RequestContext
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db import IntegrityError, transaction
from django.contrib.auth import hashers
from django.contrib.sessions.backends.base import SessionBase
from .subsystem import *
import logging
import time
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import platform
import hashlib
from threading import Thread

# For Dev Purposes Only. This logger object can be identified as 'apps.view'
logger = logging.getLogger(__name__)

# Create your views here.

def index(request, hasheduser=""):
    return home(request, hasheduser)  # We'll have it hardcoded for now...


def help_site(request):
    return render(
        request,
        'app/help.html'
    )


@cache_control(no_cache=True, must_revalidate=True)
def home(request, hasheduser=""):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated():
        return menu(request)
    # else, then redirect
    return render(
        request,
        'app/login.html', {'hasheduser':hasheduser}
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
        username = request.POST['username']
        password = request.POST['password']
        if 'hasheduser' in request.POST:
            hasheduser = request.POST['hasheduser']
        else:
            hasheduser = str()

        user = authenticate(username=username, password=password)

        if user:
            # verify that the account has been confirmed by email
            if hasheduser == str(hashlib.sha256(user.email.encode()).hexdigest()):
                user.is_active = True
                user.save()
            # verify that the user has been confirmed
            if user.is_active:
                # If successful,
                login(request, user)
                if "remember-me" not in request.POST:
                    request.session.set_expiry(0) # Basically, close after the browser closes.
                return HttpResponseRedirect('/')  # This eliminates the login_handler from the path
            else:
                return render(request,
                              'app/login.html',
                              {'hasMessage': True, 'message': 'Login not successful. Please check your email for a confirmation message.'})
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
        # studentID = request.POST['idnum']  # No ID number provided

        if username == "":
            message.append("Please enter a valid username")

        if password1 == "" or password2 == "":
            message.append("Please fill in both password blocks")

        if firstname == "" or lastname == "":
            message.append("Please fully fill in your name and last name")

        if email == "" or '@' not in str(email):
            message.append("Please fill in the email address block")

        # if studentID is None or len(studentID) > 8 or len(studentID) < 7:
        #     message.append("The ID Number provided is invalid")

        if (password1 == password2) and (message == []):
            # Everything checks out and is all working fine :)
            # Create the Standard User first and try storing it in the database
            standardUser.set_password(password1)
            standardUser.username = username
            standardUser.email = email
            standardUser.first_name = firstname
            standardUser.last_name = lastname
            standardUser.is_active = False
            standardUser.is_staff = False
            standardUser.is_superuser = False
            try:
                standardUser.save()  # Save the Django user in the Database.
                # Now let's try putting that Student user in the DB
                studentUser.user = standardUser
                newRecord = StudentRecord()
                newRecord.save()
                studentUser.academicRecord = newRecord
                only_option = AcademicProgram.objects.get(pk=5)  # SOEN!
                # # We need to create and save a main schedule as well to the student
                studentUser.save()
                isregistered = True
                # send an email with an SSH hash of the user as a confirmation link:
                # since it will cause errors on Windows and most development is being done on windows,
                # first check that we are on Linux before attempting to send email.
                # Else, just register with no confirmation.
                if "inux" in platform.system() and False:
                    subject, from_email, to = 'Echelon Planner Confirmation', 'echelonplanner@gmail.com', str(standardUser.email)
                    hasheduser = str(hashlib.sha256(standardUser.email.encode()).hexdigest())
                    authLink = str(request.get_host()+"/confirm/" + hasheduser)
                    html_content = '<p>Please click on the following link to confirm your Echelon Planner account: </p><p><a href='+authLink+'>'+authLink+'</a></p>'
                    msg = EmailMultiAlternatives(subject, html_content, from_email, [standardUser.email])
                    msg.content_subtype = "html"
                    msg.send()
                else:
                    standardUser.is_active = True
                    standardUser.save()
            except IntegrityError as problem:
                # Student or auth_user was duplicate
                isregistered = False
                logger.warn(str(problem.args))
                message.append("User already Exists!")
        # end last If check

        if isregistered:
            if standardUser.is_active:
                return render(request,
                      'app/login.html',
                      {'hasMessage': True, 'message': ['Registration is successful.'], 'registered': isregistered})
            else:
                return render(request,
                      'app/login.html',
                      {'hasMessage': True, 'message': ['Registration is successful. Please check your email for a confirmation link before you login.'], 'registered': isregistered})

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

    if StudentCatalog.getStudent(mainProfile.username):
        specificProfile = StudentCatalog.getStudent(mainProfile.username)
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

@login_required()
def logouthandler(request):

    def cleanup():
        list_to_clean = serializers.deserialize('json', request.session['auto_schedules'])
        for oldSchedule in list_to_clean:
            oldSchedule.object.delete()

    # Cleanup any schedule objects associated to session!
    if 'auto_schedules' in request.session:
        thread = Thread(target=cleanup())
        thread.start()

    logout(request)
    return HttpResponseRedirect('/', {'hasMessage': True, 'message': 'Logout succesful. We hope to see you again!'})

@login_required
def concordia_resources(request):
    return render(
        request,
        'app/concordia_resources.html'
    )


def credits_page(request):
    return render(
        request,
        'app/credits.html'
    )


def about(request):
    return render(
        request,
        'app/about.html'
    )


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
        if len(request.POST['address']) > 0:
            request.user.student.address = address
        if len(request.POST['homePhone']) > 0:
            request.user.student.homephone = homePhone
        if len(request.POST['cellPhone']) > 0:
            request.user.student.cellphone = cellPhone
        request.user.student.save()
        return user_profile(request)

    else:
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
def student_record(request):
    firstname = request.user.first_name
    lastname = request.user.last_name
    this_student = StudentCatalog.getStudent(request.user.username)

    # If we didn't find the student, stop trying to render the page.
    if not this_student:
        return render(
            request,
            'app/student_record.html',
            {'firstname': firstname,
             'lastname': lastname}
        )
    # Else, we continue.

    # Start AJAX Handler
    if request.method == "POST":
        if 'action_type' in request.POST:
            if request.POST['action_type'] == 'undo_course':
                if 'deptnum' in request.POST:
                    request.user.student.academicRecord.removeTakenCourse(request.POST['deptnum'])
                    return HttpResponse(True)
            elif request.POST['action_type'] == 'remove_schedule':
                if 'schedulepk' in request.POST:
                    schedule_to_delete = Schedule.objects.filter(pk=request.POST['schedulepk'])
                    if schedule_to_delete:
                        schedule_to_delete[0].delete()
                        return HttpResponse(True)
                # Else, just return false
                return HttpResponse(False)
        else:
            return HttpResponseBadRequest("Malformed Request")

    this_record = this_student.academicRecord
    academicProgram = this_record.academicProgram
    gpa = this_record.GPA
    currentStanding = this_record.currentStanding
    currentCredits = this_record.currentCredits
    remainingCredits = this_record.remainingCredits
    coursesTaken = this_record.coursesTaken.all()
    allSchedules = this_record.scheduleCache.all()
    mainSchedule = this_record.mainSchedule
    return render(
        request,
        'app/student_record.html',
        {'firstname': firstname,
         'lastname': lastname,
         'academicProgram': academicProgram,
         'gpa': gpa,
         'currentStanding': currentStanding,
         'currentCredits': currentCredits,
         'remainingCredits': remainingCredits,
         'coursesTaken': coursesTaken,
         'scheduleCache': allSchedules,
         'mainSchedule': mainSchedule}
    )
# end student_record



@login_required
def schedule_view(request, specific='', render_type='normal', search_mode='recent'):
    # Hardcoded Timeslot Values (No reason to generate them anew each time)
    # These were generated by the following Bash command
    # for i in {7..20}:{00..59..15}; do completeList=$completeList","`echo \"$i\"`; done
    timeSlots=["08:30","08:45","09:00","09:15","09:30","09:45","10:00","10:15","10:30","10:45","11:00","11:15","11:30","11:45","12:00","12:15","12:30","12:45","13:00","13:15","13:30","13:45","14:00","14:15","14:30","14:45","15:00","15:15","15:30","15:45","16:00","16:15","16:30","16:45","17:00","17:15","17:30","17:45","18:00","18:15","18:30","18:45","19:00","19:15","19:30","19:45","20:00","20:15","20:30","20:45","21:00","21:15","21:30","21:45","22:00","22:15","22:30","22:45"]

    # Choose how to render
    render_template = 'app/schedule_view.html'
    if render_type == "basic":
        render_template = 'app/schedule_print_view.html'


    len(timeSlots)
    print(specific)

    if StudentCatalog.getStudent(request.user.username):
        # Case 1: There were auto_generated schedules and User is requesting one by pk
        if specific != "":
            specific = int(specific)
            specifiedSchedule = None

            # Select Search type
            # recently saved schedules
            if search_mode=="recent":
                schedule_data = []
                # Search current session
                if 'auto_schedules' in request.session:
                    # Start unpacking session data
                    schedule_data = serializers.deserialize('json',request.session['auto_schedules'])

            # Cached schedules in DB
            elif search_mode == "saved" and len(request.user.student.academicRecord.scheduleCache.all())>0:
                # Retrieve Schedule Cache list
                specifiedSchedule = request.user.student.academicRecord.scheduleCache.filter(pk=specific)
                if specifiedSchedule:
                    specifiedSchedule = specifiedSchedule[0]
                else:
                    specifiedSchedule = request.user.student.academicRecord.mainSchedule
            else:
                # Stop and return here if needed
                return schedule_view(request)

            if specifiedSchedule is None:
                return schedule_view(request)

            # Else, just keep going!

            viewing_table = specifiedSchedule.schedule_package()

        # Case 2: User is asking for the Main Schedule (Default)
        elif request.user.student.academicRecord.mainSchedule is not None:
            viewing_table = request.user.student.academicRecord.mainSchedule.schedule_package()
        # Case 3: No Schedules can be given to this user.
        else:
            viewing_table = {}
        print(viewing_table)
    else:
        viewing_table = {}

    # Final rendering details
    if specific=='':
        is_current = True
        year = 0
        semester =""
    else:
        is_current = False
        year = viewing_table.get('Year')
        semester = viewing_table.get('Semester')

    return render(
        request,
        render_template,
        {'timeSlots': timeSlots,
         'schedule': viewing_table,
         'is_current': is_current,
         'year': year,
         'semester': semester,
         'specific': specific,
         'search_mode':search_mode}
    )
# end schedule_view

@login_required
def schedule_check(request, mode="edit", specific=None):
    main_student = StudentCatalog.getStudent(request.user.username)
    schedule_return = []
    original_schedule = None
    year = str()
    semester = str()

    if mode == 'edit':
        site_to_return = 'app/schedule_check.html'
    elif mode == 'done':
        site_to_return = 'app/schedule_finish.html'
    else:
        return student_record(request)


    if main_student:
        specific = int(specific)
        # Search for the requested schedule
        record = main_student.academicRecord
        if record.mainSchedule:
            if record.mainSchedule.pk == specific:
                original_schedule = record.mainSchedule
                schedule_return = original_schedule.serializeScheduleForSemester()
        if record.scheduleCache and not schedule_return:
            schedule_return = record.scheduleCache.filter(pk=specific)
            if schedule_return:
                original_schedule = schedule_return[0]
                schedule_return = original_schedule.serializeScheduleForSemester()

        # AJAX/POST Handler
        if request.method == "POST" and original_schedule:
            print(request.POST)
            if 'action_type' in request.POST:
                if request.POST['action_type'] == 'remove':
                    if 'deptnum' in request.POST:
                        course_given = request.POST['deptnum']
                        original_schedule.remove_course(course_given)
                        return HttpResponse(True)
                    else:
                        return HttpResponseBadRequest("No Course Provided!")
                if request.POST['action_type'] == 'finished_semester':
                    passed_courses = request.POST.getlist('passed_courses')
                    for a_course in passed_courses:
                        request.user.student.academicRecord.passCourse(a_course)
                    if len(record.mainSchedule.lectureList.all()) > 0:
                        # Even if the list is not empty, forcibly pass to a new schedule.
                        record.mainSchedule = None
                        record.save()
                        record.moveScheduleFromCacheToMain()
                        record.save()

                    return HttpResponseRedirect(
                        "/student_record/",
                        {'message': "You're schedule courses have been added to the list of taken courses!"}
                    )
            else:
                return HttpResponseBadRequest("No Action for Schedule Editing Specified Or Bad Parameters for Action")
        # End AJAX/POST Handler

    if original_schedule:
        year = original_schedule.year
        semester = original_schedule.semester

    return render(
        request,
        site_to_return,
        {'schedule': schedule_return,
         'pk': specific,
         'mode': mode,
         'year': year,
         'semester': semester}
    )
# end schedule_check

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
        max_courses = [1, 2, 3, 4, 5, 6]
        # request.POST['semester'] # will return given semester!
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

        # Else, give them work in progress
        return work_in_progress(request)
    # end if request is POST

    # Phase 1: Ask for Semester.
    semesterCycle=["Summer1","Summer2", "Fall", "Winter"]
    max_years = list(range(1,6)) # from 1 to 5

    return render(
        request,
        'app/sched_gen_1.html',
        {'max_years': max_years,
         'semesterCycle': semesterCycle}
    )
#end sched_gen_1


@login_required()
def sched_gen_auto(request):

    max_courses = list(range(1,7))
    theStudent = StudentCatalog.getStudent(request.user.username)
    if theStudent:
        feasable_courses = CourseCatalog.coursesWithMetPrereqs(request.user.student, "Fall", 1)
    else:
        feasable_courses = []

    # If serving a POST request, it must be to consolidate schedules
    if request.method == "POST" and theStudent:

        # If the user did not submit anything, send him back the same page with a message
        given_courses = request.POST.getlist('courses')
        given_courses = list(set(given_courses))
        if "COURSE" in given_courses:
            given_courses.remove("COURSE")

        if not len(given_courses) > 0:  # No Courses Given, ERROR!
            return render(
                request,
                'app/schedule_generator_auto.html',
                {'max_courses': max_courses,
                 'feasable_courses': feasable_courses,
                 'currentYear': 1,
                 'currentSemester': "Fall",
                'message': "ERROR: Please Pick at least one course! (Repeating courses will be ignored automatically and you do not need to fill in all)"}
            )

        course_objects = []

        for specific_course in given_courses:  # Retrieve all the objects
            course = CourseCatalog.searchCoursesThroughPartialName(specific_course)
            if course:
                course = course[0]
                course_objects.append(course)

        semester = request.POST['semester']
        year = request.POST['year']

        # Parse from received preferences
        given_locations = request.POST.getlist('location')
        given_timesOfDay = request.POST.getlist('timeOfDay')
        given_daysOff = request.POST.getlist('daysOff')
        day_set = ['M','T','W','J','F','S','D']
        string_daysOff = ""

        for i in range(0,7):  # Check all the days!
            if day_set[i] in given_daysOff:
                string_daysOff += day_set[i]
            else:
                string_daysOff += "-"

        # Null out any unset/unreceived options to keep preferences consistent when building
        if len(given_locations) < 0:
            given_locations = None
        if len(given_timesOfDay) < 0:
            given_timesOfDay = None

        # Construct new preferences object and pass it on.
        default = Preferences(given_daysOff, given_timesOfDay, given_locations)

        # Make all the Schedules now.
        all_schedules = ScheduleGenerator.findListOfUnconflictingSectionsForOneSemester(course_objects,semester,default)
        # print(all_schedules)
        # print(len(all_schedules))

        if len(all_schedules) < 1:  # If no possible schedules, notify the user!
            feasable_courses = CourseCatalog.coursesWithMetPrereqs(request.user.student, semester, year)
            return render(
                request,
                'app/schedule_generator_auto.html',
                {'max_courses': max_courses,
                 'feasable_courses': feasable_courses,
                 'currentYear': year,
                 'currentSemester': semester,
                 'message': 'ERROR: No Schedule match was found. Try different courses or reduce your preferences.'}
            )

        # NOTE: Here comes the tricky part, we're storing the new schedules as serialized objects in the Session

        # Step 2: Take care of saving the newly generated ones.
        listOfSchedulesGenerated = []
        # I just profiled this segment. Guys, We have a bottleneck :/
        # My Fault for thinking we'd get away with an n^2 (Javier)
        start_time = time.time()

        # START BOTTLENECK #####################################
        @transaction.commit_manually
        def inner_saver():
            for aSchedule in all_schedules:
                cached_schedule = Schedule()
                cached_schedule.semester = semester
                cached_schedule.year = year
                cached_schedule.save()
                for anItem in aSchedule:
                    cached_schedule.add_item_unsafely(anItem)

                cached_schedule.save()
                listOfSchedulesGenerated.append(cached_schedule)

        # END BOTTLENECK ########################################
        inner_saver()
        end_time = time.time()
        print("Total Time Cost:"+str(end_time-start_time))

        # Step 3: If all was successful, let's save to session and redirect the user to view his schedule!
        request.user.student.previousSession = request.session.session_key
        request.user.student.academicRecord.save()
        request.user.student.save()
        final_data = serializers.serialize('json', listOfSchedulesGenerated)
        # if 'auto_schedules' in request.session:
        #     longstring = request.session['auto_schedules']
        #     if len(longstring) > 3:
        #         longstring = final_data[0:-1] + ", " + longstring[1:len(longstring)]
        #     else:
        #         longstring = final_data[1:len(final_data)]
        #     request.session['auto_schedules'] = longstring
        # else:
        request.session['auto_schedules'] = final_data
        request.session.modified = True
        return HttpResponseRedirect('/schedule_select/')

    # If just rendering the page.
    # TODO: calculate current year of student and current semester.
    else:
        return render(
            request,
            'app/schedule_generator_auto.html',
            {'max_courses': max_courses,
             'feasable_courses': feasable_courses,
             'currentYear': 1,
             'currentSemester': "Fall"}
        )
# end sched_gen_auto


@login_required
def schedule_select(request):
    # AJAX Handler
    if request.method == "POST":
        # Seems like request.POST is the PK of schedule
        schedulepk = 1
        mode = "cautious"

        if 'pk' in request.POST and 'mode' in request.POST:
            schedulepk = request.POST["pk"]
            mode = request.POST["mode"]
            schedulepk=int(schedulepk)
        else:
            return HttpResponseBadRequest("Malformed POST request Rejected.")

        scheduletosave = []
        # Check where the key came from to assure the safety of the request
        # Key came from the currently generated schedules?
        if 'auto_schedules' in request.session:
            session_schedules = serializers.deserialize('json', request.session['auto_schedules'])
            session_schedules = list(session_schedules)
            for scheduleObject in session_schedules:
                if scheduleObject.object.pk == schedulepk:
                    scheduletosave = Schedule.objects.filter(pk=schedulepk)
                    break
        # The Catch all case.
        if not scheduletosave:
            # Schedule not found OR PrimaryKey is not his (Security Issue), Return an Error
            return HttpResponseNotFound("No Schedule was found")

        scheduletosave = scheduletosave[0]
        schedyear = scheduletosave.year
        schedsemester = scheduletosave.semester
        scheduletoreplace = request.user.student.academicRecord.doesScheduleForSemesterYearExist(schedyear, schedsemester)

        if mode == "cautious":

            if scheduletoreplace:
                # Something exists need to send back confirmation
                return HttpResponse(False)

            else:
                request.user.student.academicRecord.scheduleCache.add(scheduletosave)
                # Call function to move to main if needed
                if request.user.student.academicRecord.mainSchedule is None:
                    request.user.student.academicRecord.moveScheduleFromCacheToMain()


                if 'auto_schedules' in request.session:
                    session_json = json.loads(request.session['auto_schedules'])

                    for i, sched in enumerate(session_json):
                        if sched['pk'] == schedulepk:
                            session_json.pop(i)
                            break
                    request.session['auto_schedules'] = json.dumps(session_json)


                return HttpResponse(True)

        elif mode == "assert":
            # Need to remove scheduletoreplace, and add scheduletosave
            try:
                request.user.student.academicRecord.removeSchedule(scheduletoreplace.year, scheduletoreplace.semester)
                request.user.student.academicRecord.scheduleCache.add(scheduletosave)
                # Call function to move to main if needed
                if request.user.student.academicRecord.mainSchedule is None:
                    request.user.student.academicRecord.moveScheduleFromCacheToMain()

                session_json = json.loads(request.session['auto_schedules'])

                for i, sched in enumerate(session_json):
                    if sched['pk'] == schedulepk:
                        session_json.pop(i)
                        break

                request.session['auto_schedules'] = json.dumps(session_json)
                return HttpResponse(True)
            except Schedule.DoesNotExist:
                return HttpResponse(False)
    # end AJAX Handler


    # Do a normal render
    else:
        schedule_data = []
        new_package = []
        start_time = time.time()
        # Unserialize whatever is in the users current session
        if 'auto_schedules' in request.session:
            schedule_data = serializers.deserialize('json', request.session['auto_schedules'])

        # Package all objects
        for item in schedule_data:
            new_package.append(item.object.serializeScheduleForSemester())

        end_time = time.time()
        print("Total Time in deserialization and packaging: "+str(end_time-start_time))
        return render(
            request,
            'app/schedule_select.html',
            { 'newSchedules': new_package,}
        )
# end schedule_select

@login_required
def course_create(request):
    if request.user.is_superuser or ProgramDirector.objects.filter(user_id=request.user.id):
        if request.method == 'POST':
            name = request.POST['name']
            number = request.POST['number']
            department = request.POST['department']
            # type = request.POST['type']
            credits = request.POST['credits']
            # prerequisites = request.POST['prerequisites']
            # equivalence = request.POST['equivalence']
            # yearSpan = request.POST['yearSpan']
            # newCourse = courses.Course.new()
            # newCourse.course.department = department
            # newCourse.course.type = type
            # newCourse.course.number = number
            # newCourse.course.credits = credits
            # newCourse.course.name = name
            # newCourse.save()
            # newCourse.course.prerequisites = prerequisites
            # newCourse.course.equivalence = equivalence
            # newCourse.course.yearSpan = yearSpan
            CourseCatalog.addCourse(name, number, department, credits)
            return render(
                request,
                'app/course_create.html',
                { 'hasmessage':True,
                  'message':"Course successfully added."}
            )
        return render(
            request,
            'app/course_create.html',
        )
    else:
        return render(
            request,
            'app/menu.html',
            { 'hasmessage':True,
              'message':"Warning: You do not have sufficient privileges to access this feature"}
        )
# end course_create

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

    return render(
        request,
        'app/browse_all_courses.html',
        {'courseList': courseList}  # Send it off to the template for rendering
    )
# end browse_all_courses


def browse_specific_course(request, deptnum=""):
    # AJAX Handler
    if request.method == "POST":
        if 'mode' in request.POST and StudentCatalog.getStudent(request.user):
            if request.POST['mode']=='previously_taken':
                request.user.student.academicRecord.addTakenCourse(deptnum)
                return HttpResponse(True)
            elif request.POST['mode'] == 'add_to_schedule':
                try:
                    coursetoadd = Course.objects.get(pk=deptnum)
                    if coursetoadd in request.user.student.academicRecord.coursesTaken.all():
                        return HttpResponse(False)
                except:
                    return HttpResponse(False)

                # There is no MainSchedule, so one needs to be made
                if not request.user.student.academicRecord.mainSchedule:
                    newMainSchedule = Schedule(year=1, semester="Fall")
                    newMainSchedule.save()
                    request.user.student.academicRecord.scheduleCache.add(newMainSchedule)
                    request.user.student.academicRecord.save()
                    request.user.student.academicRecord.moveScheduleFromCacheToMain()
                    request.user.student.academicRecord.save()

                if request.user.student.academicRecord.mainSchedule.add_first_available_section(deptnum):
                    return HttpResponse(True)
                else:
                    return HttpResponse(False)
                # TODO: put method tht can transfer a section of this deptnum into schedule. DONE

            else:
                return HttpResponseBadRequest("Request arguments were wrong.")
        else:
            return HttpResponseBadRequest("A malformed request was issued to the server. Check User and parameters.")
    # end AJAX Handling.

    # Normal Handler
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

@login_required()
def display_students(request):
    if request.user.is_superuser:
        users = []
        for user in User.objects.all():
            users.append(user)
        return render(
            request,
            'app/work_in_progress.html',
            {'users':users}
        )
    else:
        return render(
            request,
            'app/menu.html',
            { 'has message':True,
              'message':"Warning: You do not have sufficient privileges to access this feature."}
        )
    #TODO: Permissions message goes somewhere

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

def serializeCourseForSemester(request):
    if request.method == "POST":
        specific_course = CourseCatalog.searchCoursesThroughPartialName(request.POST['deptnum'])
        if len(specific_course) > 0:
            specific_course = specific_course[0]
            data = CourseCatalog.seralizeCourseForSemester(specific_course,request.POST['semester'])
            data = json.dumps(data)
            return HttpResponse(data)
    return HttpResponseRedirect('/')


# end serializeCourseForSemester



##################################################################################################
# Dev methods to test features and not break flow

def work_in_progress(request):
  return render(
        request,
        'app/work_in_progress.html'
    )

@csrf_exempt
def nullhandler(request):
    # This method does nothing other than print out the stuff it is receiving
    print(request.build_absolute_uri())
    if request.method == "POST":
        print(str(request.POST))

    if 'auto_schedules' in request.session:
        request.session['auto_schedules'] = ""
        testy = request.session['auto_schedules']
        print(testy)
        if len(testy) >0:
            data = serializers.deserialize('json',testy)
            for something in data:
                print(something.object.pk)
            print(data)
        # del request.session['auto_schedules']
        # request.session.modified = True
    else:
        print("No Auto Schedules!")

    if StudentCatalog.getStudent(request.user.username):
        prevSessionKey = request.user.student.previousSession
        if prevSessionKey is not None or prevSessionKey != "":  # There was a previous session
            # Find it!
            prevSession = Session.objects.filter(session_key=prevSessionKey)
            if len(prevSession) > 0:
                prevSession = prevSession[0].get_decoded()  # Previous Session is now the Dictionary of old Schedules
                serializedSchedules = prevSession['auto_schedules']
                print(serializedSchedules)
                scheduleObjects = serializers.deserialize('json', serializedSchedules)
                # Flush it out!
                for oldSchedule in scheduleObjects:
                    print(oldSchedule.object.pk)
        print(request.user.student.previousSession)


    print(request.session.session_key)
    print(request.get_host())

    html = "<html><body>Transaction Logged</body></html>"

    # for some in Course.objects.all():
    #     print(str(some.deptnum) + ":" + str(some.name))
    return HttpResponse(html)

