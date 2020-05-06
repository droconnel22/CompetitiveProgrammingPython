

# brute force
def magic(arr):
    for i in range(len(arr)):
        if(arr[i] ==1):
            return i
    return -1

# binary search approach
def magic2(arr):
    low = 0
    high = len(arr)-1
    while (low <= high):
        mid = (high-low)/2 + low
        if(arr[mid] == mid):
            return mid
        elif(arr[mid] < mid):
            low = mid+1
        elif(arr[mid] > mid):
            high = mid-1
    return -1



if __name__ == "__main__":
   pass