def sort(array):

    if len(array) == 1:
        return array

    mid = len(array) // 2
    left = sort(array[:mid])
    right = sort(array[mid:])

    return merge(left, right)

def merge(left, right):    
    result_index = 0
    result_size = len(left) + len(right)
    result = [0 for x in range(result_size)]
    
    left_index = 0
    right_index = 0

    while result_index < result_size:
        if left_index == len(left):
            result[result_index] = right[right_index]
            right_index += 1
        elif right_index == len(right):
            result[result_index] = left[left_index]
            left_index += 1
        elif right[right_index] <= left[left_index]:
            result[result_index] = right[right_index]
            right_index += 1
        else:
            result[result_index] = left[left_index]
            left_index += 1
        result_index += 1
    return result
    