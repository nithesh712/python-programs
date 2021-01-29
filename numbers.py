# def calculateLength(n):
#     length = 0
#     while(n != 0):
#         length = length + 1
#         n = n//10
#     return length

# num = 175
# rem = sum = 0;
# len = calculateLength(num)

# n = num

# while(num > 0):
#     rem = num%10
#     sum += int(rem**len)
#     num = num//10
#     len = len - 1

# if(sum == n):
#     print(str(n) + ' is disarium number')
# else:
#   print(str(n) + ' is not disarium number')


# def calculateLength(n):
#     length = 0
#     while(n != 0):
#         length = length + 1
#         n = n//10
#     return length

# def sumOfDigits(num):
#     rem = sum = 0
#     len = calculateLength(num)

#     while(num > 0):
#         rem = num%10
#         sum = sum + (rem**len)
#         num = num//10
#         len = len - 1
#     return sum

# for i in range(1, 101):
#     result = sumOfDigits(i);

#     if(result == i):
#         print(i),

# num = 156
# rem = sum = 0

# n = num

# while(num > 0):
#     rem = num % 10
#     sum = sum + rem
#     num = num//10

# if(n % sum == 0):   
#      print('Yes')
# else:
#     print('No')

arr = [5, 10, 20, 30]

for i in range(len(arr)-1, -1, -1):
    print(arr[i])