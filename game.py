import random


def game():
    total = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    answer = random.sample(total, 4)
    print('四位數密碼已準備完成,您有十次猜機會,遊戲開始.')
    for times in range(1, 11):
        print('第', (times), 'round')
        for error in range(3):  # 防呆
            guess = input('請輸入4個不重覆的數字:')
            set_guess = set(guess)
            if guess.isdigit() == False or len(guess) != 4:  # 排除不是數字跟不是4位數的可能
                print('請輸入正確')
            elif len(set_guess) != len(guess):  # 重覆數字的可能
                print('請輸入不重覆數字')
                continue
            else:
                break
        else:
            print('輸入錯誤三次,你沒有理解遊戲規則,請重新閱讀規則')
            break

        a = 0
        b = 0
        for i in range(4):
            if guess[i] == answer[i]:
                a += 1
            else:
                if guess[i] != answer[i] and guess[i] in answer:
                    b += 1

        if a != 4:
            if times < 10:
                print(a, 'A', b, 'B',)
            else:
                print('LoseGame!真可惜沒有猜對,正確答案是', answer)
                restart()

        else:
            print('恭喜你~Win the game!答案就是', answer)
            restart()


def restart():
    print('想再來一局嗎?請輸入(yes or no):')
    ans = input('請輸入(yes or no):')
    if ans == 'yes':
        game()
    elif ans == 'no':
        print('好吧88~有機會再挑戰')

    else:
        print('請輸入(yes or no)大小寫正確')
        restart()


game()
