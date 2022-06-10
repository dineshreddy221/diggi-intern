file = open("a.txt")
text = file.read()
print(text)
file.close()


# opening file with statement
with open("b.txt") as f:
    f_read = f.read()
    print(f_read)

# try and except

try:
    n = input("enter a number\n")
    a = n + 4
    print(a)
except TypeError:
    print("type error")
