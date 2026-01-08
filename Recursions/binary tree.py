class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Create binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


# In-order Traversal (Left → Root → Right)
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=' ')
        inorder_traversal(node.right)


# Pre-order Traversal (Root → Left → Right)
def preorder_traversal(node):
    if node:
        print(node.value, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)


# Post-order Traversal (Left → Right → Root)
def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=' ')


# Usage
print("In-order traversal:")
inorder_traversal(root)

print("\nPre-order traversal:")
preorder_traversal(root)

print("\nPost-order traversal:")
postorder_traversal(root)
