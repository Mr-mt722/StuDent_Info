# 时间    @2023/6/5 21:34
# 作者    @Wwf
import os


class StuDentInsert:

    @staticmethod
    def add_student():
        student_new = []  # 创建一个空列表，用于保存新添加的学生信息
        while True:
            student = {}  # 创建一个空字典，用于保存一个学生的信息
            student['name'] = input('请输入学生姓名：')
            while True:
                student['age'] = input('请输入学生年龄：')
                if not student['age'].isdigit():
                    print('年龄必须是数字，请重新输入')
                    continue
                break
            student['gender'] = input('请输入学生性别：')
            while True:
                student['id'] = input('请输入学生ID：')
                if not student['id'].isdigit():
                    print('ID必须是数字，请重新输入')
                    continue
                if any(s['id'] == student['id'] for s in student_new):
                    print('该ID已经存在，请重新输入')
                    continue
                break
            student_new.append(student)  # 将学生信息添加到列表中
            answer = input('是否继续添加？y/n：')
            if answer.upper() == 'Y':
                continue
            else:
                break

        filename = 'student1.txt'
        if not os.path.exists(filename):  # 如果文件不存在，则创建文件
            with open(filename, 'w', encoding='UTF-8') as f:
                f.write('')

        with open(filename, 'a', encoding='UTF-8') as f:  # 打开文件，并将学生信息追加到文件末尾
            for student in student_new:
                f.write(str(student).replace('"', '') + '\n')

        print('学生信息添加成功！')
