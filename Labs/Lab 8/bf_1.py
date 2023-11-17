# Write a Python program with builtin function to multiply all the numbers in a list

def multiplicationOfList(list):
    product = 1
    for i in range(0, len(list)):
        product = product * list[i]
    return product

print('Enter the size of the list:')
n = int(input())
print('Enter the values one by one')
list = []
for i in range(0, n):
    listNum = int(input())
    list.append(listNum)

print(multiplicationOfList(list))

# def multiplyList(nums):
#     product = 1
#     for num in nums:
#         product = product * num
    
#     return product


# nums = [1, 2, 3]
# result = multiplyList(nums)
# print(result) # Arnur said that print() is built-in function

