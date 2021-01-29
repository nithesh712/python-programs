num = float(input('Enter a Number: '))

if(num > 0):
    print('Even Number it is', num)
elif(num == 0):
    print('Its a Zero')
else:
  print('Negative number it is', num)

num = float(input('Enter a Number: '))

if(num % 2 == 0 and num != 0):
    print(f'It is Even number {num}')
elif(num == 0):
    print('It is Zero')
else:
    print(f'It is odd number {num}')

# Leap Year
year = int(input('Enter a year to check it is leap: '))
if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(f'It is leap year {year}')
        else:
            print(f'{year}, it is not leap year')
    else:
        print(f'{year} is a leap year')
else:
    print(f'{year} is not leap year')

num = int(input('Enter Number: '))

if num > 1:
    for i in range(2, num):
        if(num % i == 0):
            print('It is not prime number')
            print(i, 'times', num//i, 'is', num)
            break
    else:
        print(num, 'is prime')

else:
    print(num, 'is not prime')

num = int(input('Enter a number: '))

if(num > 1):
    for i in range(2, num):
        if(num % i == 0):
            print('It is not a prime')
            break
    else:
        print('It is a prime')
else:
    print('Not Prime')

# Finding Prime between sequence

lower = int(input('Enter first number: '))
upper = int(input('Enter second number: '))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if(num % i == 0):
                break
        else:
            print(num)

# Factoral Program
num = int(input('Enter number: '))

factorial = 1

if (num < 0):
    print('Not factorial number')
elif (num == 0):
    print('Factorial is 1')
else:
    for i in range(1, num + 1):
        print(i)
        factorial = factorial * i
    print(factorial)

# Table Program

num = int(input('Table Number: '))
for i in range(1, 11):
    print(num, 'x', i, '=', num*i )


num = int(input('Enter Number: '))
n1 = 0
n2 = 1
count = 2

if num <= 0:
    print('Enter positive value')
elif num == 1:
    print('Febonacci number is: ', n1)
else:
    print('Febonacci sequence is:')
    print(n1,' , ',n2, end=',')
    while count < num:
        nth = n1 + n2
        print(nth, end=' , ')

        n1 = n2
        n2 = nth
        count += 1

#  Fibonacci Number 
num = int(input('Enter a number: '))

n1 = 0
n2 = 1
count = 2

if(num<=0):
    print('Enter a positive value')
elif(num==1):
    print(n1)
else:
    print(n1,',', n2, end =', ')
    while count < num:
        next_num = n1 + n2
        print(next_num, end=', ')

        n1 = n2
        n2 = next_num
        count += 1

num = int(input('Enter a number: '))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum + digit**3
    temp = temp//10
    print(temp)

if num == sum:
    print(num, 'It is Amstrong')
else:
    print(num, 'Not an Amstrong number')

lower = int(input('Enter lower value: '))
upper = int(input('Enter upper value: '))

for num in range(lower, upper+1):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp%10
        sum += digit**3
        temp //= 10
        if num == sum:
            print(num)

num = int(input('Enter a number: '))

if num<0:
    print('Enter positive number')
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print(sum)