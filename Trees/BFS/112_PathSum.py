'''
Question
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.


Steps - Attempt 
input: root, targetsum
output: True - if root to leaf = targetsum

1. if root is empty, return false 
2. start with root in queue 
3. pop from left of queue 
4. Add popped value to variable tracking current sum, currSum
5. check if currSum is == targetsum, and if left of poppedValue is none and if right of poppedValue is none,
if this is true, return True 
if false, add left of poppedValue  to queue, and add right of popped value to queue 
6. repeat steps 3 to 5


Revised steps
1. if root is empty, return false 
2. start with a queue contatining a tuple of (node,currentSum) - initially,(root,root.val). Initialize queue as [(root,root.val)]
3. pop from left of queue . while queue is not empty, pop(node,currentSum) from queue
4.if currSum == targetSum and not node.left and not node.right: return True
5. Otherwise, enqueue left and right children with updated sum
5. if queue is empty and didn't return, rteurn False 

'''
from collections import deque
class Solution(object):
    def hasPathSum(self, root, targetSum):
        #if root is empty, return false 
        if not root:
            return False 
        #start with a queue contatining a tuple of (node,currentSum) - initially,(root,root.val). Initialize queue as [(root,root.val)]
        queue = deque([(root,root.val)])

        #pop from left of queue . while queue is not empty, pop(node,currentSum) from queue
        while queue:
            node,currentSum = queue.popleft()
            #if currSum == targetSum and not node.left and not node.right: return True
            if currentSum == targetSum and not node.left and not node.right:
                return True
            #Otherwise, enqueue left and right children with updated sum
            if node.left:
                queue.append((node.left,currentSum +node.left.val ))
            if node.right:
                queue.append((node.right,currentSum+  node.right.val))

        #if queue is empty and didn't return, rteurn False 
        return False 
########################## Helper function to build tree ###############
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

######################### Run Code ##############
values = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22

root = build_tree_from_list(values)

sol = Solution()
print(sol.hasPathSum(root, targetSum))

        
