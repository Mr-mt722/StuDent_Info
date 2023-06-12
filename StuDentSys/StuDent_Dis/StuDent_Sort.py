# 时间    @2023/6/12 22:20
# 作者    @Wwf
from StuDentSys.StuDent_Dis.StuDent_Read import StuDent_Read as read
from StuDentSys.StuDent_Dis.StuDent_Show import StuDent_Show as show

class StuDent_Sort:
    def sort_by_id():
        """
        根据学生ID进行降序排序
        """
        students = read.read()
        sorted_students = sorted(students, key=lambda x: x['id'], reverse=True)
        show.show_student()

    def sort_by_name():
        """
        根据学生姓名进行降序排序
        """
        students = read.read()
        sorted_students = sorted(students, key=lambda x: x['name'], reverse=True)
        show.show_student()