stuff = "there is no failure only trying"

aa = stuff.split(' ') # 分割成list
print(aa)

print("len(stuff): ", len(stuff)) # 字符串长度，包括了空格
print("len(aa): ", len(aa)) # list长度

bb = ['apple', 'banana', 'donkey', 'duck', 'girl', 'boy']

print(aa.pop()) # 默认弹出最后一个

while len(aa) < 11:
    cc = bb.pop() # 弹出最后一个
    aa.append(cc) # append到list
    print("len(aa) now is: ", len(aa))

print(aa)

print(' '.join(aa)) # 连接
print('*'.join(aa[1:5])) # aa[1:5]表示aa[1]到aa[4], 与range(1,5)类似