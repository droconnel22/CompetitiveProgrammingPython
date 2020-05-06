# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

if __name__ =="__main__": 
    # n,m = map(int,raw_input().strip().split())
    n,m = map(int,input().strip().split())
    d = defaultdict(list)
    for i in range(n):
        d[str(input())].append(i+1)    
    for y in range(m):
        letter = input()
        if letter in d:
            print(" ".join(map(str,d[letter])))
        else:
            print(-1)