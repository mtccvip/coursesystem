from lib import common
from interface import student_interface
from interface import common_interface

student_info = {'user':None}


def register():
    while True:
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        re_password = input('请重复密码:').strip()

        if re_password == password:
            flag,msg = student_interface.student_register_interface(username,password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次输入的密码不一致，请重新输入')


def login():
    while True:
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        flag,msg = common_interface.login_interface(username,password,user_type='student')
        if flag:
            print(msg)
            student_info['user'] = username
            break
        else:
            print(msg)


@common.auth('student')
def choice_school():
    while True:
        flag,school_list_or_msg = common_interface.get_all_school_interface()
        if not flag:
            print(school_list_or_msg)
            break
        for index,school_name in enumerate(school_list_or_msg):
            print(f'编号：{index}, 学校名：{school_name}')

        choice = input('请输入学校编号:').strip()
        if not choice.isdigit():
            print('输入有误')
            continue
        choice = int(choice)

        if choice not in range(len(school_list_or_msg)):
            print('输入有误')
            continue

        school_name = school_list_or_msg[choice]
        flag,msg = student_interface.student_add_school_interface(school_name,student_info.get('user'))
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.auth('student')
def choice_course():
    while True:
        #1.获取当前学生所在学校的课程列表
        flag,course_list_or_msg = student_interface.get_course_list_interface(student_info.get('user'))
        if not flag:
            print(course_list_or_msg)
            break

        # 2.打印课程列表，供学生选择
        for index,course_name in enumerate(course_list_or_msg):
            print(f'编号：{index} 课程名：{course_name}')

        choice = input('请输入你的选择:').strip()
        if not choice.isdigit():
            print('输入有误')
            continue

        choice = int(choice)

        if choice not in range(len(course_list_or_msg)):
            print('编号输入有误')
            continue

        course_name = course_list_or_msg[choice]

        flag,msg = student_interface.add_course_interface(student_info.get('user'),course_name)

        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.auth('student')
def check_score():
    score_dict = student_interface.check_score_interface(student_info.get('user'))
    if not score_dict:
        print('没有选择课程')
    print(score_dict)



func_dic = {
    '1': register,
    '2': login,
    '3': choice_school,
    '4': choice_course,
    '5': check_score
}

def student_view():
    while True:
        print('''
        1.注册
        2.登录
        3.选择校区
        4.选择课程
        5.查看分数
        ''')
        choice = input('请输入你的选择：').strip()

        if choice == 'q':
            break

        if choice not in func_dic:
            print('请输入正确的选择')
            continue

        func_dic.get(choice)()