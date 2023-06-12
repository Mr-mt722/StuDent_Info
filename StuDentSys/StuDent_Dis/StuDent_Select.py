# 时间    @2023/6/12 21:35
# 作者    @Wwf
from StuDentSys.StuDent_Dis.StuDent_insert import StuDentInsert as insert
from StuDentSys.StuDent_Dis.StuDent_Read import StuDent_Read as read


class StuDent_Select:
    @classmethod
    def select_student(cls):
        students = read.read()
        while True:
            name = input('请输入你需要查找的学生姓名')
            for line2 in students:
                if name == line2['name']:
                    sid = line2['id']
                    sage = line2['age']
                    sgender = line2['gender']
                    print(f'你所查询的学生“{name}”，学号为：{sid}，性别：{sgender}，年龄：{sage}')
                    break
            else:
                answer = input('你所查询的学生信息不存在，是否新增？y/n：')
                if answer.upper() == 'Y':
                    insert.add_student()
                    students = read.read()
            answer = input('是否继续查询？y/n：')
            if answer.upper() == 'Y':
                continue
            else:
                break
