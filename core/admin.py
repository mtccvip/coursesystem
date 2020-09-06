from interface import admin_interface

def register():
    while True:
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        re_password = input('请确认密码:').strip()

        if password == re_password:
            flag,msg = admin_interface.admin_register_interface(username,password)
            if flag:
                print('注册成功')
                break
            else:
                print('用户已存在,请重新输入')

        else:
            print('两次输入的密码不一致')
            continue

def login():
    pass

def create_school():
    pass

def create_course():
    pass

def create_teacher():
    pass

func_dic = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_course,
    '5': create_teacher
}


def admin_view():
    while True:
        print('''
        1.注册
        2.登录
        3.创建学校
        4.创建课程
        5.创建讲师
        '''
        )
        choice = input('请输入你的选择：').strip()

        if choice == 'q':
            break

        if choice not in func_dic:
            print('请输入正确的选择')
            continue


        func_dic.get(choice)()



