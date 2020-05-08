from collections import OrderedDict
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    d = OrderedDict()
    for i in range(int(input())):
        temp = input().strip().split()
        key = " ".join(temp[:-1])
        if key not in d:
            d[key] = int(temp[-1])
        else:
            d[key]+= int(temp[-1])
    for d,v in d.items():
        print(d,v)