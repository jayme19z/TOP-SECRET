# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

user_input = input()
num_list = [int(num) for num in user_input.split()]

result = has33(num_list)
print(result)
