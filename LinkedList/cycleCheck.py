'''
Write a function that takes in the first node in a singly linked list
returns a boolean indicating if the linked list contains a cycle

Steps
1. 2 markers
2. traverse through list
3. marker 2 moves 2 nodes ahead of marker 1
4. if the linked list has a cycle, marker 2 will eventually lap marker 1 and they will equal each other
5. if the list has no cycle, marker 2 will continue on until the end,nebver equaling the first marker
'''

class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None
def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None: #while we haven't reached the tail for marker2, and aren't about to finish for marker2
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker2 == marker1:
            return True
    return False