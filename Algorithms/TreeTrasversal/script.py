# Tree traversal also klown as tree search is the process of of visiting each node of a tree data structure.
# During tree trasversal, you visit each node of a tree exactly once and perform an operation on the nodes like checking the node data (search) or updating the node. 

# Tree trasversal algorithms can be classified broadly in the following two categories by the order in which the nodes are visited 

# Depth-first-search(DFS) Algorithm:
# It starts with the root node and first visits all nodes of one branch as deep as possible before backtracking, and visits all other branches in a similar fashion 

# Breadth-first-search(BFS) Algorithm:
# This also starts from the root node and visits all nodes of current depth before moving to the next depth in the tree 

# Types of  Tree Trasversal Algorithms 

# Pre-order traversal:
# In pre_order traversal it visits the root node first, then recursively visit left subtree and right subtree 

# In-Order traversal:
# Recursively visit the left subtree, visit the root node, and then recursively visit the right subtree 

# Post-Order traversal 
# Recursively visit the left subtree, recursively visit the right subtree, and then visit the root node. 

# example:
#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7

# Pre-order(Root, Left, Right): 1, 2, 4, 5, 3, 6, 7
# In-order(Left, Root, Right): 4, 2, 5, 1, 6, 3, 7 
# Post-order(Left, Right, Root): 4, 5, 2, 6, 7, 3, 1 

# PSEUDOCODE 

# PreOrder: 
# preOrder(node):
#     if node is not NULL:
#         visit(node)             Process the current node
#         preOrder(node.left)     Trasverse left subtree
#         preOrder(node.right)    Trasverse right subtree

# InOrder:
# InOrder(node):
#     if node is not NULL:
#         InOrder(node.left)        Trasverse left subtree
#         visit(node)               Process the current node
#         InOrder(node.right)       Trasverse right subtree

# PostOrder:
# PostOrder(node):
#     if node is not NULL:
#     PostOrder(node.left)            Trasverse left subtree
#     PostOrder(node.right)           Trasverse right subtree
#     visit(node)                     Process the current node

