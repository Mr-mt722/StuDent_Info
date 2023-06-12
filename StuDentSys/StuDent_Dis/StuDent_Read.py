# 时间    @2023/6/12 22:09
# 作者    @Wwf
class StuDent_Read:
    @classmethod
    def read(cls):
        infile = open('student1.txt', 'r', encoding='utf-8')
        students = []
        for line1 in infile:
            student = eval(line1.strip())
            students.append(student)
        infile.close()
        return students