def haha(*ll):
    one, two, three = ll
    one += 100
    two -= 20
    three /= 4
    return one, two, three

one = int(input('one'))
two = int(input('two'))
three = int(input('three'))

ha = haha(one, two, three)
print("one:{} two:{} three:{}".format(*ha))