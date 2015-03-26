from django.test import TestCase
import app.subsystem.database.coursecatalog as coursecatalog
import app.subsystem.courses.course as course
# import app.management.commands.populatedb as pop
import mysql.connector as mysql


class TestDatabases(TestCase):
    def setUp(self):
        print('Adding some courses to DB')
        # To test locally, put your user and passwd
        # conn = mysql.connect(host='localhost', user='????', passwd='????', db='test_echelon')
        conn = mysql.connect(host='bbbtimmy.noip.me', user='korra', passwd='SOEN341echelon!', db='test_echelon')
        cur = conn.cursor()
        cur.execute('SET GLOBAL FOREIGN_KEY_CHECKS=0')
        cur.execute('DROP TABLE IF EXISTS app_course ')
        cur.execute('SET GLOBAL FOREIGN_KEY_CHECKS=0')
        cur.execute('CREATE TABLE app_course (name VARCHAR(120), department VARCHAR(120), number INT, deptnum VARCHAR(120) PRIMARY KEY, type VARCHAR(120), credits FLOAT, yearSpan VARCHAR(120))')
        cur.execute('INSERT INTO app_course '
                    ' (name, department, number, deptnum, type, credits, yearSpan)'
                    ' VALUES ("Software Processes", "SOEN", 341, "SOEN341", NULL, 3, "14-15")')
        # setup

    def test_getCourses(self):
        print("Checking retrieval of courses")
        myRetrievedCourse = coursecatalog.CourseCatalog.searchCourses("341")
        TestCase.assertEqual(self, 1, len(myRetrievedCourse), "The course was not retrieved")
        # get course
        # ensure that the course retrieved is the right one

    def test_getCourses_courseNotExists(self):
        print("5.2")
        # get course
        # ensure that the course retrieved nothing

    def test_addCourse(self):
        print("6")
        # '''
        # Test that addCourse inserts a course into the DB
        # :return:
        # '''
        # coursecatalog.CourseCatalog.addCourse("Software Processes", 341, "SOEN", 3)
        # cur = self.conn.cursor()
        # addedCourse = cur.execute('SELECT * FROM app_courses')
        # TestCase.assertEqual(self, "Software Processes", addedCourse.getName(), "The course was not added")
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
    TestCase.main()