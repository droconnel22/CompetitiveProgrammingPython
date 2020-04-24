
"""
Nested Lists

Given the names and grades for each student in a Physics clss of N students,
store them in a nested list and print the name of any student having the
second lowest grade.

If there are multiple students with the same grade, order their names
alphabetically and print each name on a new line.

Input Format
The first line contains an integer N the number of students
The 2N subsequent lines describe each student over 2 lines


Print the name(s) of any student(s) having
 the second lowest grade in Physics;
  if there are multiple students, order their
   names alphabetically and print each one on a new line.

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

"""




if __name__ == '__main__':
    f = open('input3.txt','r')
    n = int(f.readline())
    list = []
    for i in range(1,n*2,2):
      name = f.readline().split("\n")[0]
      grade = float(f.readline())
      temp = [name,grade]
      list.append(temp)
    result = sorted(list,key = lambda x: (x[1],x[0]))
    print(result)
    start_index = 1
    while result[0][1] == result[start_index][1]:
        start_index+=1
    
    capture_index = start_index
    while capture_index < len(result) and result[start_index][1] == result[capture_index][1]:
        print(result[capture_index][0])
        capture_index+=1
   This was a nasty problem, and another reminder of why other platforms are better. Here is my verbose cose, I don't believe in code golf.  

This could be much better performance, but the fustration on this one depreciated my motivation.


    
    




   