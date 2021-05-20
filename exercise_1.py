def is_prime(n):
    for i in range(2, n):
        if n % i == 0:  # 整除，i 是 n 的因數，所以 n 不是質數。
            return False
    return True     # 都沒有人能整除，所以 n 是質數。


c = int(input('輸入數字'))
h = int(input('輸入數字'))  # 得到輸入值 n。
if c > h:
    d = h
    j = c
else:
    d = c
    j = h
for i in range(d, j + 1):   # 產生 2 到 n 的數字。
    i_is_prime = is_prime(i)    # 判斷 i 是否為質數。
    if i_is_prime:              # 如果是，印出來。
        print(i)
