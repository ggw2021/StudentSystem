# encoding=utf-8
# 创建时间：2023-01-15 22:39
import os
import errors

""" 学生数据文件 """
filename = 'data.txt'

""" 功能菜单 """
def menu():
    # os.system('cls')
    print('\n================= |学生信息管理系统| =================')
    print('--------------------= 功能菜单 =--------------------')
    print('\t\t  1、显示所有学生信息')
    print('\t\t  2、录入学生信息')
    print('\t\t  3、查找学生信息')
    print('\t\t  4、删除学生信息')
    print('\t\t  5、修改学生信息')
    # print('\t\t\t\t 6、排序')
    print('\t\t  6、统计学生总人数')
    print('\t\t  0、退出系统')


""" 显示所有学生信息 """
def show():
    if os.path.exists(filename):
        # 取出所有的学生信息
        with open(filename, 'r', encoding='utf-8') as datafile:
            studentList = datafile.readlines()
            # 文件存在，且信息在studentList列表中
            if not studentList:
                # 文件为空
                print('\n没有学生信息')
                # errors.fileIsEmpty()
            else:
                print('\n所有的学生信息为：')
                resList = []
                for item in studentList:
                    resList.append(eval(item))
                showStudent(resList)
    else:
        print('\n没有学生信息')
        # errors.noFile()
    input('按任意键继续...')


""" 查询学生信息 """
def search():
    while 1:
        print('\n以下为查找信息操作：')
        # 特判
        if os.path.exists(filename):
            # 取出所有的学生信息
            with open(filename, 'r', encoding='utf-8') as datafile:
                studentList = datafile.readlines()
        else:
            errors.noFile()
            break
        # 文件存在，且信息在studentList列表中
        if not studentList:
            # 文件为空
            errors.fileIsEmpty()
            break

        # 要查询的学生的id
        while 1:
            studentId = input('请输入六位纯数字ID(如2120062): ')
            # 判断位数是否合法
            if len(studentId) != 6:
                errors.inputError()
                continue
            # 判断是否是数字
            try:
                int(studentId)
            except ValueError:
                errors.inputError()
                continue
            # 合法输入
            break

        # 文件存在，且信息在studentList列表中，且非空
        resList = []
        flag = False  # 是否存在该学生
        for item in studentList:
            student = eval(item)
            if student['id'] == studentId:
                flag = True
                resList.append(student)
        if flag:
            print('查找成功')
            showStudent(resList)
        else:
            # 不到为啥，linux中过不了编译，win可以
            # print(f'\n数据文件内没有id为{str(studentId)}的学生\n')
            # 这样写又可以
            print('\n数据文件内没有id为{0}的学生\n'.format(studentId))

        # 是否继续删除
        flag = 0
        while 1:
            ans = input('是否继续查询?(y/n): ')
            if ans == 'y' or ans == 'Y':
                break
            elif ans == 'n' or ans == 'N':
                flag = 1
                break
            else:
                errors.inputError()
        if flag == 1:
            break
        else:
            continue


""" 查询学生人数 """
def total():
    if os.path.exists(filename):
        # 取出所有的学生信息
        with open(filename, 'r', encoding='utf-8') as datafile:
            studentList = datafile.readlines()
            if not studentList:
                # 文件为空
                errors.fileIsEmpty()
            else:
                print('\n一共有{0}名学生的信息'.format(len(studentList)))
                input('按任意键继续...')
    else:
        errors.noFile()
    # 文件存在，且信息在studentList列表中


# =======================================
# 显示一个学生的信息
def showStudent(lst):
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', 'English成绩', 'Python成绩', 'Java成绩', '总成绩'))
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item['id'],\
                                 item['name'],\
                                 item['English'],\
                                 item['Python'],\
                                 item['Java'],\
                                 int(item['English']) + int(item['Python']) + int(item['Java'])))
# =======================================

