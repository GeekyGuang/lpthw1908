from sys import argv 

script, input_file = argv 

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end='')

current_file = open(input_file, 'w')
txt = """hajjkdjak
djskdkjds
sjkdkjdkj
keiksjdd"""
current_file.write(txt)
current_file.close()

current_file = open(input_file)

print("First let's print the whole file:")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
