from django.test import TestCase


class TestSchedule(TestCase):
    def setUp(self):
        print("12")
        # setup

    def test_saveSchedule(self):
        print("13.1")
        # save schedule
        # ensure that it is now in student's record and all course capacities have been decremented?

    def test_saveSchedule_courseFull(self):
        print("13.2")
        # save schedule
        # not enough capacity in a course error
        # maybe test for in lecture, tutorial and lab separately

    def test_generateSchedule_noPreferences(self):
        print("14.1")
        # generate schedule with no preferences selected

    def test_generateSchedule_withPreferences(self):
        print("14.2")
        # generate schedule with some preferences

    def test_generateSchedule_noPossibleSchedules(self):
        print("14.3")
        # try to generate a schedule with so many preferences that it is impossible

if __name__ == '__main__':
    TestCase.main()