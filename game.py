"""
猜數字遊戲
1.要可以任意產生亂數(1~50)
2.使用者可以猜測數字
3.偵測是否猜對?
4.可以多次猜測
5.
"""

import random

low, high = 1, 100
num = 10
x = random.randint(low, high)
print(x)

for i in range(num):
    y = eval(input(f"{i+1}/{num}請輸入一個數字{low}~{high}:"))

    if y == x:
        print("恭喜猜對")
        break
    else:
        if y > x:
            print(f"再低一點")
            if y <= high:
                high = y - 1
        else:
            print(f"再高一點")
            if y >= low:
                low = y + 1

if y != x:
    print(f"你輸了答案為:{x}")


"""while True:
    x = random.randint(low, high)
    print(x)
    if x == 50:
        break"""

# print(x)50
