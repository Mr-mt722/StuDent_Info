# 时间    @2023/5/30 21:36
# 作者    @Wwf
import sys

import Menu as menu
from StuDent_Dis import StuDent_insert as insert,StuDent_Delete as delete

def main():
    while True:
        menu.menm()
        choice = int(input('请选择\n'))
        # 菜单选择
        if choice in [1, 2, 3, 4, 5, 6, 7, 0]:
            # 退出系统判断
            if choice == 0:
                answer = input('你确定要退出系统吗y/n')
                # 讲字母转化为大写进行判断
                if answer.upper() == 'Y':
                    print('谢谢你的使用')
                    break
                else:
                    continue
            # 录入学生信息
            elif choice == 1:
                insert.StuDent_insert.student_insert()
            # 查找学生信息
            elif choice == 2:
                pass
            # 删除学生信息
            elif choice == 3:
                 delete.StuDent_Delete.student_delete()
            # 修改学生信息
            elif choice == 4:
                pass
            # 排序
            elif choice == 5:
                pass
            # 统计学生总数
            elif choice == 6:
                pass
            # 显示所有学生信息
            elif choice == 7:
                pass
            # elif choice == 0:
            #     sys.exit()
            else:
                print('请输入菜单栏中存在的')


if __name__ == '__main__':
    main()
