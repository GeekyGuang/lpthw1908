def mouse(one, two, three):
    four = 4
    h = "1 {}\n2 {}\n3 {}\n4 {}"
    print(h.format(one, two, three, four))

def write_into_doc(doc_name):
    txt = open(doc_name, 'w')
    txt.write("hello, world!\n" * 10)
    txt.close()  # 必须close才能保存
    txt = open(doc_name)
    print(txt.read())
    txt.close()

def unpack(*hello):  # 并不需要是 *args
    one, two = hello
    print(f"1 {one}\n2 {two}")

# on = input("one: ")
# tw = input("two: ")
# thr = input("three: ")

# mouse(on, tw, thr)

txt = input("Enter a file name")
write_into_doc(txt)

unpack("apple", "banana")