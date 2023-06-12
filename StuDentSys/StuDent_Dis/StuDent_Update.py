# 时间    @2023/6/12 20:44
# 作者    @Wwf
from StuDentSys.StuDent_Dis.StuDent_Show import StuDent_Show as show
from StuDentSys.StuDent_Dis.StuDent_Read import StuDent_Read as read

class StuDent_Update():
    @classmethod
    def update_student(cls):
        students = read.read()
        show.show_student()
        while True:
            # 修改特定学生信息
            target_id = ''
            target_id = input("请输入你需要修改的学生id")
            for student in students:
                name = student['name']
                if student['id'] == target_id:
                    student['name'] = input(f'学生本名”{name}“，请输入修改后的学生姓名：')
                    student['age'] = input(f'请输入修改后的学生姓年龄：')
                    student['gender'] = input(f'请输入修改后的学生性别：')
                    break
            answer = input('是否继续修改？y/n：')
            if answer.upper() == 'Y':
                continue
            else:
                break
            # 将所有学生信息重新写入文件中
        outfile = open("student1.txt", "w", encoding="utf-8")
        for student in students:
            outfile.write(str(student) + "\n")
        print('修改成功')
        outfile.close()
