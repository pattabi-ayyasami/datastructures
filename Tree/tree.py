

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.value < node.value:
            # insert right
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            # insert left
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

# In Order Traversal: Left, Root, Right
def in_order_traversal(root, nodes):
    if root:
        in_order_traversal(root.left, nodes)
        nodes.append(root.value)
        in_order_traversal(root.right, nodes)

# Pre Order Traversal: Root, Left, Right
def pre_order_traversal(root, nodes):
    if root:
        nodes.append(root.value)
        pre_order_traversal(root.left, nodes)
        pre_order_traversal(root.right, nodes)

# Post Order Traversal: Left, Right, Root
def post_order_traversal(root, nodes):
    if root:
        post_order_traversal(root.left, nodes)
        post_order_traversal(root.right, nodes)
        nodes.append(root.value)
