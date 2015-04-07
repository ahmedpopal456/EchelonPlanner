from django.test import TestCase
from ..database.coursecatalog import CourseCatalog as coursecatalog
from .schedulegenerator import ScheduleGenerator as schedGen
from .schedule import Schedule
from ..courses.course import Course as course
import django.db


class TestSchedule(TestCase):
    def setUp(self):
        self.myCourseCatalog = coursecatalog
        self.myCourseCatalog.addCourse("Test 1", 428, "COEN", 3.5)
        self.myCourseCatalog.addLectureToCourse("T", "COEN", 428, "11:45:00", "13:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.addTutorialToCourse("TA", "COEN", 428, "Fall", "17:45:00", "19:00:00", "M------", "SGW H-454", "T")
        self.myCourseCatalog.addLabToCourse("TM", "COEN", 428,  "8:45:00", "10:00:00", "M------", "Fall", "SGW H-821", "T", "TA")
        self.myCourseCatalog.addCourse("Test 2", 341, "COEN", 3)
        self.myCourseCatalog.addLectureToCourse("V", "COEN", 341, "13:45:00", "15:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.addTutorialToCourse("VI", "COEN", 341, "Fall", "11:00:00", "12:15:00", "-T-----", "SGW H-401", "V")
        self.myCourseCatalog.addLabToCourse("VM", "COEN", 341, "17:45:00", "19:00:00", "---R---", "Fall", "SGW H-821", "V", "VI")
        self.myCourseCatalog.addLabToCourse("VN", "COEN", 341, "17:45:00", "19:00:00", "---R---", "Fall", "SGW H-821", "V", "VI")
        self.myCourseCatalog.addTutorialToCourse("VJ", "COEN", 341, "Fall", "10:15:00", "11:30:00", "--W----", "SGW H-401", "V")
        self.myCourseCatalog.addLabToCourse("VO", "COEN", 341, "8:45:00", "10:00:00", "M------", "Fall", "SGW H-821", "V", "VJ")
        self.myCourseCatalog.addLabToCourse("VP", "COEN", 341, "8:45:00", "10:00:00", "---R---", "Fall", "SGW H-821", "V", "VJ")
        self.myCourseCatalog.addLectureToCourse("T", "COEN", 341, "13:45:00", "15:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.addTutorialToCourse("TI", "COEN", 341, "Fall", "11:00:00", "12:15:00", "-T-----", "SGW H-401", "T")
        self.myCourseCatalog.addLabToCourse("TM", "COEN", 341, "17:45:00", "19:00:00", "---R---", "Fall", "SGW H-821", "T", "TI")
        self.myCourseCatalog.addLabToCourse("TN", "COEN", 341, "17:45:00", "19:00:00", "---R---", "Fall", "SGW H-821", "T", "TI")
        self.myCourseCatalog.addTutorialToCourse("TJ", "COEN", 341, "Fall", "10:15:00", "11:30:00", "--W----", "SGW H-401", "T")
        self.myCourseCatalog.addLabToCourse("TO", "COEN", 341, "8:45:00", "10:00:00", "M------", "Fall", "SGW H-821", "T", "TJ")
        self.myCourseCatalog.addLabToCourse("TP", "COEN", 341, "8:45:00", "10:00:00", "---R---", "Fall", "SGW H-821", "T", "TJ")

    def tearDown(self):
        self.myCourseCatalog.removeCourseWithSections("COEN", 428)
        self.myCourseCatalog.removeCourseWithSections("COEN", 341)

    def test_addCourse_removeItem_lecture(self):
        """
            Tests that a lecture is added to schedule and then removed
        """
        myLecture = self.myCourseCatalog.searchCoursesThroughPartialName("COEN428")[0].lecture_set.all()[0]
        mySchedule = Schedule()
        mySchedule.add_item(myLecture)
        coursesInMySchedule = mySchedule.view_schedule()
        TestCase.assertIn(self, myLecture, coursesInMySchedule, "The course was not added to the schedule")
        mySchedule.remove_item(myLecture)
        coursesInMySchedule = mySchedule.view_schedule()
        TestCase.assertEqual(self, len(coursesInMySchedule), 0, "The course was not removed from the schedule")

    def test_addCourse_removeItem_tutorial(self):
        """
            Tests that a tutorial and its lecture are added to schedule
            and then removed
        """
        myLecture = self.myCourseCatalog.searchCoursesThroughPartialName("COEN428")[0].lecture_set.all()[0]
        myTutorial = self.myCourseCatalog.searchCoursesThroughPartialName("COEN428")[0].tutorial_set.all()[0]
        mySchedule = Schedule()
        mySchedule.add_item(myTutorial)
        coursesInMySchedule = mySchedule.view_schedule()
        TestCase.assertIn(self, myTutorial, coursesInMySchedule, "The course was not added to the schedule")
        TestCase.assertIn(self, myLecture, coursesInMySchedule, "The course was not added to the schedule")
        mySchedule.remove_item(myTutorial)
        coursesInMySchedule = mySchedule.view_schedule()
        TestCase.assertEqual(self, len(coursesInMySchedule), 0, "The course was not removed from the schedule")

    def test_addCourse_removeItem_lab(self):
        """
            Tests that a lab and its accompanying tutorial and
            lecture are added to schedule and then removed
        """
        myLecture = self.myCourseCatalog.searchCoursesThroughPartialName("COEN428")[0].lecture_set.all()[0]
        myTutorial = self.myCourseCatalog.searchCoursesThroughPartialName("COEN428")[0].tutorial_set.all()[0]
        myLab = self.myCourseCatalog.searchCoursesThroughPartialName("COEN428")[0].lab_set.all()[0]
        mySchedule = Schedule()
        mySchedule.add_item(myLab)
        coursesInMySchedule = mySchedule.view_schedule()
        TestCase.assertIn(self, myLab, coursesInMySchedule, "The course was not added to the schedule")
        TestCase.assertIn(self, myTutorial, coursesInMySchedule, "The course was not added to the schedule")
        TestCase.assertIn(self, myLecture, coursesInMySchedule, "The course was not added to the schedule")
        mySchedule.remove_item(myLab)
        coursesInMySchedule = mySchedule.view_schedule()
        TestCase.assertEqual(self, len(coursesInMySchedule), 0, "The course was not removed from the schedule")

if __name__ == '__main__':
    TestCase.main()