from db import models

def admin_register_interface(username,password):
    admin_obj = models.Admin.select(username)
    if admin_obj:
        return False,'用户名已存在'


    admin_obj = models.Admin(username,password)

    admin_obj.save()

    return True,'注册成功'