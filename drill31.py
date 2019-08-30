x = float(input("> "))

if 0 < x < 10: # 浮点数可以和整数比较
    print("0 < x < 10")
elif x in range(10, 100):
    print("10 <= x < 100")
elif x in range(100, 200):
    print("100 <= x < 200")
else:
    print("x <= 0 or x >= 200")