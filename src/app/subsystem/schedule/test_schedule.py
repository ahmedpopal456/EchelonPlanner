from django.test import TestCase
from ..database.coursecatalog import CourseCatalog as coursecatalog
from .schedulegenerator import ScheduleGenerator as schedGen
from ..courses.course import Course as course
import django.db


class TestSchedule(TestCase):
    def setUp(self):
        self.myCourseCatalog = coursecatalog()
        self.schedGen = schedGen()

    def remove2CreatedCourses(self):
        """
            Deletes the created courses from the database so that they can be
            recreated for other tests
        """
        self.myCourseCatalog.removeCourse("COMP", 428)
        self.myCourseCatalog.removeCourse("SOEN", 341)

    def test_doDaysConflict_noConflict(self):
        """
            Verifies that 2 non-conflicting course days passed into the method
            doDaysConflict() returns false
        """
        days_1 = "--W-F--"
        days_2 = "-T-R---"
        TestCase.assertFalse(self, self.schedGen.doDaysConflict(days_1, days_2), "An unexpected conflict was detected")

    def test_doDaysConflict_oneConflict(self):
        """
            Verifies that 2 conflicting course days with 1 day in common passed
            into the method doDaysConflict() returns true
        """
        days_1 = "-T--F--"
        days_2 = "-T-R---"
        TestCase.assertTrue(self, schedGen.doDaysConflict(days_1, days_2), "An expected conflict was not detected")

    def test_doDaysConflict_twoConflicts(self):
        """
            Verifies that 2 conflicting course days with 2 days in common passed
            into the method doDaysConflict() returns true
        """
        days_1 = "-T-R---"
        days_2 = "-T-R---"
        TestCase.assertTrue(self, schedGen.doDaysConflict(days_1, days_2), "An expected conflict was not detected")

    def test_doTimesConflict_noConflict(self):
        """
            Verifies that for two sections that whose times don't conflict,
            doTimesConflict() returns false
        """
        # Create a course with a lecture from 11:45am to 1:00pm
        self.myCourseCatalog.addCourse("Test 1", 428, "COMP", 3.5)
        self.myCourseCatalog.addLectureToCourse("T", "COMP", 428, "11:45:00", "13:00:00", "--W-F--", "Fall", "SGW H-401", False)
        c1 = course.objects.get(pk="COMP428")
        sections_1 = c1.lecture_set.all()
        section1 = sections_1[0]

        # Create a second course with a tutorial from 1:15pm to 2:30pm
        self.myCourseCatalog.addCourse("Test 2", 341, "SOEN", 3)
        self.myCourseCatalog.addLectureToCourse("V", "SOEN", 341, "8:45:00", "10:00:00", "M-W----", "Fall", "SGW H-945", False)
        self.myCourseCatalog.tutorialToCourse("VI", "SOEN", 341, "Fall", "13:15:00", "14:30:00", "--W-F--", "SGW H-401", "V")
        c2 = course.objects.get(pk="SOEN341")
        sections_2 = c2.tutorial_set.all()
        section2 = sections_2[0]

        # Verify that doTimesConflict() returns false (i.e. that the times do not conflict)
        TestCase.assertFalse(self, schedGen.doTimesConflict(section1, section2), "Times conflict that should not")

        self.remove2CreatedCourses()

    def test_doTimesConflict_conflictFully(self):
        """
            Verifies that for two sections that whose times conflict fully,
            doTimesConflict() returns true
        """
        # Create a course with a lecture from 11:45am to 1:00pm
        self.myCourseCatalog.addCourse("Test 1", 428, "COMP", 3.5)
        self.myCourseCatalog.addLectureToCourse("T", "COMP", 428, "11:45:00", "13:00:00", "--W-F--", "Fall", "SGW H-401", False)
        c1 = course.objects.get(pk="COMP428")
        sections_1 = c1.lecture_set.all()
        section1 = sections_1[0]

        # Create a second course with a tutorial from 11:45am to 1:00pm
        self.myCourseCatalog.addCourse("Test 2", 341, "SOEN", 3)
        self.myCourseCatalog.addLectureToCourse("V", "SOEN", 341, "8:45:00", "10:00:00", "M-W----", "Fall", "SGW H-945", False)
        self.myCourseCatalog.tutorialToCourse("VI", "SOEN", 341, "Fall", "11:45:00", "13:00:00", "--W-F--", "SGW H-401", "V")
        c2 = course.objects.get(pk="SOEN341")
        sections_2 = c2.tutorial_set.all()
        section2 = sections_2[0]

        # Verify that doTimesConflict() returns true (i.e. that the times conflict)
        TestCase.assertTrue(self, schedGen.doTimesConflict(section1, section2), "Times do not conflict that should")

        self.remove2CreatedCourses()

    def test_doTimesConflict_conflictPartially(self):
        """
            Verifies that for two sections that whose times conflict partially,
            doTimesConflict() returns true
        """
        # Create a course with a lecture from 11:45am to 1:00pm
        self.myCourseCatalog.addCourse("Test 1", 428, "COMP", 3.5)
        self.myCourseCatalog.addLectureToCourse("T", "COMP", 428, "11:45:00", "13:00:00", "--W-F--", "Fall", "SGW H-401", False)
        c1 = course.objects.get(pk="COMP428")
        sections_1 = c1.lecture_set.all()
        section1 = sections_1[0]

        # Create a second course with a tutorial from 12:45pm to 2:00pm
        self.myCourseCatalog.addCourse("Test 2", 341, "SOEN", 3)
        self.myCourseCatalog.addLectureToCourse("V", "SOEN", 341, "8:45:00", "10:00:00", "M-W----", "Fall", "SGW H-945", False)
        self.myCourseCatalog.tutorialToCourse("VI", "SOEN", 341, "Fall", "12:45:00", "14:00:00", "--W-F--", "SGW H-401", "V")
        c2 = course.objects.get(pk="SOEN341")
        sections_2 = c2.tutorial_set.all()
        section2 = sections_2[0]

        # Verify that doTimesConflict() returns true (i.e. that the times conflict)
        TestCase.assertTrue(self, schedGen.doTimesConflict(section1, section2), "Times do not conflict that should")

        self.remove2CreatedCourses()

    def test_findUnconflictingSections_justLectures_noConflict(self):
        """
            Verifies that for a course with just 1 lecture section and no tutorials
            or labs and another course with just 1 lecture section with no tutorials
            or labs the lecture section of the second course is returned when passed
            through findUnconflictingSections()
        """
        # Create a course with a lecture
        self.myCourseCatalog.addCourse("Test 1", 428, "COMP", 3.5)
        self.myCourseCatalog.addLectureToCourse("T", "COMP", 428, "11:45:00", "13:00:00", "--W-F--", "Fall", "SGW H-401", False)
        c1 = course.objects.get(pk="COMP428")
        sections_1 = c1.lecture_set.all()
        section1 = sections_1[0]

        # Create a second course with a lecture that does not conflict with course 1
        self.myCourseCatalog.addCourse("Test 2", 341, "SOEN", 3)
        self.myCourseCatalog.addLectureToCourse("V", "SOEN", 341, "13:45:00", "15:00:00", "--W-F--", "Fall", "SGW H-401", False)
        c2 = course.objects.get(pk="SOEN341")
        sections_2 = c2.lecture_set.all()
        section2 = sections_2[0]

        unconflictingSections = self.schedGen.findUnconflictingSections(section1, "SOEN341")

        TestCase.assertEquals(self, len(unconflictingSections), 1, "The unconflicting section was not found")
        TestCase.assertEquals(self, unconflictingSections[0], section2, "The unconflicting section was not found")
        self.remove2CreatedCourses()

    def test_findUnconflictingSections_justLectures_Conflict(self):
        """
            Verifies that for a course with just 1 lecture section and no tutorials or
            labs and another course with just 1 lecture section with no tutorials or labs
            nothing is returned when passed through findUnconflictingSections()
        """
        # Create a course with a lecture
        self.myCourseCatalog.addCourse("Test 1", 428, "COMP", 3.5)
        self.myCourseCatalog.addLectureToCourse("T", "COMP", 428, "11:45:00", "13:00:00", "--W-F--", "Fall", "SGW H-401", False)
        c1 = course.objects.get(pk="COMP428")
        sections_1 = c1.lecture_set.all()
        section1 = sections_1[0]

        # Create a second course with a lecture that conflicts with the lecture of course 1
        self.myCourseCatalog.addCourse("Test 2", 341, "SOEN", 3)
        self.myCourseCatalog.addLectureToCourse("V", "SOEN", 341, "12:45:00", "14:00:00", "--W-F--", "Fall", "SGW H-401", False)

        unconflictingSections = schedGen.findUnconflictingSections(section1, "SOEN341")

        TestCase.assertEquals(self, len(unconflictingSections), 0, "The conflicting section was returned")
        self.remove2CreatedCourses()

    def test_findUnconflictingSections_bothHaveLectureAndTutorial_noConflict(self):
        """
            Verifies that for a course with just 1 lecture section and 1 tutorial section
            and no labs and another course with just 1 lecture section  and 1 tutorial
            section and no labs the tutorial section of the second course is returned when
            passed through findUnconflictingSections()
        """
        # Create a course with a lecture and a tutorial
        self.myCourseCatalog.addCourse("Test 1", 428, "COMP", 3.5)
        self.myCourseCatalog.addLectureToCourse("T", "COMP", 428, "11:45:00", "13:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.tutorialToCourse("TA", "COMP", 428, "Fall", "17:45:00", "19:00:00", "M------", "SGW H-454", "T")
        c1 = course.objects.get(pk="COMP428")
        sections_1 = c1.tutorial_set.all()
        section1 = sections_1[0]

        # Create a second course with a lecture and a tutorial, neither of which conflict with course 1
        self.myCourseCatalog.addCourse("Test 2", 341, "SOEN", 3)
        self.myCourseCatalog.addLectureToCourse("V", "SOEN", 341, "13:45:00", "15:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.tutorialToCourse("VI", "SOEN", 341, "Fall", "11:45:00", "13:00:00", "---R---", "SGW H-401", "V")
        c2 = course.objects.get(pk="SOEN341")
        sections_2 = c2.tutorial_set.all()
        section2 = sections_2[0]

        unconflictingSections = schedGen.findUnconflictingSections(section1, "SOEN341")

        TestCase.assertEquals(self, len(unconflictingSections), 1, "The unconflicting section was not found")
        TestCase.assertEquals(self, unconflictingSections[0], section2, "The unconflicting section was not found")

        self.remove2CreatedCourses()

    def test_findUnconflictingSections_bothHaveLectureAndTutorial_ConflictInLectures(self):
        """
            Verifies that for a course with just 1 lecture section and 1 tutorial section and
            no labs and another course with just 1 lecture section  and 1 tutorial section and
            no labs nothing is returned when passed through findUnconflictingSections()
        """
        # Create a course with a lecture and a tutorial
        self.myCourseCatalog.addCourse("Test 1", 428, "COMP", 3.5)
        self.myCourseCatalog.addLectureToCourse("T", "COMP", 428, "11:45:00", "13:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.tutorialToCourse("TA", "COMP", 428, "Fall", "17:45:00", "19:00:00", "M------", "SGW H-454", "T")
        c1 = course.objects.get(pk="COMP428")
        sections_1 = c1.tutorial_set.all()
        section1 = sections_1[0]

        # Create a second course with a lecture that conflicts with the previous course, and a tutorial
        self.myCourseCatalog.addCourse("Test 2", 341, "SOEN", 3)
        self.myCourseCatalog.addLectureToCourse("V", "SOEN", 341, "1:45:00", "14:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.tutorialToCourse("VI", "SOEN", 341, "Fall", "11:45:00", "13:00:00", "--W----", "SGW H-401", "V")

        unconflictingSections = schedGen.findUnconflictingSections(section1, "SOEN341")

        TestCase.assertEquals(self, len(unconflictingSections), 0, "The conflicting section was returned")

        self.remove2CreatedCourses()

    def test_findUnconflictingSections_bothHaveLectureAndTutorial_ConflictInTutorials(self):
        """
            Verifies that for a course with just 1 lecture section and 1 tutorial section and
            no labs and another course with just 1 lecture section  and 1 tutorial section and
            no labs nothing is returned when passed through findUnconflictingSections()
        """
        # Create a course with a lecture and a tutorial
        self.myCourseCatalog.addCourse("Test 1", 428, "COMP", 3.5)
        self.myCourseCatalog.addLectureToCourse("T", "COMP", 428, "11:45:00", "13:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.tutorialToCourse("TA", "COMP", 428, "Fall", "17:45:00", "19:00:00", "M------", "SGW H-454", "T")
        c1 = course.objects.get(pk="COMP428")
        sections_1 = c1.tutorial_set.all()
        section1 = sections_1[0]

        # Create a second course with a lecture and a tutorial that conflicts with the tutorial of course 1
        self.myCourseCatalog.addCourse("Test 2", 341, "SOEN", 3)
        self.myCourseCatalog.addLectureToCourse("V", "SOEN", 341, "13:45:00", "15:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.tutorialToCourse("VI", "SOEN", 341, "Fall", "15:45:00", "18:00:00", "M------", "SGW H-401", "V")

        unconflictingSections = schedGen.findUnconflictingSections(section1, "SOEN341")

        TestCase.assertEquals(self, len(unconflictingSections), 0, "The conflicting section was returned")

        self.remove2CreatedCourses()

    def test_findUnconflictingSections_bothHaveLectureAndTutorial_ConflictInTutorialLecture(self):
        """
            Verifies that for a course with just 1 lecture section and 1 tutorial section and
            no labs and another course with just 1 lecture section  and 1 tutorial section and
            no labs nothing is returned when passed through findUnconflictingSections()
        """
        # Create a course with a lecture and a tutorial
        self.myCourseCatalog.addCourse("Test 1", 428, "COMP", 3.5)
        self.myCourseCatalog.addLectureToCourse("T", "COMP", 428, "11:45:00", "13:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.tutorialToCourse("TA", "COMP", 428, "Fall", "17:45:00", "19:00:00", "M------", "SGW H-454", "T")
        c1 = course.objects.get(pk="COMP428")
        sections_1 = c1.tutorial_set.all()
        section1 = sections_1[0]

        # Create a second course with a lecture and a tutorial that conflicts with the lecture of course 1
        self.myCourseCatalog.addCourse("Test 2", 341, "SOEN", 3)
        self.myCourseCatalog.addLectureToCourse("V", "SOEN", 341, "13:45:00", "15:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.tutorialToCourse("VI", "SOEN", 341, "Fall", "11:00:00", "12:15:00", "--W----", "SGW H-401", "V")

        unconflictingSections = schedGen.findUnconflictingSections(section1, "SOEN341")

        TestCase.assertEquals(self, len(unconflictingSections), 0, "The conflicting section was returned")

        self.remove2CreatedCourses()

    def test_findUnconflictingSections_bothHaveLectureAndTutorials_ConflictInOneTutorialOnly(self):
        """
            Verifies that for a course with just 1 lecture section and 1 tutorial section and
            no labs and another course with just 1 lecture section  and 3 tutorial sections and
            no labs only 2 tutorial sections are returned when passed through
            findUnconflictingSections()
        """
        # Create a course with a lecture and a tutorial
        self.myCourseCatalog.addCourse("Test 1", 428, "COMP", 3.5)
        self.myCourseCatalog.addLectureToCourse("T", "COMP", 428, "11:45:00", "13:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.tutorialToCourse("TA", "COMP", 428, "Fall", "17:45:00", "19:00:00", "M------", "SGW H-454", "T")
        c1 = course.objects.get(pk="COMP428")
        sections_1 = c1.tutorial_set.all()
        section1 = sections_1[0]

        # Create a second course with a lecture and 3 tutorials, 1 tutorial that conflicts with the lecture of course 1
        self.myCourseCatalog.addCourse("Test 2", 341, "SOEN", 3)
        self.myCourseCatalog.addLectureToCourse("V", "SOEN", 341, "13:45:00", "15:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.tutorialToCourse("VI", "SOEN", 341, "Fall", "11:00:00", "12:15:00", "-T-----", "SGW H-401", "V")
        self.myCourseCatalog.tutorialToCourse("VJ", "SOEN", 341, "Fall", "11:00:00", "12:15:00", "--W----", "SGW H-401", "V")
        self.myCourseCatalog.tutorialToCourse("VK", "SOEN", 341, "Fall", "11:00:00", "12:15:00", "---R---", "SGW H-401", "V")
        c2 = course.objects.get(pk="SOEN341")
        sections_2 = c2.tutorial_set.all()
        unconflictingSection1 = sections_2.filter(event__tutorial__section = "VI")
        unconflictingSection2 = sections_2.filter(event__tutorial__section = "VK")

        unconflictingSections = schedGen.findUnconflictingSections(section1, "SOEN341")

        TestCase.assertGreater(self, len(unconflictingSections), 1, "One or more unconflicting sections were not returned")
        TestCase.assertLess(self, len(unconflictingSections), 3, "The conflicting section was returned")

        TestCase.assertIn(self, unconflictingSection1[0], unconflictingSections, "An unconflicting section is missing")
        TestCase.assertIn(self, unconflictingSection2[0], unconflictingSections, "An unconflicting section is missing")

        self.remove2CreatedCourses()

    def test_findUnconflictingSections_bothHaveLectureAndTutorialsAndLabs_ConflictInOneLabOnly(self):
        """
            Verifies that for a course with just 1 lecture section and 1 tutorial section and
            no labs and another course with just 1 lecture section  and 3 tutorial sections and
            no labs only 2 tutorial sections are returned when passed through
            findUnconflictingSections()
        """
        # Create a course with a lecture and a tutorial
        self.myCourseCatalog.addCourse("Test 1", 428, "COMP", 3.5)
        self.myCourseCatalog.addLectureToCourse("T", "COMP", 428, "11:45:00", "13:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.tutorialToCourse("TA", "COMP", 428, "Fall", "17:45:00", "19:00:00", "M------", "SGW H-454", "T")
        self.myCourseCatalog.labToCourse("TM", "COMP", 428,  "8:45:00", "10:00:00", "M------", "Fall", "SGW H-821", "T", "TA")
        c1 = course.objects.get(pk="COMP428")
        sections_1 = c1.lab_set.all()
        section1 = sections_1[0]

        # Create a second course with a lecture and a tutorial that conflicts with the lecture of course 1
        self.myCourseCatalog.addCourse("Test 2", 341, "SOEN", 3)
        self.myCourseCatalog.addLectureToCourse("V", "SOEN", 341, "13:45:00", "15:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.tutorialToCourse("VI", "SOEN", 341, "Fall", "11:00:00", "12:15:00", "-T-----", "SGW H-401", "V")
        self.myCourseCatalog.labToCourse("VM", "SOEN", 341, "17:45:00", "19:00:00", "---R---", "Fall", "SGW H-821", "V", "VI")
        self.myCourseCatalog.labToCourse("VN", "SOEN", 341, "17:45:00", "19:00:00", "---R---", "Fall", "SGW H-821", "V", "VI")
        self.myCourseCatalog.tutorialToCourse("VJ", "SOEN", 341, "Fall", "10:15:00", "11:30:00", "--W----", "SGW H-401", "V")
        self.myCourseCatalog.labToCourse("VO", "SOEN", 341, "8:45:00", "10:00:00", "M------", "Fall", "SGW H-821", "V", "VJ")
        self.myCourseCatalog.labToCourse("VP", "SOEN", 341, "8:45:00", "10:00:00", "---R---", "Fall", "SGW H-821", "V", "VJ")
        c2 = course.objects.get(pk="SOEN341")
        sections_2 = c2.lab_set.all()
        unconflictingSection1 = sections_2.filter(event__lab__section = "VM")
        unconflictingSection2 = sections_2.filter(event__lab__section = "VN")
        unconflictingSection3 = sections_2.filter(event__lab__section = "VP")

        unconflictingSections = schedGen.findUnconflictingSections(section1, "SOEN341")

        TestCase.assertGreater(self, len(unconflictingSections), 2, "One or more unconflicting sections were not returned")
        TestCase.assertLess(self, len(unconflictingSections), 4, "The conflicting section was returned")

        TestCase.assertIn(self, unconflictingSection1[0], unconflictingSections, "An unconflicting section is missing")
        TestCase.assertIn(self, unconflictingSection2[0], unconflictingSections, "An unconflicting section is missing")
        TestCase.assertIn(self, unconflictingSection3[0], unconflictingSections, "An unconflicting section is missing")

        self.remove2CreatedCourses()


# TODO: Continue making tests when functions become available:
#     def test_saveSchedule(self):
#         print("_")
#         # save schedule
#         # ensure that it is now in student's record and all course capacities have been decremented?
#
#     def test_saveSchedule_courseFull(self):
#         print("_")
#         # save schedule
#         # not enough capacity in a course error
#         # maybe test for in lecture, tutorial and lab separately
#
#     def test_generateSchedule_noPreferences(self):
#         print("_")
#         # generate schedule with no preferences selected
#
#     def test_generateSchedule_withPreferences(self):
#         print("_")
#         # generate schedule with some preferences
#
#     def test_generateSchedule_noPossibleSchedules(self):
#         print("_")
#         # try to generate a schedule with so many preferences that it is impossible

if __name__ == '__main__':
    TestCase.main()