'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Examples:

Input: s = "()"  Output: true
Input: s = "()[]{}" Output: true
Input: s = "(]" Output: false
Input: s = "([])" Output: true

Steps
1. initiliaze open parentheses, close parentheses, matched parentheses,stack
2. If the len of input is odd, return false
3. Iterate through the string
4. when an open bracket is seen, add it to the stack
5. When a close bracket is seen, pop off the last open parenthese from the stack
    If the stack is empty, it means we encountered a closing bracket without a matching opening bracket, so return False.
6. check if the popped off element(open parenthese) is a match with the closed parenthese 
    return Trur or false if it is a match or it isn't
5. If a match, repeat steps 2-4
6. if stack is not empty, it means there are open parentheses, that haven't been closed so return False
'''
# def validParentheses(s):
#     #initiliaze open parentheses, close, match,stack
#     open_parentheses =  ['(', '[', '{']
#     close_parentheses =  [')', ']', '}']
#     match_parentheses =  ('()'),('[]'),('{}')
#     stack = []
    
#     #if the len of input is odd, return false
#     if len(s)%2 != 0: 
#         return False
    
#     #Iterate through the string
#     for paran in s:
#         #when an open bracket is seen, add it to the stack
#         if paran in open_parentheses:
#             stack.append(paran)
#         #when a close bracket is seen, pop off the lase open parenthese from the stack
#         else:
#             # If the stack is empty, it means we encountered a closing bracket without a matching opening bracket, so return False.
#             if len(stack) == 0:
#                 return False
#             else:
#                 popped_element = stack.pop() #removes last open parentheses from the stack
#             #check if the popped off element(open parenthese) is a match with the closed parenthese 
#             possible_parentheses = popped_element + paran #concantenate open and closed parentheses 
#             if possible_parentheses not in match_parentheses:
#                 return False
#     #if stack is not empty, it means there are open parentheses that haven't been closed so return False
#     return len(stack) == 0

# s = '[' #False
# s = '()[]{}' #True
# s = '(]' #False
# s = '([])' #True
# s = '()' #True
# s = '([{}])' #True
s = '([{[])' #False
# print(validParentheses(s))
#---------------------------------------------------------------------------------------------------------------------------------
#Another solution using dictionary

def validParentheses(s):
    #initiliaze open parentheses, close, match,stack
    paren_dict =  {'(':')','[':']','{':'}'}
    stack = []
    
    #if the len of input is odd, return false
    if len(s)%2 != 0: 
        return False
    
    #Iterate through the string
    for paran in s:
        #when an open bracket is seen, add it to the stack
        if paran in paren_dict.keys():#in automatically searches through the keys
            stack.append(paran)
        #when a close bracket is seen, pop off the lase open parenthese from the stack
        else:
            # If the stack is empty, it means we encountered a closing bracket without a matching opening bracket, so return False.
            if len(stack) == 0: #if not stack
                return False
            else:
                popped_element = stack.pop() #removes last open parentheses from the stack
            #check if the popped off element(open parenthese) is a match with the closed parenthese      
            if paran != paren_dict[popped_element]:
                return False
    #if stack is not empty, it means there are open parentheses that haven't been closed so return False
    return len(stack) == 0 #return not stack 
