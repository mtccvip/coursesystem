from core import admin
from core import student
from core import teacher


fun_dic = {
    '1': admin.admin_view,
    '2': student.student_view,
    '3': teacher.teacher_view
}

def run():
    while True:
        print('''
        =========欢迎来到选课系统=========
                1.管理员功能
                2.学生功能
                3.老师功能
        ==============end==============
        ''')
        choice = input("请输入你的选择：").strip()

        if choice == 'q':
            break

        if choice not in fun_dic:
            print('请重新输入')
            continue


        fun_dic.get(choice)()





