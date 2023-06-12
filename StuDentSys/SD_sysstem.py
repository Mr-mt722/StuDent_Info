# 时间    @2023/5/30 21:36
# 作者    @Wwf
import sys

import Menu as menu
from StuDent_Dis import StuDent_insert as insert, StuDent_Delete as delete, StuDent_Show as show, \
    StuDent_Update as update \
    , StuDent_Select as select, StuDent_Read as read, StuDent_Sort as sort


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
                    sys.exit()
                else:
                    continue
            # 录入学生信息
            elif choice == 1:
                insert.StuDentInsert.add_student()
            # 查找学生信息
            elif choice == 2:
                select.StuDent_Select.select_student()
            # 删除学生信息
            elif choice == 3:
                delete.StuDent_Delete.delete_student()
            # 修改学生信息
            elif choice == 4:
                update.StuDent_Update.update_student()
            # 排序
            elif choice == 5:
                while True:
                    method = input('你想要通过姓名还是id排序呢？0/1')
                    if not method.isdigit():
                        print('必须是0/1哈')
                        answer = input('是否继续？y/n：')
                        if answer.upper() == 'Y':
                            continue
                        else:
                            break
                    elif method == '1':
                        sort.StuDent_Sort.sort_by_id()
                        break
                    elif method == '0':
                        sort.StuDent_Sort.sort_by_name()
                        break


            # 统计学生总数
            elif choice == 6:
                line = len(read.StuDent_Read.read()) + 1
                print(f'总共有{line}个学生')
            # 显示所有学生信息
            elif choice == 7:
                show.StuDent_Show.show_student()
            # elif choice == 0:
            #     sys.exit()
            else:
                print('请输入菜单栏中存在的')


if __name__ == '__main__':
    main()
