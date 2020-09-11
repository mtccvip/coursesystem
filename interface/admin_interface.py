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