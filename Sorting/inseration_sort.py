def inseration_sort(array):
    index = 0;
    while index < len(array):
        j = index
        while j > 0:
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
            j -= 1

        index += 1
    return array
