'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

'''
def leafSimilar(root1,root2):
    out1 = []
    if not root1: #if root is none
        return
    if not root1.left and not root1.right: #if leaf node
        out1.append(root1.val)
    leafSimilar(root1.left)
    leafSimilar(root1.right)

    out2 = []
    if not root2: #if root is none
        return
    if not root2.left and not root2.right: #if leaf node
        out2.append(root2.val)
    leafSimilar(root2.left)
    leafSimilar(root2.right)

    return out1 == out2