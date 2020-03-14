'''猜数游戏
可自行选择次数
可自行选择范围'''


import random  #引入随机数模块

play_again = 'y'

print("**********number guessing game**********\n--by Kirit\n--in 2020.3")  #游戏名称·作者·时间

while play_again == ('y' or  'Y'):  #多次游戏

    print('\n<<<<<setting range>>>>>')

    ran0 = int(input('enter the minimum of range:'))  #设置范围最小值

    ran1 = int(input('enter the maximum of range:'))  #设置范围最大值

    print('\n<<<<<setting chances>>>>>')

    chances = int(input('how many chances do you need:'))  #选择次数

    print('\n<<<<<Game start>>>>>')

    guess = int(input("enter a number from 1 to 20:"))  #输入猜测的数字

    true = random.randint (ran0,ran1)  #设置随机答案

    def result_judge():  #定义判断结果函数

        if guess > true:

            print('too big')

        elif guess < true:

            print('too low')

        else:

            print('right')

    result_judge()  #调用函数

    print(chances - 1,'chances left')

    while (guess != true) and (chances - 1 > 0):  #加入循环结构并加入次数限制

        guess = int(input("wrong,guess agian:"))

        result_judge()

        chances -= 1

        if guess != true:
        
            print(chances - 1,"chances left")  #当猜数错误时显示剩余次数

    if chances - 1 == 0:

        print('you have no chances yet.') #提醒次数已用尽
        
    print('game over') #打印游戏结束

    play_again = input('\nplay again?(y/n):')  #询问是否再次游戏

else:

    print("\ngoodebye")
