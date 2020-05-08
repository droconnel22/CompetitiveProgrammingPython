# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

if __name__ == "__main__":
    word,count = map(str,input().split())
    for j in combinations_with_replacement(sorted(word),int(count)):
        print("".join(j))

# https://docs.python.org/2/library/itertools.html#itertools.combinations_with_replacement