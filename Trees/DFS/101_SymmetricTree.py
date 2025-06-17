'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
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
# ########################## Symmetric Tree Solution ########################
# class Solution(object):
#     def isSymmetric(self, root):
#         tree_list = []
       
#         def dfs(node):
#             #base case
#             if not node:
#                 return    
#             #condition

#             #recurse tree
#             dfs(node.left)
#             tree_list.append(node.val)
#             dfs(node.right)
#             #use left and right soln 
#             return tree_list

#         returned_tree_list = dfs(root)
#         #split list into 2
#         length = len(returned_tree_list)
#         return tree_list[0:(length//2 + 1)]  == tree_list[:-1-((length//2 + 1)):-1]

# ########################## Symmetric Tree Solution using a helper function ########################
class Solution(object):
    def isSymmetric(self,root):
        def isMirror(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (
                t1.val == t2.val and 
                isMirror(t1.left,t2.right) and
                isMirror (t1.right,t2.left)
            )
        
        return isMirror(root.left,root.right)



        

     

##########################Function Call ########################


# root1_list = [1,2,2,3,4,4,3]
# root2_list = [1,2,2,3,4,4,3,5,6,]
root2_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

root1 = build_tree(root2_list)

sol = Solution()
#choose any node and a direction 
print(sol.isSymmetric(root1))

