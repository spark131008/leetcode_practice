myList = [8,3,5,2,7,4,1,23,4,51,2,3,]

# REPLACE ELEMENTS WITH GREATEST ELEMENT ON RIGHT SIDE and last element should be -1

def brute_force(arr):
    new_arr = []
    for i in range(1, len(arr)):
        new_max = max(arr[i:])
        new_arr.append(new_max)
    new_arr.append(-1)
    return new_arr

def leetcode_1299(arr):
    myMax = -1
    for x in range(len(arr)-1, -1, -1):
        newMax = max(myMax, arr[x])
        arr[x] = myMax
        myMax = newMax
    return arr

print(brute_force(myList))
print(leetcode_1299(myList))