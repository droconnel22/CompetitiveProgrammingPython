

def binary_search(arr,target):
    left = 0
    right = len(arr)

    while left <= right:
        mid = (right-left)//2+left
        if arr[mid] < target:
            left = mid+1
        elif arr[mid] > target:
            right = mid -1
        else:
            return mid
    return -1

arr = [1,2,3,4,5,6]
target = 7

result = binary_search(arr,target)


if result != -1:
    print("Element is present at index %d"%result)
else:
    print("Element is not present in array")

