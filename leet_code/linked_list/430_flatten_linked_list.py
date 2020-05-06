"""
430. Flatten a Multilevel Doubly Linked List

You are given a doubly linked list which
in addition to the next and previous
pointers,it could have a child poniter,
which may or may not point to a separate
doubly linked list

These child lists may have one or more children
of thair own, and so on, to produce a multilevel
data structure, as shown in the example below.

[Linked List, Depth First Search]

> Flatten the list so that all the nodes appear in a single-level
doubly linked list.

You are given the head of the first level of the list.


Node:
    Node next;
    Node previous;
    Node child;


Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

"""

class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child



class Solution:

    def __init__(self):
        self.head = None

    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return
        origin = head
        node = head
        while node:
            if node.child:
                child = node.child
                while child.next:
                    child = child.next
                child.next = node.next
                node.next = node.child
                node.next.prev = node
                node.child = None
            node = node.next
        return origin




        

    def create_linked_list(self,parent, values):
        index = 0
        node_list = []
        node = None
        while index <len(values) and values[index] is not None :
            value = values[index]
            next_node = Node(value)
            node_list.append(next_node)
            if node is None:     
                if self.head is None:
                    self.head = next_node
                if parent and parent.child is None:
                    #print('child', parent.val)
                    parent.child = next_node  
                node = next_node
            else:
                node.next = next_node
                next_node.prev = node
                node = next_node
            index+=1
        parent_index = 0
        while index < len(values) and values[index] is None:
            parent_index+=1 
            index+=1      
        #print([n.val for n in node_list])
        if index < len(values):           
            #print([v for v in values[index:]])
            self.create_linked_list(node_list[parent_index-1],values[index:])

                   
    def print_node(self,head):
        if head is not None:
            node = head
            while node is not None:
                print(node.val,end=" ")
                self.print_node(node.child)
                node = node.next

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12]
    s = Solution()
    s.create_linked_list(s.head,arr)
    s.print_node(s.head)
    print("\n----\n")
    moap = s.flatten(s.head)
    while moap:
        print(moap.val,end=" ")
        moap = moap.next
    #s.print_node(s.head)f