# 多組測資以 EOF 結束
#
# 每組測資開始有兩個正整數 n,m (n<=500, m<=100000)
#
# 接下來 n 行有 n 個不超過100的正整數依序代表每個食物的飽足度
#
# 接下來 m 行每行有四個數字 x1,y1,x2,y2 (1 <= x1 <= x2 <= n, 1 <= y1 <= y2 <= n)
#
# 代表你想要吃掉食物的範圍
while 1:
    try:
        n,m = int(input())
        food = []
        for _ in range(n):
            a = input()
            food.append(a)
        print(food)
    except:
        break