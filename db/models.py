from db import db_handler

class Base:
    @classmethod
    def select(cls, username):
        obj = db_handler.select_data(cls, username)
        return obj

    def save(self):
        db_handler.save_data(self)


class Admin(Base):
    def __init__(self,user,pwd):
        self.user = user
        self.pwd = pwd

    def create_school(self,school_name,school_addr):
        school_obj = School(school_name,school_addr)
        school_obj.save()


    def create_course(self,school_obj,course_name):
        course_obj = Course(course_name)
        course_obj.save()

        school_obj.course_list.append(course_name)

        school_obj.save()


    def create_teacher(self,teacher_name,teacher_pwd):
        teacher_obj = Teacher(teacher_name,teacher_pwd)
        teacher_obj.save()



class School(Base):
    def __init__(self,name,addr):
        self.user = name
        self.addr = addr

        self.course_list = []


class Student(Base):
    def __init__(self,username,pwd):
        self.user = username
        self.pwd = pwd
        self.school = None
        self.course_list = []
        self.score_dict = {}

    def add_school(self,school_name):
        self.school = school_name
        self.save()

    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.score_dict[course_name] = 0
        self.save()
        course_obj = Course.select(course_name)
        course_obj.student_list.append(self.user)
        course_obj.save()


class Course(Base):
    def __init__(self,course_name):
        self.user = course_name
        self.student_list = []


class Teacher(Base):
    def __init__(self,teacher_name,teacher_pwd):
        self.user = teacher_name
        self.pwd = teacher_pwd
        self.course_list_from_teacher = []

    def add_course(self,course_name):
        self.course_list_from_teacher.append(course_name)
        self.save()

    def show_course(self):
        return self.course_list_from_teacher

    def get_student(self,course_name):
        course_obj = Course.select(course_name)
        return course_obj.student_list

    def change_score(self,course_name,student_name,score):
        student_obj = Student.select(student_name)
        student_obj.score_dict[course_name] = score
        student_obj.save()






