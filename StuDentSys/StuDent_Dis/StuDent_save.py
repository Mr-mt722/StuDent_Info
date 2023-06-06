# 时间    @2023/6/5 21:34
# 作者    @Wwf
class StuDent_save():

    @classmethod
    def student_save(*cls):
        filename = 'student1.txt'
        if cls != '':
            try:
                stu_txt = open(filename, 'a', encoding='UTF-8')
            except:
                stu_txt = open(filename, 'w', encoding='UTF-8')
            for item in cls:
                if not isinstance(item, type) and item not None:
                    stu_txt.write(str(item) + '\n')

            stu_txt.close()
        else:
            print('数据为空，请重试')
