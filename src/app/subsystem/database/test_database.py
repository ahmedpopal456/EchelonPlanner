from django.test import TestCase
import app.subsystem.database.coursecatalog as coursecatalog
import app.subsystem.courses.course as course


class TestDatabases(TestCase):
    """
    Test class for Databases (courses and users)
    """

    def setUp(self):
        """
        Setup adds 3 set courses to the course catalog database
        """
        self.myCourseCatalog = coursecatalog.CourseCatalog
        self.myCourseCatalog.addCourse("Test 0", 341, "COMP", 3)
        self.myCourseCatalog.addCourse("Test 1", 342, "SOEN", 3.5)
        self.myCourseCatalog.addCourse("Test 2", 341, "SOEN", 4)

    def tearDown(self):
        """
        teardown removes the 3 courses from the course catalog database
        """
        self.myCourseCatalog.removeCourse("COMP", 341)
        self.myCourseCatalog.removeCourse("SOEN", 342)
        self.myCourseCatalog.removeCourse("SOEN", 341)

    def test_getCourseBasedOnNumber(self):
        """
        Test adds 3 courses, and retrieves only the 2 with course number 341
        """
        myRetrievedCourses = coursecatalog.CourseCatalog.searchCourses("341")
        courses = []
        for c in myRetrievedCourses:
            courses.append(c.name)
        TestCase.assertEqual(self, 2, len(myRetrievedCourses), "The correct amount of courses was not retrieved")
        TestCase.assertIn(self, "Test 2", courses, "The  course was not retrieved from the database")
        TestCase.assertIn(self, "Test 0", courses, "The  course was not retrieved from the database")

    def test_getCourseBasedOnName(self):
        """
        Test adds 3 courses, and retrieves only the 1 with course name Test 2
        """
        myRetrievedCourses = coursecatalog.CourseCatalog.searchCourses("Test 1")
        TestCase.assertEqual(self, 1, len(myRetrievedCourses), "The correct amount of courses was not retrieved")
        TestCase.assertEqual(self, "Test 1", myRetrievedCourses[0].name, "The course was not retrieved from the database")

    def test_getCourseBasedOnDepartment(self):
        """
        Test adds 3 courses, and retrieves only the 2 with department SOEN
        """
        myRetrievedCourses = coursecatalog.CourseCatalog.searchCourses("SOEN")
        courses = []
        for c in myRetrievedCourses:
            courses.append(c.name)
        TestCase.assertEqual(self, 2, len(myRetrievedCourses), "The correct amount of courses was not retrieved")
        TestCase.assertIn(self, "Test 1", courses, "The  course was not retrieved from the database")
        TestCase.assertIn(self, "Test 2", courses, "The  course was not retrieved from the database")

    def test_getCourseBasedOnPartialNumber(self):
        """
        Test adds 3 courses, and retrieves the 3 with course number or name containing 1
        """
        myRetrievedCourses = coursecatalog.CourseCatalog.searchCourses("1")
        courses = []
        for c in myRetrievedCourses:
            courses.append(c.name)
        TestCase.assertEqual(self, 3, len(myRetrievedCourses), "The correct amount of courses was not retrieved")
        TestCase.assertIn(self, "Test 0", courses, "The  course was not retrieved from the database")
        TestCase.assertIn(self, "Test 1", courses, "The  course was not retrieved from the database")
        TestCase.assertIn(self, "Test 2", courses, "The  course was not retrieved from the database")

    def test_getCourseBasedOnPartialName(self):
        """
        Test adds 3 courses, and retrieves the 3 with name that contains "est"
        """
        myRetrievedCourses = coursecatalog.CourseCatalog.searchCourses("est")
        courses = []
        for c in myRetrievedCourses:
            courses.append(c.name)
        TestCase.assertEqual(self, 3, len(myRetrievedCourses), "The correct amount of courses was not retrieved")
        TestCase.assertIn(self, "Test 0", courses, "The  course was not retrieved from the database")
        TestCase.assertIn(self, "Test 1", courses, "The  course was not retrieved from the database")
        TestCase.assertIn(self, "Test 2", courses, "The  course was not retrieved from the database")

    def test_getCourseBasedOnPartialDepartment(self):
        """
        Test adds 3 courses, and retrieves only the 2 with partial department "EN"
        """
        myRetrievedCourses = coursecatalog.CourseCatalog.searchCourses("EN")
        courses = []
        for c in myRetrievedCourses:
            courses.append(c.name)
        TestCase.assertEqual(self, 2, len(myRetrievedCourses), "The correct amount of courses was not retrieved")
        TestCase.assertIn(self, "Test 1", courses, "The  course was not retrieved from the database")
        TestCase.assertIn(self, "Test 2", courses, "The  course was not retrieved from the database")

    def test_getCourseBasedOnCredits(self):
        """
        Test adds 3 courses, and retrieves only the 1 with 3.5 credits
        """
        myRetrievedCourses = coursecatalog.CourseCatalog.searchCoursesByCredits(3.5, 3.5)
        TestCase.assertEqual(self, 1, len(myRetrievedCourses), "The correct amount of courses was not retrieved")
        TestCase.assertEqual(self, "Test 1", myRetrievedCourses[0].name, "The course was not retrieved from the database")

    def test_getCourses_courseNotExists(self):
        """
        Test adds 3 courses, and retrieves none, since none match the criteria
        """
        myRetrievedCourses = coursecatalog.CourseCatalog.searchCourses("z")
        TestCase.assertEqual(self, 0, len(myRetrievedCourses), "The correct amount of courses was not retrieved")

    def test_addCourse_courseAlreadyExists(self):
        """
        Test that addCourse does not insert a course that already exists into the database,
        but that the course remains in the database
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
        Test tries to remove a course that does not exist, then makes sure that the other
        courses are not affected.
        """
        allCourses = self.myCourseCatalog.searchCourses(" ")
        TestCase.assertEqual(self, len(allCourses), 3, "There are not the correct amount of courses in the database")
        self.myCourseCatalog.removeCourse("COEN", 341)
        allCourses = self.myCourseCatalog.searchCourses(" ")
        TestCase.assertLess(self, len(allCourses), 4, "One or many courses have been added")
        TestCase.assertGreater(self, len(allCourses), 2, "One or many courses have been removed")

    def test_modifyCourseCredits(self):
        """
        Test modifies the number of credits a course that exists is worth
        """
        myCourse = self.myCourseCatalog.searchCoursesByCredits(4, 4)
        TestCase.assertEqual(self, myCourse[0].name, "Test 2", "The course does not have the expected number of credits")
        self.myCourseCatalog.modifyCredits("SOEN", 341, 5)
        myCourse = self.myCourseCatalog.searchCoursesByCredits(5, 5)
        TestCase.assertEqual(self, myCourse[0].name, "Test 2", "The course does not have the modified number of credits")

    def test_modifyCourseCredits_CourseNotExist(self):
        """
        Test attempts to modify the number of credits a course that does not exist, and then
        verifies that the course still does not exist
        """
        myCourse = self.myCourseCatalog.searchCourses("COEN 341")
        TestCase.assertEqual(self, len(myCourse), 0, "The course exists already")
        self.myCourseCatalog.modifyCredits("COEN", 341, 5)
        myCourse = self.myCourseCatalog.searchCourses("COEN 341")
        TestCase.assertEqual(self, len(myCourse), 0, "The course has been added from an attempt to modify credits")

# TODO: search by credits not exists, search by credits limits, add and remove lecture (maybe using credits?)

    def test_getProfessor(self):
        a = 1
        # get professor
        # ensure that the correct professor is retrieved

    def test_getProfessor_profNotExists(self):
        a = 1
        # get professor
        # ensure that nothing happens

    def test_enrollStudent(self):
        a = 1
        # enroll student
        # try to fetch them from the db

    def test_enrollStudent_studentAlreadyExists(self):
        a = 1
        # enroll student
        # nothing happens, i.e. student with same ID still exists as it did before
        # try to fetch them from the db

    def test_removeStudent(self):
        a = 1
        # remove an enrolled student

    def test_removeStudent_studentNotExists(self):
        a = 1
        # remove student
        # ensure that nothing happens

if __name__ == '__main__':
    TestCase.main()