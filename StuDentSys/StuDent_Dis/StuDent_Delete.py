# 时间    @2023/6/1 20:57
# 作者    @Wwf
import os
import json
from StuDentSys.StuDent_Dis.StuDent_Show  import StuDent_Show as show


class StuDent_Delete():
    @classmethod
    def student_delete(cls):

        while True:
            student_id = input('请输入你要删除的学生id')
            if student_id != '':
                # 检查文件是否存在
                if os.path.exists('student1.txt'):
                    # 读取学生信息
                    with open('student1.txt', 'r', encoding='UTF-8') as file:
                        # 将学生信息放到一个列表里
                        student_old = file.readlines()
                # 如果文件不存在则创建一个空列表
                else:
                    student_old = []
                flag = False  # 标记是否删除

                if student_old:
                    with open('student1.txt', 'w', encoding='UTF-8') as wfile:
                        d = {}
                        for item in student_old:
                            # 将字符串转化为字典
                            d = json.loads(item)
                            if d['id'] != student_id:
                                wfile.write(str(d) + '\n')
                            else:
                                flag = True
                        if flag:
                            print(f'id为{student_id}的学生信息已被删除')
                        else:
                            print(f'没有找到id为{student_id}的学生信息')
                else:
                    print('无此学生')
                    break
                show.student_show()  # 删除后重新显示所有学生信息
                answer = input('是否继续删除？y/n')
                if answer.upper() == 'Y':
                    continue
                else:
                    break
