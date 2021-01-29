# x = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# y = [
#     [10, 11, 12],
#     [13, 14, 15],
#     [16, 17, 18]
# ]

# result = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]

# print(len(x))

# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j] = x[i][j] + y[i][j]
#     for r in result:
#         print(r)


# for i in range(len(x)):
#     for j in range(len(y[0])):
#         for k in range(len(y)):
#             result[i][j] += x[i][k] * y[k][j]
#     for r in result:
#         print(r)

# str = input('Enter a string: ')
# words = str.split()

# words.sort()

# for word in words:
#     print(word)

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = input('Enter a string: ')

no_punc = ''

for char in my_str:
    if char not in punctuation:
        no_punc = no_punc + char
print(no_punc)
