import os
import sys
from conf import settings
from db import models


def get_all_school_interface():
    school_dir  = os.path.join(settings.DB_PATH,'School')

    if not os.path.exists(school_dir):
        return False,'学校不存在,请先联系管理员'

    school_list = os.listdir(school_dir)
    return True,school_list


def login_interface(user,pwd,user_type):
    obj = None
    if user_type == 'admin':
        obj = models.Admin.select(user)

    elif user_type == 'student':
        obj = models.Student.select(user)

    elif user_type == 'teacher':
        obj = models.Teacher.select(user)

    else:
        return False,'登录角色不对'

    if obj:

        if pwd == obj.pwd:
            return True,'登录成功'
        else:
            return False,'密码错误'
    else:
        return False,'用户名不存在'

def get_course_in_school_interface(school_name):
    school_obj = models.School.select(school_name)
    course_list = school_obj.course_list

    if course_list:
        return True,course_list
    else:
        return False,'该学校没有课程'