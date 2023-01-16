# 创建时间：2023-01-15 20:29
import os
import errors
import infoQuery

""" 学生数据文件 """
filename = 'data.txt'


""" 录入信息 """
def insert():
    student_list = []
    while 1:
        stu = getStudent()
        # 查看id是否重复
        if os.path.exists(filename):
            # 取出所有的学生信息
            with open(filename, 'r', encoding='utf-8') as datafile:
                studentList = datafile.readlines()
                flag = False  # 是否已经存在id
                for item in studentList:
                    student = eval(item)
                    if student['id'] == stu['id']:
                        flag = True
                if flag:
                    print('id已经存在，请更换id')
                    continue
        # 添加一个学生
        student_list.append(stu)

        # 是否继续添加y/n
        flag = 0
        while 1:
            ans = input('是否继续添加?(y/n): ')
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
    sava(student_list)


""" 删除学生信息 """
def delete():
    while 1:
        print('\n以下为删除信息操作：')
        # 特判
        if os.path.exists(filename):
            # 取出所有旧的学生信息
            with open(filename, 'r', encoding='utf-8') as datafile:
                studentIOld = datafile.readlines()
        else:
            errors.noFile()
            break
        # 文件存在，且信息在studentIOld列表中
        if not studentIOld:
            # 文件为空
            errors.fileIsEmpty()
            break

        # 要删除学生的id
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

        # 文件存在，且信息在studentIOld列表中，且非空
        # 重写文件
        flag = False  # 是否存在该学生
        with open(filename, 'w', encoding='utf-8') as datafile:
            student = {}
            for item in studentIOld:
                student = eval(item)
                if student['id'] != studentId:
                    datafile.write(str(student) + '\n')
                else:
                    flag = True
        if flag:
            print(f'\nid为{str(studentId)}的学生信息已经被删除了\n')
        else:
            print(f'\n数据文件内没有id为{str(studentId)}的学生\n')

        # 操作完成后显示所有学生的信息
        infoQuery.show()
        # 是否继续删除
        flag = 0
        while 1:
            ans = input('是否继续删除?(y/n): ')
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


""" 修改学生信息 """
def modify():
    infoQuery.show()
    while 1:
        print('\n以下为修改信息操作：')
        # 特判
        if os.path.exists(filename):
            # 取出所有旧的学生信息
            with open(filename, 'r', encoding='utf-8') as datafile:
                studentIOld = datafile.readlines()
        else:
            errors.noFile()
            break
        # 文件存在，且信息在studentIOld列表中
        if not studentIOld:
            # 文件为空
            errors.fileIsEmpty()
            break

        # 要修改学生的id
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

        # 文件存在，且信息在studentIOld列表中，且非空
        # 重写文件
        flag = False  # 是否存在该学生
        with open(filename, 'w', encoding='utf-8') as datafile:
            student = {}
            for item in studentIOld:
                student = eval(item)
                if student['id'] != studentId:
                    datafile.write(str(student) + '\n')
                else:
                    flag = True
                    print(f'\n存在id为{str(studentId)}的学生，可以进行修改')
                    datafile.write(str(getStudent()) + '\n')

        if flag:
            print(f'\nid为{str(studentId)}的学生信息已经被修改了\n')
        else:
            print(f'\n数据文件内没有id为{str(studentId)}的学生\n')

        # 操作完成后显示所有学生的信息
        infoQuery.show()
        # 是否继续删除
        flag = 0
        while 1:
            ans = input('是否继续修改?(y/n): ')
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

# =============================================
# 数字num是否在[a, b]范围内
def isNumLegal(a, b, num):
    if num < a or num > b:
        return False
    return True

# 保存学生信息到文件
def sava(lst):
    try:
        datafile = open(filename, 'a', encoding='utf-8')
    except:
        # 文件不存在的话
        datafile = open(filename, 'w', encoding='utf-8')
    for item in lst:
        datafile.write(str(item) + '\n')
    datafile.close()
    errors.status('文件已录入!!!', 0.5)

# 返回一个学生的字典类型
def getStudent():
    # 学生ID
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

    # 学生姓名
    while 1:
        name = input('请输入学生姓名(最大20个字符): ')
        # 判断位数是否合法
        if len(name) > 20:
            errors.inputError()
            continue
        # 合法输入
        break

    # 英语成绩
    while 1:
        # 是否是数字
        try:
            english = int(input('请输入英语成绩(0-150): '))
        except ValueError:
            errors.inputError()
            continue
        # 是否超出范围
        if not isNumLegal(0, 150, english):
            errors.inputError()
            continue
        # 合法输入
        break

    # Python成绩
    while 1:
        # 是否是数字
        try:
            python = int(input('请输入Python成绩(0-150): '))
        except ValueError:
            errors.inputError()
            continue
        # 是否超出范围
        if not isNumLegal(0, 150, python):
            errors.inputError()
            continue
        # 合法输入
        break

    # Java成绩
    while 1:
        # 是否是数字
        try:
            java = int(input('请输入Java成绩(0-150): '))
        except ValueError:
            errors.inputError()
            continue
        # 是否超出范围
        if not isNumLegal(0, 150, java):
            errors.inputError()
            continue
        # 合法输入
        break

    # 信息存在字典里
    return {'id': studentId, 'name': name, 'English': english, 'Python': python, 'Java': java}
# ==============================================


