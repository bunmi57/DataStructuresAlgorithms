'''
LL: Find Middle Node
Implement the find_middle_node method for the LinkedList class.

Note: this LinkedList implementation does not have a length member variable.

If the linked list has an even number of nodes,
return the first node of the second half of the list.

requirements:

1. The method should use a two-pointer approach,
where one pointer (slow) moves one node at a time 
and the other pointer (fast) moves two nodes at a time.

2. When the fast pointer reaches the end of the list 
or has no next node, the slow pointer should be at the middle node of the list.

3. The method should return the middle node
 when the number of nodes is odd or 
 the first node of the second half of the list if the list has an even number of nodes.

4. The method should only traverse the linked list once.  
In other words, you can only use one loop.



'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
        

    def find_middle_node(self):
        #Initialize 2 pointers at the head - fast and slow 
        slow = self.head
        fast = self.head

        #Iterate through the list until half of the length
        #slow poingter moves 2 nodes at a time, slow pointer moves 1 poinyter at a time
        for _ in range(self.length//2):
            fast = fast.next.next
            slow = slow.next
        return slow
    
    #SAlternstive soln if length is not known
    # def find_middle_node(self):
    #     slow = self.head
    #     fast = self.head

    #     while fast is not None and fast.next is not None:
    #         slow = slow.next
    #         fast = fast.next.next
    #     return slow 





my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(34)



print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""