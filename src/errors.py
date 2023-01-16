# 创建时间：2023-01-15 20:19
import time

""" 提示信息并延时 """
def status(str, t=1):
    print('\n' + str)
    print('即将返回', end='')
    for i in range(3, 0, -1):
        print(i, end='')
        time.sleep(t)
    print('\n')


""" 输入错误 """
def inputError():
    status('请正确输入!!!', t=0.5)


""" 数据文件不存在 """
def noFile():
    status('数据文件不存在，无法操作，即将直接退出', t=0.5)


""" 数据文件为空 """
def fileIsEmpty():
    status('数据文件内容为空，无法进行操作，即将直接退出', t=0.5)




