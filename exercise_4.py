f = (input('請輸入0-9'))
for i in range(1, 10):
    for j in range(1, 10):
        print(str(i*j).replace(f, '*'), end='\t')  # 變數不用分號
    print()
