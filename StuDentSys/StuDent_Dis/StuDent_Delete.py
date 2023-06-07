# 时间    @2023/6/1 20:57
# 作者    @Wwf
from StuDentSys.StuDent_Dis.StuDent_save import StuDent_save


class StuDent_Delete:
    @staticmethod
    def delete_student():
        """
        根据学生ID删除学生信息
        """
        student_list = []  # 创建一个空列表，用于保存所有的学生信息
        while True:
            student_id = input('请输入要删除的学生ID：')
            if not student_id.isdigit():
                print('ID必须是数字，请重新输入')
                continue
            with open('student1.txt', 'r', encoding='UTF-8') as f:  # 打开文件，并读取所有学生信息
                lines = f.readlines()
                if not lines:
                    print('没有学生信息，请先添加学生信息')
                    return
                for line in lines:
                    student = eval(line)  # 将字符串转换为字典
                    student_list.append(student)
            for student in student_list:
                if student['id'] == student_id:
                    student_list.remove(student)  # 从学生信息列表中删除指定的学生信息
                    print('学生信息删除成功！')
                    break
            else:
                print('没有找到该ID的学生信息，请重新输入')
                continue

            answer = input('是否继续删除？y/n：')
            if answer.upper() == 'Y':
                continue
            else:
                break

        StuDent_save.student_save(student_list)  # 将更新后的学生信息保存到文件中
