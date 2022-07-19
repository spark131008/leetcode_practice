nums = [2,7,11,15]
target = 9

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

def brute_force(arr, target):
    for i in range(len(arr)-1):
        for j in range(1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j

def hash_map(arr, target):
    my_hash_map = {} #key : index

    for index, value in enumerate(arr):
        diff = target - value
        if diff in my_hash_map:
            return my_hash_map[diff], index
        my_hash_map[value] = index


# print(brute_force(nums, target))
print(hash_map(nums, target))