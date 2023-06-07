# 时间    @2023/6/5 21:34
# 作者    @Wwf
import os


class StuDent_save:
    @staticmethod
    def student_save(student_list):
        """
        将学生信息保存到文件中
        :param student_list: 学生信息列表
        """
        filename = 'student1.txt'
        if not os.path.exists(filename):  # 如果文件不存在，则创建文件
            with open(filename, 'w', encoding='UTF-8') as f:
                f.write('')

        with open(filename, 'w', encoding='UTF-8') as f:  # 打开文件，并将学生信息写入文件
            for student in student_list:
                f.write(str(student).replace('"', '') + '\n')
