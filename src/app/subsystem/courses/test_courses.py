from django.test import TestCase
from ..database.coursecatalog import CourseCatalog
from .course import Course


class TestCourses(TestCase):
    def setUp(self):
        # Add a course with a lab and tutorial
        CourseCatalog.addCourse("Testy1", 357, "COMP", 3)
        CourseCatalog.addLectureToCourse("A", "COMP", 357, "10:00", "11:00", "--W-F--", "Winter", "SGW FG2.70", False)
        CourseCatalog.addTutorialToCourse("AB", "COMP", 357, "Winter", "15:00", "16:00", "M------", "SGW H 909", "A")
        CourseCatalog.addLabToCourse("AC", "COMP", 357, "16:00", "18:00", "-T-----", "Winter", "SGW H 567", "A", "AB")
        # Add a course without a lab and tutorial
        CourseCatalog.addCourse("Testy2", 753, "COMP", 3)

    def tearDown(self):
        CourseCatalog.removeCourseWithSections("COMP", 357)
        CourseCatalog.removeCourseWithSections("COMP", 753)

    def test_hasTutorials(self):
        c1 = CourseCatalog.searchCoursesThroughPartialName("Testy1")[0]
        c2 = CourseCatalog.searchCoursesThroughPartialName("Testy2")[0]
        TestCase.assertTrue(self, c1.hasTutorials(), "A course with tutorial returns that it does not have any.")
        TestCase.assertFalse(self, c2.hasTutorials(), "A course without tutorial returns that it does have.")

    def test_hasLabs(self):
        c1 = CourseCatalog.searchCoursesThroughPartialName("Testy1")[0]
        c2 = CourseCatalog.searchCoursesThroughPartialName("Testy2")[0]
        TestCase.assertTrue(self, c1.hasLabs(), "A course with lab returns that it does not have any.")
        TestCase.assertFalse(self, c2.hasLabs(), "A course without lab returns that it does have.")

if __name__ == '__main__':
    TestCase.main()