# 时间    @2023/6/3 15:34
# 作者    @Wwf


class StuDent_Show:
    @staticmethod
    def show_student():
        """
        展示所有学生信息
        """
        with open('student1.txt', 'r', encoding='UTF-8') as f:
            lines = f.readlines()
            if not lines:
                print('没有学生信息，请先添加学生信息')
                return
            students = [eval(line) for line in lines]  # 将所有学生信息转换为字典列表
            # 计算每个字段的最大长度
            max_name_len = max([len(student['name']) for student in students])
            max_age_len = max([len(str(student['age'])) for student in students])
            max_gender_len = max([len(student['gender']) for student in students])
            max_id_len = max([len(student['id']) for student in students])
            # 计算表头的长度
            header_len = max(max_name_len, 4) + max_age_len + max_gender_len + max_id_len + 6
            # 输出表头
            print('{:<{name_len}}{:<{age_len}}{:<{gender_len}}{:<{id_len}}'.format('姓名', '年龄', '性别', '学号',
                                                                                   name_len=max(max_name_len, 4) + 2,
                                                                                   age_len=max_age_len + 2,
                                                                                   gender_len=max_gender_len + 2,
                                                                                   id_len=max_id_len + 2))
            # 输出分割线
            print('-' * header_len)
            # 输出每个学生的信息
            for student in students:
                print('{:<{name_len}}{:<{age_len}}{:<{gender_len}}{:<{id_len}}'.format(student['name'], student['age'],
                                                                                       student['gender'], student['id'],
                                                                                    name_len=max(max_name_len, 4) + 2,
                                                                                       age_len=max_age_len + 2,
                                                                                       gender_len=max_gender_len + 2,
                                                                                       id_len=max_id_len + 2))