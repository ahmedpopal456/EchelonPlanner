import unittest


class TestDatabases(unittest.TestCase):
    def setUp(self):
        print("4")
        # setup

    def test_getCourses(self):
        print("5.1")
        # get course
        # ensure that the course retrieved is the right one

    def test_getCourses_courseNotExists(self):
        print("5.2")
        # get course
        # ensure that the course retrieved nothing

    def test_addCourse(self):
        print("6.1")
        # add the course
        # ensure that the course is in the db

    def test_addCourse_courseAlreadyExists(self):
        print("6.2")
        # add the course
        # ensure that the course is not added but is still in db

    def test_removeCourse(self):
        print("7.1")
        # remove the course
        # ensure that it is not in db nor in memory

    def test_removeCourse_courseNotExists(self):
        print("7.2")
        # remove the course
        # ensure that nothing happens

    def test_modifyCourseCapacity(self):
        print("8.1")
        # modify course capacity
        # get course from db
        # ensure that the course capacity is correct

    def test_modifyCourseCapacity_courseNotExists(self):
        print("8.2")
        # modify course capacity
        # ensure that nothing happens

    def test_getProfessor(self):
        print("9.1")
        # get professor
        # ensure that the correct professor is retrieved

    def test_getProfessor_profNotExists(self):
        print("9.2")
        # get professor
        # ensure that nothing happens

    def test_enrollStudent(self):
        print("10.1")
        # enroll student
        # try to fetch them from the db

    def test_enrollStudent_studentAlreadyExists(self):
        print("10.2")
        # enroll student
        # nothing happens, i.e. student with same ID still exists as it did before
        # try to fetch them from the db

    def test_removeStudent(self):
        print("11.1")
        # remove an enrolled student

    def test_removeStudent_studentNotExists(self):
        print("11.2")
        # remove student
        # ensure that nothing happens

if __name__ == '__main__':
    unittest.main()