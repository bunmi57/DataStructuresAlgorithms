'''
'''

class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None
        self.right = None

class BinarySearchTree:
    #initializing a binary search tree
    def __init__(self):
        self.root = None
    #BST insert 
    def BST_insert(self,value):
        #create a new node
        new_node = Node(value)

        #edge case, if root is none, root becomes the new node
        if self.root == None:#if self.root is None
            self.root = new_node
            return True
        temp = self.root #declare variable
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: #if new node is > temp
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right
    def max_sum(self):
        current_node = self.root
        #queue to keep track of nodes in BST
        queue = []
        max_level = 1
        present_sum = current_node.value
        print("initial sum:",present_sum)
        max_sum = present_sum
        level = 1

        queue.append(current_node)
        print("Queue before while loop:",queue)
        while len(queue)>0:
            level += 1
            level_size = len(queue)
            present_sum = 0
            #iterate through the values in a level
            for i in range(level_size):

                current_node = queue.pop(0)
                    
                if current_node.left is not None:
                    queue.append(current_node.left)
                    present_sum += current_node.left.value
                    print(f"left - present sum {present_sum} at level {level}")
                
                if current_node.right is not None:
                    queue.append(current_node.right)
                    present_sum += current_node.right.value
                    print(f"right -present sum {present_sum} at level {level}")

                if i == level_size - 1: #reached the last node
                    if present_sum > max_sum:
                        max_level = level
                        max_sum = present_sum
                        print(f"at level: {max_level} maxsum:{max_sum}")

        return max_level


            







#create an instance of a BST
my_tree = BinarySearchTree()

print(my_tree.BST_insert(1))
print(my_tree.BST_insert(7))
print(my_tree.BST_insert(0))
print(my_tree.BST_insert(7))
print(my_tree.BST_insert(-8))
print(my_tree.BST_insert(0))
print(my_tree.BST_insert(0))
#[1,7,0,7,-8,null,null]

print(my_tree.max_sum())
# print('Root:',my_tree.root.value) #41
# print('Root -> Left:', my_tree.root.left.value) #21
# print('Root -> Right:', my_tree.root.right.value) #76
# print('Root -> Left -> Left:', my_tree.root.left.left.value) #18
# print('Root -> Left -> Right:', my_tree.root.left.right.value) #27
# print('Root -> Right -> Left:', my_tree.root.right.left.value) #52
# print('Root -> Right -> Right:', my_tree.root.right.right.value) #82
