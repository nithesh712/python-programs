# def pypart(n):
#     for i in range(0, n):
#         for j in range(0, i+1):
#             print('* ', end='')
#         print('\r')

# pypart(5)

# def pypart(n):
#     myList = []
#     for i in range(1, n+1):
#         myList.append('* '*i)
#     print('\n'.join(myList))

# pypart(5)

# def pypart2(n):
#     k = 2*n - 2

#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=' ')
        
#         k = k-2

#         for j in range(0, i+1):
#             print('* ', end='')

#         print('\r')

# pypart2(4)

# def triangle(n):
#     k = n-1

#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=' ')

#         k = k-1

#         for j in range(0, i+1):
#             print('* ', end='')
            
#         print('\r')

# triangle(4)

# def numpat(n):
#     num = 1

#     for i in range(0, n):
#         num = 1

#         for j in range(0, i+1):
#             print(num, end =' ')

#             num = num + 1
        
#         print('\r')

# numpat(4)

# def contnum(n):

#     num = 1

#     for i in range(0, n):
#         # num = 1

#         for j in range(0, i+1):
#             print(num, end=' ')
#             num += 1
        
#         print('\r')

# contnum(4)

# def alphpat(n):

#     num = 65

#     for i in range(0, n):
#         for j in range(0, i+1):
#             print(chr(num), end=' ')
#         num += 1
#         print('\r')

# alphpat(5)

# def contalphpat(n):
#     num = 65

#     for i in range(0, n):
#         for j in range(0, i+1):
#             print(chr(num), end=' ')
#             num += 1
#         print('\r')

# contalphpat(5)

def charpat(n):
    num = 65

    for i in range(0, n):
        for j in range(0, i+1):
            print(chr(num), end=' ')
        num += 1
        print('\r')
charpat(5)