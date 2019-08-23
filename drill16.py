from sys import argv

script, filename = argv 

target = open(filename, 'w')

target.write(input("line1: "))
target.write('\n')
target.write(input("line2: "))
target.write('\n')
target.write(input("line3: "))

target.close

target = open('test.txt', 'r')
print(target.read())
