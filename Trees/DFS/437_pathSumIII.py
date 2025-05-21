'''
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

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

##########################Path sum iii Solution ########################
class Solution(object):
    def pathSum(self,root,targetSum):
        return self.findSum(root,targetSum)
        
    #Try each node as a starting point  
     #This is a helper function - passes a node as the start position, traverse through the tree from
     #this start position and check is sum is = target sum
    def findSum(self,node,targetSum):
       if not node:
           return 0
       

       # Count paths starting from this node
       first = self.dfs(node,targetSum)
       # Recur for left and right subtrees
       left = self.findSum(node.left,targetSum)
       right = self.findSum(node.right,targetSum)
       return first + left + right

    # Count paths that start at this node and go downward
    def dfs(self,new,targetSum,curr_sum=0):
        if not new:
            return 0

        curr_sum += new.val
        print('curr_sum = ',curr_sum)
        if curr_sum == targetSum:
            this_node = 1
        else:
            this_node = 0
        
        #recurse through left and right node
        left_count = self.dfs(new.left,targetSum,curr_sum)
        right_count = self.dfs(new.right,targetSum,curr_sum)
        
        return this_node + left_count + right_count

'''
 Notes
 1. think of a recursive function as soln at one level where you have a node, a left and right
 2. then the return statement is what you need at that level
 3. remember the result gets bubbled up to next level up
 4. when a return statement is called,the function that called it is popped off the stack and the return value is returned
 Ultimately, think of solns as what do i need at the higher level(root), how do i recurse the lower levels to get the result at the highest level
 
 
'''   
        



##########################Function Call ########################

root1_list = [10,5,-3,3,2,0,11,3,-2,0,1]
targetSum = 8

root1 = build_tree(root1_list)

sol = Solution()
print(sol.pathSum(root1,targetSum))