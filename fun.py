# def lcm(x, y):
#     if x > y:
#         greater = x
#     else:
#         greater = y

#     while(True):
#         if((greater % x == 0) and (greater % y == 0)):
#             lcm = greater
#             break
#         greater += 1
#     return lcm


# num1 = int(input('Enter a number: '))
# num2 = int(input('Enter another number: '))
# print('LCM of: ', num1, num2, 'is', lcm(num1, num2))


# def hcf(x, y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller+1):
#         if((x%i == 0) and (y%i == 0)):
#             hcf = i
#     return hcf

# num1 = int(input('Enter First number: '))
# num2 = int(input('Enter Second number: '))

# print('HCF of', num1, num2, 'is', hcf(num1, num2))

# dec = int(input('Enter a number: '))

# print(bin(dec), 'in binary')
# print(oct(dec), 'in octal')
# print(hex(dec), 'in hex')

# c = input('Enter a charachter: ')

# print(ord(c))

# def add(x, y):
#     return x + y


# def sub(x, y):
#     return x - y


# def mul(x, y):
#     return x * y


# def div(x, y):
#     return x / y


# choice = input('Enter Arthematic operator +, -, *, /: ')

# num1 = int(input('Enter First number: '))
# num2 = int(input('Enter Second number: '))
# if(choice == '+'):
#     print(add(num1, num2))

# if(choice == '-'):
#     print(sub(num1, num2))

# if(choice == '*'):
#     print(mul(num1, num2))

# if(choice == '/'):
#     print(div(num1, num2))


# import calendar

# yy = int(input('Enter Year: '))
# mm = int(input('Enter Month: '))

# print(calendar.month(yy, mm))

# def rec_feb(n):
#     if n <= 1:
#         return n
#     else:
#         return(rec_feb(n-1) + rec_feb(n-2))

# num = int(input('Enter no of terms: '))

# if num <= 0:
#     print('Enter positive number')
# else:
#     for i in range(num):
#         print(rec_feb(i))

def rec_fac(n):
    if(n == 1):
        return n
    else:
        return n*rec_fac(n-1)

num = int(input('Enter a number: '))
if(num < 0):
    print('Enter Positive number')
else:
    print(rec_fac(num))