import random
min = input('終極密碼! 請輸入數字範圍，起始數字：')
max = input('末尾數字：')
min = int(min)
max = int(max)
count = 0
answer = random.randint(min,max)
while True:
    count = count + 1
    print ('第', count, '局')
    x = input('請猜數字:')
    x = int(x)
    if x == answer:
        print ('恭喜答對')
        break
    if x < answer:
        print ('數字範圍：大於', x, '小於', max)
        min = x
    if x > answer:
        print ('數字範圍：大於', min, '小於', x)
        max = x
