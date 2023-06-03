# 时间    @2023/5/30 22:07
# 作者    @Wwf
def insert():
    # 创建一个学生列表
    student_list = []

    # 循环添加
    while True:
        id = input('请输入ID（如：00001：')
        if not id :
            input('要死啊你，按提示输入！！！')
            break
        name = input('请输入姓名')
        if not name:
            input('姓名未输入哦！！！')
            break
        try:
            english = int(input('请输入英语成绩'))
            java = int(input('请输入JAVA成绩'))
            python = int(input('请输入Python成绩'))
        except:
            print('输入的不是整数类型，重新输入')
        # 将学生信息添加到字典里
        student = {'id': id, 'name': name, 'english': english, 'java': java, 'python': python}
        # 将字典添加到列表中去
        student_list.append(student)

        answer = input('是否继续添加y/n')
        if answer.upper() == 'Y':
            continue
        else:
            break

    # 调用Save保存
    save(student_list)
    print('保存完毕')


# 定义一个保存文件
filename = 'student1.txt'

#将学生列表保存至文件当中
def save(lst):
    try:
        stu_txt = open(filename,'a',encoding='UTF-8')
    except:
        stu_txt = open(filename, 'w', encoding='UTF-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()