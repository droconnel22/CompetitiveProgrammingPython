"""
1029. Two City Scheduling

There are 2*N people a company is planning to interview.

The cost of lfying the i-th person to a city A is 
costs[i][0] 
and the cost of flying the i-th person to city B is
costs[i][1]

Return the minmum cost to fly every person to a city
such that exactly N people arrive in each city.

costs[candidate][city a cost][city b cost]

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110

The first person goest ot city A for a cost fo 10
The second person goes to city A for a cost of 30
the third persoon goes to city B for a cost 50
the fourth person goes to city B for a cost of 20

(what if the costs are the same?)
input is 1,2,3,4 (is that 2*N so N per city or two per city)

total minimum cost is

(10+30) + (50+20) = 110

It is guaranteed the costs length is even
Values are always positive.
"""

class Solution:
    def twoCitySchedCost(self,costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        ~i
        # Returns the complement of x - the number you get by switching 
        # each 1 for a 0 and each 0 for a 1.  is the same as -x - 1.
        a = 50
        print(a,~a)

        b = 10
        print(b,~b)

        trip_cost = 0
        costs.sort(key=lambda cost:(cost[0]-cost[1]))

        # The trip where you save the least needs to be paired with the
        # trip where you save the most.        
        for i in range(len(costs)>>1):
            tilda_i = -1*(i+1)
            print(tilda_i,~i)
            trip_cost += costs[i][0] + costs[tilda_i][1]
        return trip_cost


    
        


if __name__ == "__main__":
    s = Solution()
    r = s.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])
    print(r)