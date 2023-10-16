# Write a function that takes in a list of integers and returns True if it contains 007 in order

def contains007(nums):
    if len(nums) < 3:
        return False

    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True

    return False

user_input = input()
num_list = [int(num) for num in user_input.split()]

result = contains007(num_list)
print(result)
