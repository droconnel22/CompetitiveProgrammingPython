import math
from cmath import phase

# Enter your code here. Read input from STDIN. Print output to STDOUT
# 1+2j
if __name__ =="__main__":    
    z = complex(input())
    #print(z)
    # Calculate r the distance from y to origin
    #r =abs(math.sqrt(math.pow(int(z.real),2) + math.pow(int(z.imag),2) ))
    r = phase(z)
    phi = abs(z) 
    print(phi)
    print(r)
    
   