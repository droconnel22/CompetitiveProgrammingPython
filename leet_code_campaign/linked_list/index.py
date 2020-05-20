
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head= None

    def insert_node(self, node):
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next        
            temp.next = node

    def delete_node(self,node):
        if self.head:
            if self.head.data == node.data:
                self.head = self.head.next
            else:
                temp = self.head
                while temp.next and temp.next.data != node.data:
                    temp = temp.next
                
                # we want remove the next node
                to_remove = temp.next
                temp.next = temp.next.next


    
    
    def print_list(self):
        temp = self.head
        linked_list = []

        while(temp):
            linked_list.append(temp.data)
            temp = temp.next

        # string.join connects elements inside list of strings, not ints.
        print(" -> ".join(map(str,linked_list)))

ll = LinkedList()

second_node = Node(1)
third_node = Node(3)
fourth_node = Node(7)

ll.insert_node(Node(5))
ll.insert_node(second_node)
ll.insert_node(third_node)
ll.insert_node(fourth_node)
ll.print_list()
ll.delete_node(third_node)
ll.print_list()