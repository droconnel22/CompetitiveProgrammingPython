"""
Sliding Window Technique

Optimization Technique

Given an array of integers of size N,
find maximum sum of K
consecutive elements
"""



def naive_try(arr,k):
    index = 0
    max_sum = 0
    while index < len(arr)-k+1:       
        temp_sum = 0
        for i in range(index,index+k):
           temp_sum+=arr[i]
           print(arr[i],end=",")
        print("\n")
        if temp_sum > max_sum:
            max_sum = temp_sum
        index+=1
    return max_sum

# subtracting the last element while adding the next
def sliding_window(arr,k):
    window_sum = sum([arr[i] for i in range(k)])
    max_sum = window_sum
    for i in range(0,len(arr)-k):
        window_sum = (window_sum - arr[i]) + arr[i+k]
        max_sum = max(max_sum,window_sum)
    return max_sum



if __name__ == "__main__":
    arr = [80,-50,90,100]
    k = 2
    print(naive_try(arr,k))
    print(sliding_window(arr,k))
