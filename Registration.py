yes = 'y'
no = 'n'
list_name = []
print('註冊開始')
while True:
    n = input('是否結束y/n')
    if n == 'n':
        list_name.append(input('請輸入學生姓名'))
    elif n == 'y':
        print('註冊結束')
        print('名稱為', (list_name))
        print('總共', (len(list_name)), '人')
        break
    else:
        print('輸入錯誤，請輸入y/n')
