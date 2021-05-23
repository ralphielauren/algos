"""
BST = BT where for each Node:
 -> LEFT CHILD < NODE
 -> RIGHT CHILD > NODE

In Binary Tree, Inorder successor of a node is the next
node in Inorder traversal of the Binary Tree.
Inorder Successor is NULL for the last node in Inorder traversal.

Given a BST, and a reference to a Node x in the BST.
Find the Inorder Successor of the given node in the BST.
"""

"""
- Time Complexity:
- Space Complexity:

For node, if:
1. RIGHT subtree NOT NULL, successor in there.
   --> SUCCESSOR = Find min key val in right subtree.
2. RIGHT subtree IS NULL, successor in one of parents.
   --> SUCCESSOR = Climb up until Node is left child of parent, and that
   parent is the successor.
"""


class Node:
    def __init__(self, data: int):
        self.right = None
        self.left = None
        self.data = data
        self.parent = None


def successor(node: Node):

    if node.right is not None:
        return get_min(node.right)

    parent = node.parent
    while parent is not None:
        if parent.right != node:
            break
        node = parent  # climb up
        parent = node.parent
    return parent


def get_min(node: Node):

    current = node

    while current is not None:
        if current.left is None:
            break
        current = current.left

    return current


def insert(node: Node, data: int):

    if node is None:
        return Node(data)

    if data <= node.data:
        temp_node = insert(node.left, data)
        node.left = temp_node
        temp_node.parent = node

    else:
        temp_node = insert(node.right, data)
        node.right = temp_node
        temp_node.parent = node

    return node


if __name__ == "__main__":
    root = None
    root = insert(root, 35)
    root = insert(root, 10)
    root = insert(root, 45)
    root = insert(root, 5)
    root = insert(root, 14)
    root = insert(root, 7)
    root = insert(root, 16)

    t = root.left
    print(t.data)
    print(successor(t).data)
