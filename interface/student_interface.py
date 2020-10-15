from db import models

def student_register_interface(user,pwd):
    student_obj = models.Student.select(user)
    if student_obj:
        return False,'学生已存在'
    student_obj = models.Student(user,pwd)
    student_obj.save()
    return True,'学生注册成功'


def student_login_interface(user,pwd):
    student_obj = models.Student.select(user)
    if not student_obj:
        return False,'用户不存在'
    if pwd == student_obj.pwd:
        return True,'登录成功'
    else:
        return False,'密码错误'

def student_add_school_interface(school_name,user):
    student_obj = models.Student.select(user)
    if student_obj.school:
        return False,'当前学生已经绑定学校'

    student_obj.add_school(school_name)

    return True,'学生选择学校成功'

def get_course_list_interface(student_name):
    student_obj = models.Student.select(student_name)
    school_name = student_obj.school
    if not school_name:
        return False,'当前学生没有学校,请先选择学校'
    school_obj = models.School.select(school_name)
    course_list = school_obj.course_list
    if not course_list:
        return False,'当前学校没有课程,请先联系管理员创建'
    return True,course_list

def add_course_interface(student_name,course_name):
    #1.判断当前课程是否已经存在学生课程列表中
    student_obj = models.Student.select(student_name)
    if course_name in student_obj.course_list:
        return False,'该课程已经选择过了'
    student_obj.add_course(course_name)

    return True,'课程添加成功'

def check_score_interface(student_name):
    student_obj = models.Student.select(student_name)
    if  student_obj.score_dict:
        return student_obj.score_dict