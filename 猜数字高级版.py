import random
num = random.randint(1,10)
guess_number= int(input("输入你要猜测的数字"))
if guess_number == num :
    print("第一次就猜对了,你运气真好")
else:
    if guess_number > num:
        print("猜大了")
    else :
        print("猜小了")
    guess_number = int(input("再次输入你要猜测的数字"))
    if guess_number == num:
        print("第二次猜对了")
    else:
        if guess_number > num:
            print("猜大了")
        else:
            print("猜小了")
        guess_number = int(input("再次输入你要猜测的数字"))
        if guess_number == num :
            print("最后一次猜对了")
        else:
            print("三次机会都猜错了")