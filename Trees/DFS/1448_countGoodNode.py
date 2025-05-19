'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

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

##########################count good node Solution ########################
class Solution(object):
    def goodNodes(self, root):
        if not root:
            return 0
        
        return self.findGoodNode(root,float('-inf'))
        
     #returns the count of good Node
    def findGoodNode(self,node,maxVal):
       
        if not node:
            return 0

        #finds the max value in curren path
        max_val = max(node.val,maxVal)
        print('node.val',node.val)
        if max_val == node.val:
            this_node = 1
        else:
            this_node = 0
        
        #recurse through left and right node
        left_count = self.findGoodNode(node.left,max_val)
        right_count = self.findGoodNode(node.right,max_val)
        
        return this_node + left_count + right_count

    
        



##########################Function Call ########################

# root1_list =[3,1,4,5,0,1,5]
root1_list =[3,1,4,5,0,2,6]

root1 = build_tree(root1_list)

sol = Solution()
print(sol.goodNodes(root1))