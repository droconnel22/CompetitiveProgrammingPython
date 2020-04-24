









import string



def print_rangoli(size):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    interval = 1
    for _ in range(0,size*size):
        for i in range(0,size*size):
            print("-", end = '')
        print()
    
    # your code goes here
    return alphabet

if __name__ == '__main__':
    n = 5
    print_rangoli(n)