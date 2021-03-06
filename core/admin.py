from interface import admin_interface
from interface import common_interface
from lib import common

admin_info = {'user':None}

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
    while True:
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        flag,msg =  admin_interface.admin_login_interface(username,password)
        if flag:
            print(msg)
            admin_info['user'] = username
            break
        else:
            print(msg)

@common.auth('admin')
def create_school():
    while True:
        school_name = input('请输入学校名称:').strip()
        school_addr = input('请输入学校地址:').strip()
        flag,msg = admin_interface.create_school_interface(school_name,school_addr,admin_info.get('user'))
        if flag:
            print(msg)
            break
        else:
            print(msg)

@common.auth('admin')
def create_course():
    while True:
        flag,school_list_msg = common_interface.get_all_school_interface()
        if not flag:
            print(school_list_msg)
            break
        for index,school_name in enumerate(school_list_msg):
            print(f'编号:{index} 学校名称:{school_name}')

        choice = input('请输入学校编号：').strip()
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)

        if choice not in range(len(school_list_msg)):
            print('请输入正确编号')
            continue
        school_name = school_list_msg[choice]
        course_name = input('请输入需要创建的课程名称：').strip()

        flag,msg = admin_interface.create_course_interface(school_name,course_name,admin_info.get('user'))

        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.auth('admin')
def create_teacher():
    while True:
        teacher_name = input('请输入老师的名字:').strip()
        flag,msg = admin_interface.create_teacher_interface(teacher_name,admin_info.get('user'))
        if flag:
            print(msg)
            break
        else:
            print(msg)





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



