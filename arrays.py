# arr1 = [1, 2, 3, 4, 5]

# arr2 = [None] * len(arr1)

# for i in range(0, len(arr1)):
#     arr2[i] = arr1[i]

# for i in range(0, len(arr2)):
#     print(arr2[i])

# arr = [1, 5, 2, 3, 1, 4, 5, 2, 9, 1]

# fr = [None] * len(arr)
# visited = -1

# for i in range(0, len(arr)):
#     count = 1
#     for j in range(i+1, len(arr)):
#         if(arr[i] == arr[j]):
#             count += 1
#             fr[j] = visited

#     if(fr[i] != visited):
#         fr[i] = count

# print('-----------------------')
# print('Element | Frequency')
# print('-----------------------')

# for i in range(0, len(fr)):
#     if(fr[i] != visited):
#         print(' ' + str(arr[i]) + ' | ' + str(fr[i]))
# print('----------------------')

# arr = [1, 2, 3, 4, 1, 3, 1, 6, 8]
# fr = [None] * len(arr)

# visited = -1

# for i in range(0, len(arr)):
#     count = 1
#     for j in range(i+1, len(arr)):
#         if(arr[i] == arr[j]):
#             count += 1

#             fr[j] = visited
#     if(fr[i] != visited):
#         fr[i] = count

# for i in range(0, len(fr)):
#     if(fr[i] != visited):
#         print(str(arr[i]) + '|' + str(fr[i]))


# arr = [1, 2, 3, 4, 5]

# n = 3

# for i in range(0, len(arr)):
#     print(arr[i])

# for i in range(0, n):
#     first = arr[0]

#     for j in range(0, len(arr)-1):
#         arr[j] = arr[j+1]

#     arr[len(arr)-1] = first

# print()

# print('-----------')
# for i in range(0, len(arr)):
#     print(arr[i])

# arr = [1, 2, 3, 4, 2, 7, 8, 8, 3, 4, 3];

# for i in range(0, len(arr)):
#     for j in range(i+1, len(arr)):
#         if(arr[i] == arr[j]):
#             print(arr[j])

# arr = [1, 2, 3, 4, 5]

# for i in range(0, len(arr)):
#     print(arr[i])

# for i in range(len(arr) - 1, -1, -1):
#     print(arr[i])

# arr = [1, 2, 3, 4, 5, 6, 7]

# for i in range(0, len(arr), 2):
#     print(arr[i])

# arr = [4, 12, 20, 13, 42, 65]
# max = arr[0]

# for i in range(0, len(arr)):
#     if(max < arr[i]):
#         max = arr[i]

# print(str(max))

# arr = [4, 12, 20, 3, 42, 65]
# small = arr[0]

# for i in range(0, len(arr)):
#     if(arr[i] < small):
#         small = arr[i]

# print(small)

# arr = [4, 12, 20, 13, 42, 65]

# sum = 0

# for i in range(0, len(arr)):
#     sum += arr[i]

# print(sum)

# arr = [1,2,3,4,5]
# n = 3

# for i in range(0, n):
#     last = arr[len(arr) -1]

#     for j in range(len(arr)-1, -1, -1):
#         arr[j] = arr[j-1]

#     arr[0] = last

# print()

# for i in range(0, len(arr)):
#     print(arr[i])

# arr = [6, 4, 3, 2, 6]
# temp = 0

# for i in range(0, len(arr)):
#     for j in range(i+1, len(arr)):
#         if(arr[i] > arr[j]):
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp

# for i in range(0, len(arr)):
#     print(arr[i])

arr = [6, 4, 3, 2, 6]
temp = 0

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i]< arr[j]):
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

for i in range(0, len(arr)):
    print(arr[i])