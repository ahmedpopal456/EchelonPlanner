from django.test import TestCase
from .coursecatalog import CourseCatalog as coursecatalog
from ..courses.course import Course as course
from ..courses.lecture import Lecture
from ..courses.lab import Lab
from ..courses.tutorial import Tutorial
from ..event.event import Event
import django.db


class TestDatabases(TestCase):
    """
        Test class for Databases (courses and users)
    """

    def setUp(self):
        """
            Setup adds 3 set courses to the course
            catalog database
        """
        self.myCourseCatalog = coursecatalog()
        self.myCourseCatalog.addCourse("Test 0", 341, "COMP", 3)
        self.myCourseCatalog.addCourse("Test 1", 342, "SOEN", 3.5)
        self.myCourseCatalog.addCourse("Test 2", 341, "SOEN", 4)

    def tearDown(self):
        """
            teardown removes the 3 courses from the
            course catalog database
        """
        self.myCourseCatalog.removeCourse("COMP", 341)
        self.myCourseCatalog.removeCourse("SOEN", 342)
        self.myCourseCatalog.removeCourse("SOEN", 341)

    def test_getCourseBasedOnNumber(self):
        """
            Test adds 3 courses, and retrieves only the 2
            with course number 341
        """
        myRetrievedCourses = self.myCourseCatalog.searchCourses("341")
        courses = []
        for c in myRetrievedCourses:
            courses.append(c.name)
        TestCase.assertEqual(self, 2, len(myRetrievedCourses), "The correct amount of courses was not retrieved")
        TestCase.assertIn(self, "Test 2", courses, "The  course was not retrieved from the database")
        TestCase.assertIn(self, "Test 0", courses, "The  course was not retrieved from the database")

    def test_getCourseBasedOnName(self):
        """
            Test adds 3 courses, and retrieves only the 1
            with course name Test 2
        """
        myRetrievedCourses = self.myCourseCatalog.searchCourses("Test 1")
        TestCase.assertEqual(self, 1, len(myRetrievedCourses), "The correct amount of courses was not retrieved")
        TestCase.assertEqual(self, "Test 1", myRetrievedCourses[0].name, "The course was not retrieved from the database")

    def test_getCourseBasedOnDepartment(self):
        """
            Test adds 3 courses, and retrieves only the 2
            with department SOEN
        """
        myRetrievedCourses = self.myCourseCatalog.searchCourses("SOEN")
        courses = []
        for c in myRetrievedCourses:
            courses.append(c.name)
        TestCase.assertEqual(self, 2, len(myRetrievedCourses), "The correct amount of courses was not retrieved")
        TestCase.assertIn(self, "Test 1", courses, "The  course was not retrieved from the database")
        TestCase.assertIn(self, "Test 2", courses, "The  course was not retrieved from the database")

    def test_getCourseBasedOnPartialNumber(self):
        """
            Test adds 3 courses, and retrieves the 3 with
            course number or name containing 1
        """
        myRetrievedCourses = self.myCourseCatalog.searchCourses("1")
        courses = []
        for c in myRetrievedCourses:
            courses.append(c.name)
        TestCase.assertEqual(self, 3, len(myRetrievedCourses), "The correct amount of courses was not retrieved")
        TestCase.assertIn(self, "Test 0", courses, "The  course was not retrieved from the database")
        TestCase.assertIn(self, "Test 1", courses, "The  course was not retrieved from the database")
        TestCase.assertIn(self, "Test 2", courses, "The  course was not retrieved from the database")

    def test_getCourseBasedOnPartialName(self):
        """
            Test adds 3 courses, and retrieves the 3 with
            name that contains "est"
        """
        myRetrievedCourses = self.myCourseCatalog.searchCourses("est")
        courses = []
        for c in myRetrievedCourses:
            courses.append(c.name)
        TestCase.assertEqual(self, 3, len(myRetrievedCourses), "The correct amount of courses was not retrieved")
        TestCase.assertIn(self, "Test 0", courses, "The  course was not retrieved from the database")
        TestCase.assertIn(self, "Test 1", courses, "The  course was not retrieved from the database")
        TestCase.assertIn(self, "Test 2", courses, "The  course was not retrieved from the database")

    def test_getCourseBasedOnPartialDepartment(self):
        """
            Test adds 3 courses, and retrieves only the 2
            with partial department "EN"
        """
        myRetrievedCourses = self.myCourseCatalog.searchCourses("EN")
        courses = []
        for c in myRetrievedCourses:
            courses.append(c.name)
        TestCase.assertEqual(self, 2, len(myRetrievedCourses), "The correct amount of courses was not retrieved")
        TestCase.assertIn(self, "Test 1", courses, "The  course was not retrieved from the database")
        TestCase.assertIn(self, "Test 2", courses, "The  course was not retrieved from the database")

    def test_getCourseBasedOnCredits(self):
        """
            Test adds 3 courses, and retrieves only the 1
            with 3.5 credits
        """
        myRetrievedCourses = self.myCourseCatalog.searchCoursesByCredits(3.5, 3.5)
        TestCase.assertEqual(self, 1, len(myRetrievedCourses), "The correct amount of courses was not retrieved")
        TestCase.assertEqual(self, "Test 1", myRetrievedCourses[0].name, "The course was not retrieved from the database")

    def test_getCourseBasedOnCreditRange(self):
        """
            Test adds 3 courses, and retrieves only the 2
            courses with 3 to 3.5 credits
        """
        myRetrievedCourses = self.myCourseCatalog.searchCoursesByCredits(3, 3.5)
        courses = []
        for c in myRetrievedCourses:
            courses.append(c.name)
        TestCase.assertEqual(self, 2, len(myRetrievedCourses), "The correct amount of courses was not retrieved")
        TestCase.assertIn(self, "Test 0", courses, "The  course was not retrieved from the database")
        TestCase.assertIn(self, "Test 1", courses, "The  course was not retrieved from the database")

    def test_getCourseBasedOnCredits_CourseNotExists(self):
        """
            Test adds 3 courses, and attempts to retrieve a
            course with les than 2 credits, which none of
            the courses have.
        """
        myRetrievedCourses = self.myCourseCatalog.searchCoursesByCredits(0, 2)
        TestCase.assertEqual(self, 0, len(myRetrievedCourses), "The correct amount of courses was not retrieved")

    def test_getCourses_courseNotExists(self):
        """
            Test adds 3 courses, and retrieves none, since
            none match the criteria
        """
        myRetrievedCourses = self.myCourseCatalog.searchCourses("z")
        TestCase.assertEqual(self, 0, len(myRetrievedCourses), "The correct amount of courses was not retrieved")

    def test_addCourse_courseAlreadyExists(self):
        """
            Test that addCourse does not insert a course
            that already exists into the database, but
            that the course remains in the database
        """
        myCourse = self.myCourseCatalog.searchCourses("SOEN 341")
        TestCase.assertEqual(self, len(myCourse), 1, "The course does not already exist")
        self.myCourseCatalog.addCourse("Test 2", 341, "SOEN", 3)
        myRetrievedCourse = self.myCourseCatalog.searchCourses("SOEN 341")
        TestCase.assertLess(self, len(myRetrievedCourse), 2, "The course was added twice")
        TestCase.assertGreater(self, len(myRetrievedCourse), 0, "The course was removed")
        TestCase.assertEqual(self, "Test 2", myRetrievedCourse[0].name, "The course was not added")
        # TODO rewrite this test now that searchCourses() has changed to not return duplicates

    def test_removeCourse(self):
        """
            Test that a course was added, and then removed
        """
        self.myCourseCatalog.addCourse("Test 4", 343, "SOEN", 3)
        myCourse = self.myCourseCatalog.searchCourses("SOEN 343")
        TestCase.assertEqual(self, len(myCourse), 1, "The course was not added")
        TestCase.assertEqual(self, "Test 4", myCourse[0].name, "The course was not added")
        self.myCourseCatalog.removeCourse("SOEN", 343)
        myRetrievedCourse = self.myCourseCatalog.searchCourses("SOEN 343")
        TestCase.assertEqual(self, len(myRetrievedCourse), 0, "The course was not removed")

    def test_removeCourse_courseNotExists(self):
        """
            Test tries to remove a course that does not exist,
            then makes sure that the other courses are not affected.
        """
        allCourses = self.myCourseCatalog.searchCourses(" ")
        TestCase.assertEqual(self, len(allCourses), 3, "There are not the correct amount of courses in the database")
        self.myCourseCatalog.removeCourse("COEN", 341)
        allCourses = self.myCourseCatalog.searchCourses(" ")
        TestCase.assertLess(self, len(allCourses), 4, "One or many courses have been added")
        TestCase.assertGreater(self, len(allCourses), 2, "One or many courses have been removed")

    def test_modifyCourseCredits(self):
        """
            Test modifies the number of credits a course
            that exists is worth
        """
        myCourse = self.myCourseCatalog.searchCoursesByCredits(4, 4)
        TestCase.assertEqual(self, myCourse[0].name, "Test 2", "The course does not have the expected number of credits")
        self.myCourseCatalog.modifyCredits("SOEN", 341, 5)
        myCourse = self.myCourseCatalog.searchCoursesByCredits(5, 5)
        TestCase.assertEqual(self, myCourse[0].name, "Test 2", "The course does not have the modified number of credits")

    def test_modifyCourseCredits_CourseNotExist(self):
        """
            Test attempts to modify the number of credits
            a course that does not exist, and then verifies
            that the course still does not exist
        """
        myCourse = self.myCourseCatalog.searchCourses("COEN 341")
        TestCase.assertEqual(self, len(myCourse), 0, "The course exists already")
        self.myCourseCatalog.modifyCredits("COEN", 341, 5)
        myCourse = self.myCourseCatalog.searchCourses("COEN 341")
        TestCase.assertEqual(self, len(myCourse), 0, "The course has been added from an attempt to modify credits")

    def test_AddLecture(self):
        """
            Test attempts to add a lecture to a course
            and verifies that it is found in the database.
        """
        TestCase.assertTrue(self, self.myCourseCatalog.addLectureToCourse(
            "A", "SOEN", 341, "8:45:00", "10:00:00", "--W-F--", "Fall", "SGW H-620", False),
                            "Lecture not successfully added to course")
        TestCase.assertEqual(self, len(self.myCourseCatalog.searchCourses("SOEN341")[0].lecture_set.all()), 1, "Lecture not successfully added to database")

    def test_AddLecture_CourseNotExists(self):
        """
            Test attempts to add a lecture to a course that
            doesn't exist and verifies that it is not found
            in the database.
        """
        TestCase.assertFalse(self, self.myCourseCatalog.addLectureToCourse(
            "A", "COEN", 341, "8:45:00", "10:00:00", "--W-F--", "Fall", "SGW H-620", False),
                            "Lecture successfully added to a course that does not exist")
        TestCase.assertEqual(self, len(self.myCourseCatalog.searchCourses("COEN341")), 0, "Course has been added to database")

    def test_removeLecture(self):
        """
            Test adds a lecture to an existing course, verifies
            that it is there, and then removes it, and verifies
            that it is not there.
        """
        self.test_AddLecture()
        TestCase.assertTrue(self, self.myCourseCatalog.removeLecture("A", "SOEN", 341, "Fall"), "The lecture was not successfully removed")
        TestCase.assertEqual(self, len(self.myCourseCatalog.searchCourses("SOEN341")[0].lecture_set.all()), 0, "The lecture was not successfully removed")

    def test_removeLecture_noLectureExists(self):
        """
            Test attempts to remove a non-existing lecture
            from a course and verifies that it is not there.
        """
        TestCase.assertFalse(self, self.myCourseCatalog.removeLecture("A", "SOEN", 341, "Fall"), "The non-existant lecture was successfully removed")
        TestCase.assertEqual(self, len(self.myCourseCatalog.searchCourses("SOEN341")[0].lecture_set.all()), 0, "The lecture was created and not removed")

    def test_AddTutorial(self):
        """
            Test attempts to add a tutorial to a lecture and
            verifies that it is found in the database.
        """
        self.test_AddLecture()
        TestCase.assertTrue(self, self.myCourseCatalog.tutorialToCourse(
            "AI", "SOEN", 341, "Fall", "8:45:00", "10:00:00", "---R---", "SGW H-620", "A"),
                            "Tutorial not successfully added to course")
        TestCase.assertEqual(self, len(self.myCourseCatalog.searchCourses("SOEN341")[0].tutorial_set.all()), 1, "Tutorial not successfully added to lecture")

    def test_AddTutorial_CourseNotExists(self):
        """
            Test attempts to add a tutorial to a course that
            doesn't exist and verifies that it is not found
            in the database.
        """
        TestCase.assertFalse(self, self.myCourseCatalog.tutorialToCourse(
            "AI", "COEN", 341, "Fall", "8:45:00", "10:00:00", "--W-F--", "SGW H-620", "A"),
                            "Tutorial successfully added to a course that does not exist")
        TestCase.assertEqual(self, len(self.myCourseCatalog.searchCourses("COEN341")), 0, "Course has been added to database")

    def test_removeTutorial(self):
        """
            Test adds a lecture to a course, and then a tutorial
            to that lecture, and then verifies that it is in the
            database, and then removes it and verifies that it is
            no long in the database
        """
        self.test_AddTutorial()
        TestCase.assertTrue(self, self.myCourseCatalog.removeTutorial("AI", "SOEN", 341, "Fall"), "Tutorial removal not successful")
        TestCase.assertEqual(self, len(self.myCourseCatalog.searchCourses("SOEN341")[0].tutorial_set.all()), 0, "Tutorial not removed from course")

    def test_AddLab(self):
        """
            Test attempts to add a lab to a course and verifies
            that it is found in the database.
        """
        self.test_AddTutorial()
        self.myCourseCatalog.labToCourse("AM", "SOEN", 341, "8:45:00", "10:00:00", "-T-----", "Fall", "SGW H-620", "A", "AI")
        TestCase.assertEqual(self, len(self.myCourseCatalog.searchCourses("SOEN341")[0].lab_set.all()), 1, "Lab not successfully added to database")
        TestCase.assertEqual(self, len(self.myCourseCatalog.searchCourses("SOEN341")[0].tutorial_set.all()[0].lab_set.all()), 1, "Lab not successfully added to tutorial")

    def test_AddLab_CourseNotExists(self):
        """
            Test attempts to add a lab to a course that doesn't
            exist and verifies that it is not found in the database.
        """
        self.myCourseCatalog.labToCourse("AM", "COEN", 341, "8:45:00", "10:00:00", "--W-F--", "Fall", "SGW H-620", "A", "AI")
        TestCase.assertEqual(self, len(self.myCourseCatalog.searchCourses("COEN341")), 0, "Course has been added to database")

    def test_removeLab(self):
        """
            Test adds a lecture to a course, and then a tutorial
            to that lecture, then a lab to that tutorial, and then
            verifies that it is in the database, and then removes
            it and verifies that it is no long in the database.
        """
        self.test_AddLab()
        TestCase.assertTrue(self, self.myCourseCatalog.removeLab("AM", "SOEN", 341, "Fall"), "Lab removal not successful")
        TestCase.assertEqual(self, len(self.myCourseCatalog.searchCourses("SOEN341")[0].lab_set.all()), 0, "Lab not removed from course")
        TestCase.assertEqual(self, len(self.myCourseCatalog.searchCourses("SOEN341")[0].tutorial_set.all()[0].lab_set.all()), 0, "Lab not removed from tutorial")

    # def test_getProfessor(self):
    #     a = 1
    #     # get professor
    #     # ensure that the correct professor is retrieved
    #
    # def test_getProfessor_profNotExists(self):
    #     a = 1
    #     # get professor
    #     # ensure that nothing happens
    #
    # def test_enrollStudent(self):
    #     a = 1
    #     # enroll student
    #     # try to fetch them from the db
    #
    # def test_enrollStudent_studentAlreadyExists(self):
    #     a = 1
    #     # enroll student
    #     # nothing happens, i.e. student with same ID still exists as it did before
    #     # try to fetch them from the db
    #
    # def test_removeStudent(self):
    #     a = 1
    #     # remove an enrolled student
    #
    # def test_removeStudent_studentNotExists(self):
    #     a = 1
    #     # remove student
    #     # ensure that nothing happens

if __name__ == '__main__':
    TestCase.main()