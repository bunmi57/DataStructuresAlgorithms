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
########################## Symmetric Tree Solution ########################
class Solution(object):
    def isSymmetric(self, root):
        tree_list = []
       
        def dfs(node):
            #base case
            if not node:
                return    
            #condition

            #recurse tree
            dfs(node.left)
            tree_list.append(node.val)
            dfs(node.right)
            #use left and right soln 
            return tree_list

        returned_tree_list = dfs(root)
        #split list into 2
        length = len(returned_tree_list)
        return tree_list[0:(length//2 + 1)]  == tree_list[:-1-((length//2 + 1)):-1]




        

     

##########################Function Call ########################


# root1_list = [1,2,2,3,4,4,3]
# root2_list = [1,2,2,3,4,4,3,5,6,]
root2_list = [1,2,2,3,4,4,3]

root1 = build_tree(root2_list)

sol = Solution()
#choose any node and a direction 
print(sol.isSymmetric(root1))

# test = [3, 2, 4, 1, 4, 2, 3]
# leng = len(test)
# print("length =", leng)
# print("0:3", test[0:(leng//2 + 1)])
# print("6:3", test[(leng-1):(leng//2)])
# print(test[:-1-((leng//2 + 1)):-1])