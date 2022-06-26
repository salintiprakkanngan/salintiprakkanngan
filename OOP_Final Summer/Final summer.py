"""
name: {Salinthip Rakkanngan}
id: {364211760050}
group: {MIT212}
"""


class Person:
    def __init__(self,name,email,tel):
        self.__name = name
        self.__email = email
        self.__tel = tel

    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_email(self):
        return self.__email
    def set_email(self,email):
        self.__email = email
    def get_tel(self):
        return self.__tel
    def set_tel(self,tel):
        self.__tel = tel


    def __str__(self):
        print(f'\tName: {self.__name}\n'
            f'\tEmail: {self.__email}\n'
            f'\tTel: {self.__tel}\n')


 class Student:
    def __init__(self, sid, major):
        self.__sid = sid
        self.__major = major

    def get_sid(self):
        return self.__sid
    def set_sid(self, sid):
        self.__sid = sid
    def get_major(self):
        return self.__major
    def set_major(self, major):
        self.__major = major


    def __str__(self):
        print(f'\tsid: {self.__sid}\n'
            f'\tmajor: {self.__major}\n'


class Employee:
    def __init__(self,eid,position):
        self.__eid = eid
        self.__position = position

    def get_eid(self):
        return self.__eid
    def set_eid(self,eid):
        self.__eid = eid
    def get_position(self):
        return self.__position
    def set_position(self,position):
        self.__position = position


    def __str__(self):
        print(f'\teid: {self.__eid}\n'
            f'\tposition: {self.__position}\n'


class Courses:
    def __init__(self, courses_id,courses_name):
        self.__courses_id = courses_id
        self.__courses_name = courses_name

    def get_courses_id(self):
        return self.__courses_id
    def set_courses_id(self, courses_id):
        self.__courses_id = courses_id
    def get_courses_name(self):
        return self.__courses_name
    def set_courses_name(self, courses_name):
        self.__courses_name = courses_name


    def __str__(self):
        print(f'\tcourses_id: {self.__courses_id}\n'
            f'\tcourses_name: {self.__courses_name}\n'


class CourseRegisteration:
    def id: student/employee(self):
        return __student/employee
    def course_regis: list(self, course_regis: list):
        self.__course_regis: list = course_regis: list

    def add_course(Course):
        return self.__courses


    def __str__(self):
        print(f'\tstudent/employee: {self.__student/employee}\n'
            f'\tcourse_regis: list: {self.__course_regis: list}\n'
            f'\tadd_course: {self.__course}\n'