# defing a fuction for even odd numbers.
def even_odd(num):
    if num%2==0:
        print("Even Number : {}".format(num))
        if num>10:
            print(f"It is a even two digit number : {num}")
        else:
            print(f"It is even single digit number : {num}")
    else:
        print("Odd Number : {}".format(num))


# Taking the number as input from user.
num = int(input())

# calling the function
even_odd(num)


