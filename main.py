#from Sorting import inseration_sort, merge_sort
from BTrees.Nodes import Node
from random import *
#print(inseration_sort.inseration_sort([1,2,4,6]))

#my_list =[23,56,23,44,22,7,9,2,4,5,6,78,99]

#print(inseration_sort.inseration_sort(my_list))

#print(merge_sort.sort(my_list))
foo = Node(5)

for i in range(20):
    val = randint(1,20)
    foo.insert(val)

foo.inOrder()
#print('pre order')
#foo.preOrder()
#print('post order')
#foo.postOrder()

print(foo.find(5))
mys = randint(1,20)
print(foo.find(mys),mys)

result = foo.findNode(mys)
if result is not None:
    print(result.Data)   
    print(foo.delete(mys,foo).Data)
    foo.inOrder()
