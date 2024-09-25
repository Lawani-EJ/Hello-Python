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


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None


    def insert(self, data):
        new_node = Node(data)
        
        if self.root is None:
            self.root = new_node
            return


        queue = [self.root]
        
        while queue:
            current = queue.pop(0)


            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)


            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)


    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)


binary_tree = BinaryTree()
binary_tree.insert(1)
binary_tree.insert(2)
binary_tree.insert(3)
binary_tree.insert(4)
binary_tree.insert(5)

print("In-order Traversal: ")
binary_tree.in_order_traversal(binary_tree.root)
