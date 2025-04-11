'''
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

'''
def deleteMiddle(self,head):
    def deleteMiddle(self, head):
        ########################## My solution##################
        #Edge cases
        #if head is empty or has 1 element 
        if head is None or head.next is None:  #if not head or not head.next
            return head.next #return None


        # #create 3 pointers, slow and fast ,and 1 pointer behind slow to delete the middle node 
        slow = head.next
        fast = head.next.next
        behind_slow = head

        while fast is not None and fast.next is not None: #while fast and fast.next
            slow = slow.next
            behind_slow = behind_slow.next
            fast = fast.next.next

        #delete node 
        after_slow = slow.next 
        behind_slow.next = after_slow.next #behind_slow.next = slow.next

        return head 

        ########################## Another solution##################
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # delete the middle node
        prev.next = slow.next
        return head
    
        



