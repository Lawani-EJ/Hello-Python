# PSEUDOCODE 
# Node {
#     data
#     left_child
#     right_child
# }

# Inserting a Node
# Insert(root, value):
#     if root is NULL:
#         root = new Node(value)
#         return
#     else:
#         Queue = empty queue
#         enqueue(root)

#         while Queue is not empty:
#             node = dequeue(Queue)

#             if node.left is NULL:
#                 node.left = new Node(value)
#                 return
#             else:
#                 enqueue(node.left)

#             if node.right is NULL:
#                 node.right = new Node(value)
#                 return
#             else:
#                 enqueue(node.right)
