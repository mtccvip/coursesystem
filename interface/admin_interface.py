from db import models

def admin_register_interface(username,password):
    admin_obj = models.Admin.select(username)
    if admin_obj:
        return False,'用户名已存在'


    admin_obj = models.Admin(username,password)

    admin_obj.save()

    return True,'注册成功'


def admin_login_interface(username,password):
    admin_obj = models.Admin.select(username)
    if not admin_obj:
        return False,'用户名不存在'

    if password == admin_obj.pwd:
        return True,'登录成功'
    else:
        return False,'用户名或密码错误'


def create_school_interface(school_name,school_addr,admin_name):
    school_obj = models.School.select(school_name)
    if school_obj:
        return False,'学校已存在'

    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_school(school_name,school_addr)
    return True,f'{school_name}创建成功'

def create_course_interface(school_name,course_name,admin_name):
    school_obj = models.School.select(school_name)
    if course_name in school_obj.course_list:
        return False,'当前课程已存在'

    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(school_obj,course_name)


    return True,f'{course_name}课程创建成功,绑定给{school_name}'

def create_teacher_interface(teacher_name,admin_name,teacher_pwd = '123'):
    teacher_obj = models.Teacher.select(teacher_name)

    if teacher_obj:
        return False,'老师已经存在'

    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name,teacher_pwd)

    return True,f'{teacher_name}创建成功'


















