'''
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.

'''

def removeStars(s):
    
    star = '*'
    my_list = []
    for element in s:
        #push each character onto the stack unless it's a star 
        if element != star:
            my_list.append(element)
        #if you encouter a stack, pop the top element from the stack 
        if element == star:
            my_list.pop()
    #convert to string
    stack_str = "".join(my_list)
    return stack_str


#optimized soln using deque
from collections import deque

def removeStars(s):
    stack = deque()  # Initialize a deque as the stack
    
    for element in s:
        if element == '*':
            stack.pop()  # Pop from the stack if a star is encountered
        else:
            stack.append(element)  # Push the character onto the stack
    
    return ''.join(stack)  # Convert the deque to a string and return it
print('Output:',removeStars("leet**cod*e"))
print('Output:',removeStars("erase*****"))  