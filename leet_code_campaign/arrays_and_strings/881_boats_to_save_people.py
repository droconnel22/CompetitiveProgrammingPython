 """

 881. Boats to Save People

 The i-th person has weight people[i],
 and each boat
 can carry a max weight of limit

 Each boat carriers at most 2 people at the same time
 provided the sum of the weight of those people is at most
 limit.

 Return the minimum number of boats to carry every given person.
 (it is guaranteed each person can be carried by a boat.)

 Return the min number of boats to carry every given person.

 Example 1:
 Input 
 people = [1,2]
 limit = 3
 Explanation: 1 boat (1,2)

 Example 2:
  Input people = [3,2,2,1]
  limit = 3
  Output = 3
  Explanation 3 boats (1,2) (3) (2)

  Example 3:
  Input 
  people = [3,5,3,4]
  limit =5 
  Output: 4
  Explanation: 4 boast (3),(3),(4),(5)

  Example 4:
  people [1,2,3,4,5] limit: 5

  2,3
  1,4
  5

  3 boats

  5,4,3,2,1

  Example 5:

  [3,3,4,4,5,5]  limit 10

  [5,5,4,4,3,3]
  5,3 - 8
  5,3 - 8
  5,4 - 9
  5,4 - 9
  5-5 10 
 [5,4,4,3,3]
 5,4

 [4,3,3]
10

Example 6:

Recall max is two
[1,1,1,1,1,1]
limit 1 -> len(peeps)
limit 2 -> len(peeps)/2
limit 3 -> len(peeps)/
2 people per boat boats
4,3

3

  1 <= people.length <= 50,000
  1 <= people[i] <= limit <= 30,000

  Amazon | FactSet

  Two pointers, Greedy

  Maximize the number of peeps 
  of people whose weights can be added together

  1. Sort the Array
  2. Attempt to add the heavy and lightest person
  3. 2 pointsers to 
    - left at beginning
    - right at the end of the array
    - boats number variable
  4. Loop as long the right is bigger then or
  equal then the left pointer


 """


class Solution:
    
    # O (N log(N))
    # S (1)
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        low = 0
        
        sorted_people = sorted(people,reverse=True)
        boat_count = 0
        #print(sorted_people)
        while low < len(sorted_people) and sorted_people[low] >= limit:
            boat_count+=1
            low+=1
        if low == len(sorted_people):
            return boat_count

        high = len(sorted_people)-1
        while low <= high:
            if low == high:
                boat_count+=1
                break

            weight = abs(sorted_people[low] + sorted_people[high])
            if weight <= limit:
                low+=1
                high-=1
                boat_count+=1
            else:
                low+=1
                boat_count+=1
            
            
        
        return boat_count
        


if __name__ == "__main__":
    pass


