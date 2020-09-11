from lib import common

teacher_info = {'user':None}

def login():
    pass

@common.auth('teacher')
def check_course():
    pass

@common.auth('teacher')
def choose_course():
    pass

@common.auth('teacher')
def check_stu_from_course():
    pass

@common.auth('teacher')
def change_score_from_student():
    pass


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

