import random
import math
secret=random.randint(0,99)
guess=0
tries=0
n=5
print('欢迎来到猜数游戏')
while tries<n and guess!=secret:
    tries=tries+1
    guess=int(input('请输入你猜的数：'))
    if guess>secret:
        print('大了')
    elif guess<secret:
        print('小了')
    else:
        print('恭喜你，答对了！猜了',tries,'次')
if tries==n and guess!=secret:
    print('机会用完了，再来一次！')
