from django.test import TestCase


class TestCourses(TestCase):
    def setUp(self):
        print("1")
        # setup

    def test_AddStudent(self):
        print("2")
        # add the student
        # ensure that the student is in the db

    def test_RemoveStudent(self):
        print("3")
        # remove the student
        # ensure that the student is not in the db nor in memory

if __name__ == '__main__':
    TestCase.main()