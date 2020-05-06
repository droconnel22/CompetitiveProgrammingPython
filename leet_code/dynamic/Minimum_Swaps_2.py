import math
import os
import random
import re
import sys


"""
Ok here we go!

You are given an unordered array consisting of 
consectutive integers < [1,2,3..n] without any duplicates.

consecutive ints
no duplicates
can inplace swap any two elements
you need to find the MIN # of swaps required to 
sort the array in ascending order
>ascending order
1,2,3,4...

You are allowed to swap any two elements. You need to find the 
min number of swaps required to sort the array in 
ascending order.

arr = [7,1,3,2,4,5,6]

1. Problem
2. Re-read
3. examples
4. best guess
5. execute
6. iterate
7. solve
8. optimize

i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]

It took 5 swaps to sort the array.

1 < n < 10^5 so basically huge

input is n the size of array
the second is n spaced integers consisting of the array

arr [4,3,1,2]
After swapping (0,2) we get arr: [1,3,4,2]
After swapping (1,2) we get arr: [1,4,3,2]
After swapping (1,3) we get arr: [1,2,3,4]

so we need a min of 3 swaps to sort the array

> OK so is this combimetrics ? 
Either swap or don't swap

ask more questions stay in motion
ok so what are some questions

1. how do i know the array is sorted?
2. how do i know when to select or not select the current combination
- swap the current elements
- swap the leave the first element swap the next
- keep going until the array is sorted
- right but the array keeps mutating
- every time you swap you have to count
- quicksort with a count?
- quick is demonstronablyt efasts with swap

Answer
- The idea is that if a occupies b' position and b' occupies
c' postion and son then there will be some integer x
which will occupy a's position, so it forms a cycle

so if any element arr is not at its correct position,
we shit it to its correct position j, then shift arrj to its
correct position k and so on.

So if len is the length of the cycle(num of elements in cycle) then it will
require a min len -1 swaps to rearrange the elements of the cycle
to their correct positions
3.  we find all such cycles and compute our answer

The correct positions of all the elements can be found by sorting the array by value and keeping track of the old and new positions.
 You may gain more clarity by the setters solution.



"""

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    memo = {a:i for i, a in enumerate(arr)}
    swaps = 0
    for i in range(len(arr)):
        actual, expected = arr[i],i+1
        actual_index, expected_index = i, memo[expected]
        if actual != expected:
            arr[actual_index] = expected
            arr[expected_index] = actual
            memo[actual] = expected_index
            memo[expected] = actual_index
            swaps+=1
    return swaps

   
   
    

def minimumswaps(arr,low,high,count):
    if(low >= high):
        return count
    
    p_index,p_count = partition(arr,low,high,count)
    minimumswaps(arr,low,p_index-1,p_count)
    minimumswaps(arr,p_index+1,high,p_count)
    

def partition(arr,low, high, count):
    i = (low-1) 
    pivot  = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # swap
            arr[i],arr[j] = arr[j],arr[i]
            count+=1
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1,count

def checkIfsorted(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i+1]-arr[i] != 1:
            return False
        i+=1
    return True



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
