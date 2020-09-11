from lib import common


student_info = {'user':None}


def register():
    pass

def login():
    pass

@common.auth('student')
def choice_school():
    pass

@common.auth('student')
def choice_course():
    pass

@common.auth('student')
def check_score():
    pass



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