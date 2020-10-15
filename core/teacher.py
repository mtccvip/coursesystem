from lib import common
from interface import common_interface
from interface import teacher_interface

teacher_info = {'user':None}

def login():
    while True:
        username = input('请输入用户名:').strip()
        pwd = input('请输入密码:').strip()
        flag,msg = common_interface.login_interface(username,pwd,user_type='teacher')
        if flag:
            teacher_info['user'] = username
            print(msg)
            break
        else:
            print(msg)


@common.auth('teacher')
def check_course():
    flag,msg = teacher_interface.check_course_interface(teacher_info.get('user'))
    if flag:
        print(msg)
    else:
        print(msg)

@common.auth('teacher')
def choose_course():
    while True:
        #1.打印所有学校供选择
        flag,school_list_or_msg = common_interface.get_all_school_interface()
        if not flag:
            print(school_list_or_msg)
            break
        for index,school_name in enumerate(school_list_or_msg):
            print(f'编号{index},学校名称{school_name}')

        choice = input('请输入你的选择:').strip()
        if not choice.isdigit():
            print('输入有误')
            continue
        choice = int(choice)

        if choice not in range(len(school_list_or_msg)):
            print('输入的编号有误')
            continue

        school_name = school_list_or_msg[choice]

        flag2,course_list_or_msg = common_interface.get_course_in_school_interface(school_name)
        if not flag2:
            print(course_list_or_msg)
            break

        for index2,course_name in enumerate(course_list_or_msg):
            print(f'编号：{index} 课程名称：{course_name}')

        choice2 = input('请输入你的选择:').strip()
        if not choice2.isdigit():
            print('输入有误')
            continue

        choice2 = int(choice2)

        if choice2 not in range(len(course_list_or_msg)):
            print('输入有误')
            continue

        course_name = course_list_or_msg[choice2]

        flag3,msg3 = teacher_interface.add_course_interface(course_name,teacher_info.get('user'))

        if flag3:
            print(msg3)
            break
        else:
            print(msg3)


        #2.打印所选择的学校的所有课程供选择
        #3.将所选择的课程添加到老师课程列表中

@common.auth('teacher')
def check_stu_from_course():
    while True:
        #1.列出当前老师所有课程供老师选择
        flag,course_list_or_msg = teacher_interface.check_course_interface(teacher_info.get('user'))
        if not flag:
            print(course_list_or_msg)
            break

        for index,course_name in enumerate(course_list_or_msg):
            print(f'编号:{index} 课程名称:{course_name}')

        choice = input('请输入你的选择:').strip()

        if not choice.isdigit():
            print('输入有误')
            continue

        choice = int(choice)

        if choice not in range(len(course_list_or_msg)):
            print('输入有误')
            continue

        course_name = course_list_or_msg[choice]

        #2.列出选择的课程下所有学生
        flag,student_list_or_msg = teacher_interface.get_student_interface(course_name,teacher_info.get('user'))
        if flag:
            print(student_list_or_msg)
            break
        else:
            print(student_list_or_msg)



@common.auth('teacher')
def change_score_from_student():
    #1.列出老师所有教授课程供老师选择
    while True:
        flag,course_list_or_msg = teacher_interface.check_course_interface(teacher_info.get('user'))
        if not flag:
            print(course_list_or_msg)
            break
        for index,course_name in enumerate(course_list_or_msg):
            print(f'编号：{index} 课程名称：{course_name}')

        choice = input('请输入你的选择:').strip()
        if not choice.isdigit():
            print('输入有误')
            continue
        choice = int(choice)
        if choice not in range(len(course_list_or_msg)):
            print('输入有误')
            continue
        course_name = course_list_or_msg[choice]

    #2.列出所选择课程下所有学生供老师选择
        flag2,student_list_or_msg = teacher_interface.get_student_interface(course_name,teacher_info.get('user'))
        if not flag2:
            print(student_list_or_msg)
            break
        for index2,student_name in enumerate(student_list_or_msg):
            print(f'编号：{index2} 学生姓名：{student_name}')

        choice2 = input('请输入你的选择:').strip()
        if not choice2.isdigit():
            print('输入有误')
            continue
        choice2 = int(choice2)

        if choice2 not in range(len(student_list_or_msg)):
            print('输入有误')
            continue
        student_name = student_list_or_msg[choice2]

    #3.调用所选择的学生的分数修改接口
        score = input('请输入你的分数:').strip()
        if not score.isdigit():
            print('输入有误')
            continue
        score = int(score)

        flag3,msg = teacher_interface.change_score_interface(course_name,student_name,score,teacher_info.get('user'))

        if flag3:
            print(msg)
        else:
            print(msg)


fun_dic = {
    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_stu_from_course,
    '5': change_score_from_student

}

def teacher_view():
    while True:
        print('''
        1.登录
        2.查看教授课程
        3.选择教授课程
        4.查看课程下学生
        5.修改学生分数
        ''')
        choice = input('请输入你的选择：').strip()

        if choice == 'q':
            break

        if choice not in fun_dic:
            print('请输入正确的选择')
            continue

        fun_dic.get(choice)()

