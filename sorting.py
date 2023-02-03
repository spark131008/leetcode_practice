def bubble_sort(l):
    list_length = len(l)
    for x in range(list_length):
        already_sorted = True

        for i in range(list_length - x - 1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]

                already_sorted = False
        if already_sorted:
            return l


def insertion_sort(l):
    for i in range(1, len(l)):
        key_item = l[i]
        j = i - 1

        while j >= 0 and l[j] > key_item:
            l[j], l[j+1] = key_item, l[j]
            j -= 1
    return l

def merge_sort(left, right):

    if(len(left) == 0):
        return right

    if(len(right) == 0):
        return left

    result = []
    left_index = right_index = 0

    while len(result) < len(left) + len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1


        if left_index == len(left):
            result += right[right_index:]
            break

        if right_index == len(right):
            result += left[left_index:]
            break

    return result


def merge(l):
    if len(l) < 2:
        return l

    midpoint = len(l) // 2

    return merge_sort(
        left = merge(l[:midpoint]),
        right = merge(l[midpoint:])
    )