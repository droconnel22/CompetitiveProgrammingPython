"""

everyones in line for the rollercoaster

# of people queued up

each person wears a sticker indicating thier initial
position in the queue

initial positions increment by 1 from 1 
at the front of the line to n at the back

any person in the queue can be bribe the person
directly in front of them to swap positions

if two people swap positions, they still wear the same
sticker denoting their original places in line.

one person can bribe at most two others

Find the minimum number of bribes that took place to 
get the queue into its current state.

Print an integer representing the min number of bribes
necssary or 'Too chatoic' if the line configuration is not
possible.

Input:
q: an array of integers
The first line contains an integer t, the number of test cases
Each of the next t pairs of lines are as follows:
- the first line contains an integer t, the # people in queue
- the second line has n space seperated integers describting the
final state of the queue

Constraints
 1 < t < 10 examples
 1 < n  < 10^5

Examples :
n = 8
Person 5 bribes 4
1,2,3,5,4,6,7,8

Example 2:
5
2 1 5 3 4


Out put: 
3

Research:

2 1 5 3 4
1 2 3 4 5 

2 is ahead of 1 so +1
5 is ahead by 2 of 3 adn 4 +2

3

Example 3:
5
2 5 1 3 4
1 2 3 4 5
2 is ahead by 1
5 is ahed by 4 and we have a limit of 2 so 
'Too chaotic'

1 2 5 3 7 8  4 6

1 2 3 4 5 6  7 8
    2   2 2 {1}
 
if no rotation

1 2 5 3 7 8 6 4

1 2 3 4 5 6 7 8
    2   2 2    

over take?
1 2 5 3 7 8 6 4
1 2 3 4 5 6 7 8
0 0 
    Y 1           1
      Y 1 2 3 4   5
        Y         6
          Y       7    

over take w/ chaos
2 5 1 3 4
1 2 3 4 5
Y 1 2  (2 > 1) ? 1, (5 >1) ? => 2
  Y (5 > 2) ? 1 - (5 > 1) ? 1+1 -  (5 > 3) ? 1+1+1 !


# All you need to do is to count the number of people who overtake a person.

# take action just don't sit there and suffer


1 2 5 3 7 8 6 4
1 2 3 4 5 6 7 8

1 0
2 0
5 3,4 -> 2
3 



over take?
1 2 5 3 7 8 6 4
1 2 3 4 5 6 7 8
0 0 
    Y 1           1
      Y 1 2 3 4   5
        Y         6
          Y       7    


# All you need to do is to count the number of people who overtake a person.
"""
def min_b(q):
    count = 0    
    # Loop through each person in the q from 1 to len(q)
    for i in range(1,len(q)):        
        person = q[i-1]
        if person - i > 2:
            print('Too chaotic')
            return
        # how many people are in front
        # one position in front of p's original position
        # to one in front of p's current position
        # how many times has a p recieved a bribe to move back
        for j in range(i,min(i+person,len(q))):
            if person > q[j]:
                count+=1
                #print(person,q[j],count)
    print(count)

def minimumBribes(Q):
    #
    # initialize the number of moves
    moves = 0 
    #
    # decrease Q by 1 to make index-matching more intuitive
    # so that our values go from 0 to N-1, just like our
    # indices.  (Not necessary but makes it easier to
    # understand.)
    Q = [P-1 for P in Q]
    #
    # Loop through each person (P) in the queue (Q)
    for i,P in enumerate(Q):
        # i is the current position of P, while P is the
        # original position of P.
        #
        # First check if any P is more than two ahead of 
        # its original position
        if P-1 - i > 2:
            print("Too chaotic")
            return
        #
        # From here on out, we don't care if P has moved
        # forwards, it is better to count how many times
        # P has RECEIVED a bribe, by looking at who is
        # ahead of P.  P's original position is the value
        # of P.
        # Anyone who bribed P cannot get to higher than
        # one position in front if P's original position,
        # so we need to look from one position in front
        # of P's original position to one in front of P's
        # current position, and see how many of those 
        # positions in Q contain a number large than P.
        # In other words we will look from P-1 to i-1,
        # which in Python is range(P-1,i-1+1), or simply
        # range(P-1,i).  To make sure we don't try an
        # index less than zero, replace P-1 with
        # max(P-1,0)
        for j in range(max(P-1-1,0),i):
            if Q[j] > P-1:
                moves += 1
    print(moves-1)

def minimum_bribes(q):
    expected_position = 1
    count = 0
    for i in range(len(q)):        
        if q[i] > expected_position:
            hop = q[i]-expected_position
            if hop > 2:
                print('Too chaotic')
                return            
            else:                
                count += hop
        elif abs(q[i]-expected_position) > 2:            
            count+= 1
        expected_position +=1
    print(count)
    

if __name__ == '__main__':
   min_b([1, 2, 5, 3, 7, 8, 6, 4])
   """
    f = open('input1.txt','r')
    cases = int(f.readline())
   
    for i in range(cases):
        n = int(f.readline())
        q = list(map(int, f.readline().rstrip().split()))
    """
        
    
    

       
