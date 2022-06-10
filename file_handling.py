# opening the file and closing after print.
file = open("a.txt")
text = file.read()
print(text)
file.close()


# opening file in read mode using with
with open("b.txt") as f:
    f_read = f.read()  # it reads the files and gives us the text from file
    print(f_read)


# Opening a file in write mode
with open("b.txt", mode="w") as open_write:  # whenever we open file in write mode all the data is lost.
    context = open_write.write("dinesh")   # this line every time writes something new after clearing.
    print(context)


# opening the file in append mode
with open("b.txt", mode="a") as append_mode:
    text = append_mode.write("\nhi, welcome")  # it writes a new line and append in the file
    print(text)


# checking read mode functions
with open("b.txt", mode="r") as opn_read:
    text = opn_read.read()         # this read method print the text in the file.
    print(text)


# read mode with read lines method
with open("b.txt") as opn_read:
    text = opn_read.readlines()  # this reads all the file and give that in a list.
    print(text)
    print(type(text))


# read mode with readable method
with open("b.txt") as opn_read:
    text = opn_read.readable()  # this reads all the file and give that in a list.
    print(text)
    print(type(text))


# read mode with readline method
with open("b.txt") as opn_read:
    text = opn_read.readline()  # this reads only the first line of the file.
    print(text)
    print(type(text))


# writing a new lines using append mode.
with open("b.txt", mode="a") as opn_read:
    text = opn_read.writelines("\nwriting a new lines with append mode\nthe lines has appended")
    print(text)
