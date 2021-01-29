# Python code to demonstrate 
# how to update an element in array 

# importing array module 
import array 

# initializing array with array values 
# initializes array with signed integers 
arr = array.array('i', [1, 2, 3, 1, 2, 5]) 

# printing original array 
print ("Array before updation : ", end ="") 
for i in range (0, 6): 
	print (arr[i], end =" ") 

print ("\r") 

# updating a element in a array 
arr[2] = 6
print("Array after updation : ", end ="") 
for i in range (0, 6): 
	print (arr[i], end =" ") 
print() 

# updating a element in a array 
arr[4] = 8
print("Array after updation : ", end ="") 
for i in range (0, 6): 
	print (arr[i], end =" ") 


# print ("The new created array is : ", end ="")
# for i in range (0, 6):
#     print (arr[i], end =" ")

# print ("\r")

# # using index() to print index of 1st occurrenece of 2
# print ("The index of 1st occurrence of 2 is : ", end ="")
# print (arr.index(2))

# # using index() to print index of 1st occurrenece of 1
# print ("The index of 1st occurrence of 1 is : ", end ="")
# print (arr.index(1))


# a = [1, 2, 3, 4, 5, 6]

# for i in a:
#     # print(i, end=' ')

#     print(a.index(3))

    # sliced_arr = a[1: -3]
    # print(sliced_arr)


# print(a.pop())
# a.remove(2)
# print(a)


# for i in range(0, 5):
#     print(i)

    # for i in range(0, 4):
    #     print(a[i], end=' ')

    # b = arr.array('d', [2.5, 3.2, 3.30])

    # for i in range(0, 3):
    #     print(b[i], end=' ')
