from django.test import TestCase
from ..database.coursecatalog import CourseCatalog
from .course import Course


class TestCourses(TestCase):
    def setUp(self):
        # Add a course with at least one lab and tutorial
        CourseCatalog.addCourse("Testy1", 357, "COMP", 3)
        CourseCatalog.addLectureToCourse("A", "COMP", 357, "10:00", "11:00", "--W-F--", "Winter", "SGW FG2.70", False)
        CourseCatalog.addTutorialToCourse("AB", "COMP", 357, "Winter", "15:00", "16:00", "M------", "SGW H 909", "A")
        CourseCatalog.addLabToCourse("AC", "COMP", 357, "16:00", "18:00", "-T-----", "Winter", "SGW H 567", "A", "AB")
        CourseCatalog.addLectureToCourse("V", "COMP", 357, "10:00", "11:00", "--W-F--", "Fall", "SGW FG2.70", False)
        CourseCatalog.addTutorialToCourse("VB", "COMP", 357, "Fall", "15:00", "16:00", "M------", "SGW H 909", "V")
        CourseCatalog.addLabToCourse("VC", "COMP", 357, "16:00", "18:00", "-T-----", "Fall", "SGW H 567", "V", "VB")
        # Add a course without a lab and tutorial
        CourseCatalog.addCourse("Testy2", 753, "COMP", 3)

    def tearDown(self):
        CourseCatalog.removeCourseWithSections("COMP", 357)
        CourseCatalog.removeCourseWithSections("COMP", 753)

    def test_hasTutorials(self):
        """
            Test verifies that courses with at least one tutorial
            return true when hasTutorials is called, and false otherwise.
        """
        c1 = CourseCatalog.searchCoursesThroughPartialName("Testy1")[0]
        c2 = CourseCatalog.searchCoursesThroughPartialName("Testy2")[0]
        TestCase.assertTrue(self, c1.hasTutorials(), "A course with tutorial returns that it does not have any.")
        TestCase.assertFalse(self, c2.hasTutorials(), "A course without tutorial returns that it does have.")

    def test_hasLabs(self):
        """
            Test verifies that courses with at least one lab
            return true when hasLabs is called, and false otherwise.
        """
        c1 = CourseCatalog.searchCoursesThroughPartialName("Testy1")[0]
        c2 = CourseCatalog.searchCoursesThroughPartialName("Testy2")[0]
        TestCase.assertTrue(self, c1.hasLabs(), "A course with lab returns that it does not have any.")
        TestCase.assertFalse(self, c2.hasLabs(), "A course without lab returns that it does have.")

    def test_allLectures(self):
        """
            Test verifies that all lectures are returned
            when allLectures is called.
        """
        c = CourseCatalog.searchCoursesThroughPartialName("Testy1")[0]
        TestCase.assertEqual(self, len(c.allLectures()), 2, "Not all the lectures were returned")

    def test_allLectures_givenSemester(self):
        """
            Test verifies that all lectures are returned for a given
            semester when allLectures is called with a semester
        """
        c = CourseCatalog.searchCoursesThroughPartialName("Testy1")[0]
        TestCase.assertEqual(self, len(c.allLectures("Fall")), 1, "The correct amount of lectures were not returned")

    def test_allTutorials(self):
        """
            Test verifies that all tutorials are returned
            when allTutorials is called.
        """
        c = CourseCatalog.searchCoursesThroughPartialName("Testy1")[0]
        TestCase.assertEqual(self, len(c.allTutorials()), 2, "Not all the tutorials were returned")

    def test_allTutorials_givenSemester(self):
        """
            Test verifies that all tutorials are returned for a given
            semester when allTutorials is called with a semester
        """
        c = CourseCatalog.searchCoursesThroughPartialName("Testy1")[0]
        TestCase.assertEqual(self, len(c.allTutorials("Fall")), 1, "The correct amount of lectures were not returned")

    def test_allLabs(self):
        """
            Test verifies that all labs are returned
            when allLabs is called.
        """
        c = CourseCatalog.searchCoursesThroughPartialName("Testy1")[0]
        TestCase.assertEqual(self, len(c.allLabs()), 2, "Not all the lectures were returned")

    def test_allLabs_givenSemester(self):
        """
            Test verifies that all labs are returned for a given
            semester when allLabs is called with a semester
        """
        c = CourseCatalog.searchCoursesThroughPartialName("Testy1")[0]
        TestCase.assertEqual(self, len(c.allLabs("Fall")), 1, "The correct amount of lectures were not returned")

if __name__ == '__main__':
    TestCase.main()