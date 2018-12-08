# Bus Stops

* https://www.hackerrank.com/contests/101hack54/challenges/bus-stops

There are  bus stops on the street. You can imagine the street as a line with the coordinate system. The coordinates of the bus stops are , where  is the distance in meters from the  bus stop to the beginning of the street. The first bus stop is located at the beginning of the street and the last is located at the end of the street.

image

There is exactly one bus route. A bus goes from the beginning to the end of the street every  minutes with speed  meters per minute, starting at time . A bus stops at each stop. Stopping takes no time.

There are  people who want to reach the end of the street. The  person starts at point  at time  and has walking speed  meters per minute. For each person, you should find the minimum time when this person can reach the end of the street.

Complete the function minimumTimeToEnd that takes in the array  of coordinates of the bus stops and three integers ,  and  (the meanings of which are explained in the statement) and prints  real numbers, the  of which denotes the minimum time when the  person can reach the end of the street. The description of the people should be taken from the standard input as described in the input format section.

Input Format

The first line contains a single integer .

The second line contains  space-separated integers .

The third line contains two space-separated integers  and .

The fourth line contains a single integer .

The next  lines contain the description of people. The  of these lines contains three space-separated integers , , .