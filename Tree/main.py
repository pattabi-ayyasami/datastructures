from tree import (
    TreeNode,
    insert, in_order_traversal,
    pre_order_traversal,
    post_order_traversal
)


def create_binary_search_tree():
    tree = TreeNode(10)
    insert(tree, TreeNode(20))
    insert(tree, TreeNode(30))
    insert(tree, TreeNode(40))
    insert(tree, TreeNode(50))
    insert(tree, TreeNode(60))
    insert(tree, TreeNode(70))
    return tree

def create_binary_tree():
    tree = TreeNode(10)
    tree.left = TreeNode(20)
    tree.right = TreeNode(30)
    tree.left.left = TreeNode(40)
    tree.left.right = TreeNode(50)
    left = TreeNode(60)
    tree.right.left = TreeNode(60)
    tree.right.right = TreeNode(70)

    tree.left.left.left = TreeNode(80)
    tree.right.right.right = TreeNode(90)

    return tree


def get_nodes_at_given_level(node, level, nodes):
    if node is None:
        return

    if level == 1:
        nodes.append(node.value)
    elif level > 1:
        get_nodes_at_given_level(node.left, level - 1, nodes)
        get_nodes_at_given_level(node.right, level - 1, nodes)


def height_of_tree(root):
    if root is None:
        return 0
    return 1 + max(height_of_tree(root.left), height_of_tree(root.right))


def size(root):
    if root is None:
        return 0
    return size(root.left) + size(root.right) + 1

def get_leaf_count(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return get_leaf_count(root.left) + get_leaf_count(root.right)


def bfs_traversal(root):
    print "================================================="
    print "BFS / Level Order Tree Traversal"
    print "================================================="
    max_width = 0
    max_width_level = 0
    height = height_of_tree(root)
    print "Height of the tree: %d" %height
    for level in range(height):
        nodes = []
        get_nodes_at_given_level(root, level+1, nodes)
        print "Nodes at level %d: %s" %(level+1, nodes)
        width = len(nodes)
        print "Width of the tree at level %d: %s" % (level + 1, width)
        if max_width < width:
            max_width = width
            max_width_level = level + 1
    print "Maximum width of the tree is %d and is at level %d" %(max_width, max_width_level)


def print_circular_link_list(head):
    if head is None:
        return

    current = head
    while True:
        print "Node %d" %(current.value)
        current = current.right
        if current == head:
            break

def concatenate_circular_dll(left_dll, right_dll):
    if left_dll is None:
        return right_dll
    if right_dll is None:
        return left_dll

    left_last = left_dll.left
    right_last = right_dll.left

    left_last.right = right_dll
    right_dll.left = left_last

    left_dll.left = right_last
    right_last.right = left_dll

    return left_dll


def convert_tree_to_circular_link_list(root):
    if root is None:
        return

    left = convert_tree_to_circular_link_list(root.left)
    right = convert_tree_to_circular_link_list(root.right)

    # Make the root as a single node circular link list
    root.left = root.right = root
    return concatenate_circular_dll(concatenate_circular_dll(left, root), right)


def path_to_leaf(node, path_list):
    if node is None:
        return None

    path_list.append(node.value)

    if node.left is None and node.right is None:
        # Leaf Node
        print path_list
    else:
        path_to_leaf(node.left, path_list[:])
        path_to_leaf(node.right, path_list[:])


def get_level(node, value, level):
    if node is None:
        return 0

    if node.value == value:
        return level

    matched_level = get_level(node.left, value, level + 1)
    if matched_level != 0:
        return matched_level

    matched_level = get_level(node.right, value, level + 1)
    return matched_level

def does_node_exist(root, value):
    if root is None:
        return False

    if root.value == value:
        return True

    node_exists = does_node_exist(root.left, value)
    if node_exists:
        return True

    node_exists = does_node_exist(root.right, value)
    return node_exists

def print_ancestors(root, value):
    if root is None:
        return False

    if root.value == value:
        return True

    if print_ancestors(root.left, value) or print_ancestors(root.right, value):
        print root.value
        return True

    return False

def main():
    print "Tree"
    #tree = create_binary_search_tree()
    tree = create_binary_tree()
    print "================================================="
    print "In-Order Tree Traversal (Left, Root, Right)"
    nodes = []
    in_order_traversal(tree, nodes)
    print nodes
    print "================================================="

    print "================================================="
    print "Pre-Order Tree Traversal (Root, Left, Right)"
    nodes = []
    pre_order_traversal(tree, nodes)
    print nodes
    print "================================================="

    print "================================================="
    print "Post-Order Tree Traversal (Left, Right, Root)"
    nodes = []
    post_order_traversal(tree, nodes)
    print nodes
    print "================================================="

    bfs_traversal(tree)


    print "================================================="
    tree_height = height_of_tree(tree)
    print "Height of the tree: %d" % tree_height
    print "================================================="

    print "================================================="
    print "Nodes at a given level: %d" %tree_height
    print "================================================="
    nodes = []
    get_nodes_at_given_level(tree, tree_height, nodes)
    print nodes

    print "================================================="
    size_of_tree = size(tree)
    print "# of nodes in tree: %d" %(size_of_tree)
    print "================================================="

    print "================================================="
    leaf_count = get_leaf_count(tree)
    print "Number of Leaf Nodes in the tree: %d" % (leaf_count)
    print "================================================="

    '''
    
    circular_link_list = convert_tree_to_circular_link_list(tree)
    print "================================================="
    print "Display Tree as a circular link list (In Order Traversal)"
    print "================================================="
    print_circular_link_list(circular_link_list)
    print circular_link_list.left.value
    print circular_link_list.left.right.value

    '''

    print "========================================================="
    print "Root to Leaf Path"
    path_to_leaf(tree, [])
    print "========================================================="

    print "========================================================="
    node_value = 20
    matched_level = get_level(tree, node_value, 1)
    if matched_level != 0:
        print "Node %d is at level %d" %(node_value, matched_level)
    else:
        print "Node %d not found in the tree" %node_value
    print "========================================================="

    print "========================================================="
    node_value = 70
    node_exists = does_node_exist(tree, node_value)
    if node_exists:
        print "Node %d exists in the tree" %node_value
    else:
        print "Node %d does not exist in the tree" %node_value

    print "========================================================="


    print "========================================================="
    node_value = 90
    print_ancestors(tree, node_value)
    print "========================================================="

if __name__ == "__main__":
    main()