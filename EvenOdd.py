def even_odd(num):
    if num%2==0:
        print("Even Number : {}".format(num))
    else:
        print("Odd Number : {}".format(num))


# Taking the number as input from user.
num = int(input())

# calling the function
even_odd(num)