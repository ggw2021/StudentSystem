# encoding=utf-8
# 创建时间：2023-01-15 18:34
import infoQuery
import errors
import infoMag

def main():
    while 1:
        infoQuery.menu()  # 功能菜单
        print('选择功能请输入0-7')
        choice = input('请选择: ')
        # ------------------------------------------
        if choice == '0':
            flag = 0
            while 1:
                ans = input('确定要退出系统吗?(y/n): ')
                if ans == 'y' or ans == 'Y':
                    flag = 1
                    print('谢谢使用！！再见')
                    break
                elif ans == 'n' or ans == 'N':
                    break
                else:
                    errors.inputError()
            if flag == 1:
                break
            else:
                continue
        # ------------------------------------------
        elif choice == '1':
            infoQuery.show()
        elif choice == '2':
            infoMag.insert()
        elif choice == '3':
            infoQuery.search()
        elif choice == '4':
            infoMag.delete()
        elif choice == '5':
            infoMag.modify()
        # elif choice == '6':
        #
        elif choice == '6':
            infoQuery.total()
        else:
            errors.inputError()
        # ------------------------------------------


if __name__ == '__main__':
    main()
