"""
You are given a pointer to the root of a binary search tree and 
values to be inserted into the tree. Insert the values into their 
appropriate position in the binary search tree and return the root 
of the updated binary tree.

# e.g. [ 4,2,7,1,3]
if root = None -> ADD NODE
else check where to add value:
   - if value <= current node key --> [Add to left] --> iif left exists: traverse 1 down (make left local root)
                                                    --> else ADD NODE on left
       
   - if value > current node key --> [Add to right] --> SAME LOGIC AS ABOVE for right
"""

class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        
    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return 
        
        local_root = self.root  # might need to traverse to leaf if children exist
        while True:
            # left
            if val < local_root.info:
                if local_root.left:
                    local_root = local_root.left
                else:
                    local_root.left = Node(val)
                    break
            # right
            elif val > local_root.info:
                if local_root.right:
                    local_root = local_root.right
                else:
                    local_root.right = Node(val)
                    break

arr = [ 4, 2, 3, 1, 7, 6]

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
