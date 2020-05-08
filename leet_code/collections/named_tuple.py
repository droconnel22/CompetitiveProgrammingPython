# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

if __name__ == "__main__":     
    n = int(input())
    total_marks = 0
    TestCase = namedtuple('TestCase',input().strip().split())
    for i in range(0,n):       
        total_marks +=int(TestCase._make(input().strip().split()).MARKS)
    print("{:.2f}".format(total_marks/n))
