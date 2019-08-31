def while_loop(element, i, inc):
    while i < 100:
        element.append(i)
        i += inc
    

mm = []
i = 0
inc = int(input("increment: "))

# while_loop(mm, i, inc)
for i in range(0, 100):
    mm.append(i)
    i += inc  # 这个递增没用

for i in mm:
    print(i)

