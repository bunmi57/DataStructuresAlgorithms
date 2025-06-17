'''
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
'''

##########################Define the TreeNode Class ########################
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

##########################Helper to build a tree from a list  ########################
from collections import deque

def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root
##########################Sum root Solution ########################
class Solution(object):
    def sumNumbers(self, root):
        my_string = []

        def dfs(node):
            if not node: #if none 
                return 0
            
            my_string.append(str(node.val))

            #Add each node from root to leaf in a string
            if node.left == None and node.right == None:
                string = "".join(my_string)
                #pop last item 
                my_string.pop()
                int_string = int(string)
                return int_string
    
            #traverse left and right 
            left = dfs(node.left)
            right = dfs(node.right)

            my_string.pop() #backtrack          

            return left + right 


        return dfs(root) #Function call to run dfs

     

##########################Function Call ########################

# Input:root = [1,2,3,4,5,6,7,8,9]
#Output: 1026 (495 + 491 + 40)
#Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
root1_list = [1,2,3,4,5,6,7,8,9]

root1 = build_tree(root1_list)

sol = Solution()
#choose any node and a direction 
print(sol.sumNumbers(root1))


