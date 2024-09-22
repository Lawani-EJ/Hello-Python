# PSEUDOCODE
# search (value, root)
# {
#     if(root == null ){
#         # Empty
#         # Not found return null 
#     }
#     if(root.data == value){
#         # Found 
#         return root
#     }
#     if(root.data > value){
#         return search(value,root.left)
#     }
#     if(root.data  < value){
#         return search(value,root.right)
#     }
# }

# class Node:
#     def__init__(self,data):
#          self.data = data
#         self.children = []


# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.parent = None

#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent

#         return level

#     def print_tree(self):
#         spaces = ' ' * self.get_level() * 3
#         prefix = spaces + "|__" if self.parent else ""
#         print(prefix + self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_tree()

#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)

# def build_product_tree():
#     root = TreeNode("Electronics")

#     laptop = TreeNode("Laptop")
#     laptop.add_child(TreeNode("Mac"))
#     laptop.add_child(TreeNode("Surface"))
#     laptop.add_child(TreeNode("Thinkpad"))

#     cellphone = TreeNode("Cell Phone")
#     cellphone.add_child(TreeNode("iPhone"))
#     cellphone.add_child(TreeNode("Google Pixel"))
#     cellphone.add_child(TreeNode("Vivo"))

#     tv = TreeNode("TV")
#     tv.add_child(TreeNode("Samsung"))
#     tv.add_child(TreeNode("LG"))

#     root.add_child(laptop)
#     root.add_child(cellphone)
#     root.add_child(tv)

#     root.print_tree()

# if __name__ == '__main__':
#     build_product_tree()

from collections import deque

def addEdge(x, y, adj):
    adj[x].append(y)
    adj[y].append(x)

def printParents(node, adj, parent):
    if parent == 0:
        print(f"{node}->Root")
    else:
        print(f"{node}->{parent}")

    for cur in adj[node]:
        if cur != parent:
            printParents(cur, adj, node)

def printChildren(Root, adj):
    q = deque()
    q.append(Root)

    vis = [0] * len(adj)
    while q:
        node = q.popleft()
        vis[node] = 1
        print(f"{node}->", end="")
        for cur in adj[node]:
            if vis[cur] == 0:
                print(cur, end=" ")
                q.append(cur)
        print()  

def printLeafNodes(Root, adj):
    for i in range(1, len(adj)):
        if len(adj[i]) == 1 and i != Root:
            print(i, end=" ")

def printDegrees(Root, adj):
    for i in range(1, len(adj)):
        print(f"{i}: {len(adj[i])}")


N = 7
Root = 1

adj = [[] for _ in range(N + 1)]
addEdge(1, 2, adj)
addEdge(1, 3, adj)
addEdge(1, 4, adj)
addEdge(2, 5, adj)
addEdge(2, 6, adj)
addEdge(4, 7, adj)

print("The parents of each node are: ")
printParents(Root, adj, 0)

print("\nThe children of each node are: ")
printChildren(Root, adj)

print("\nThe leaf nodes are: ")
printLeafNodes(Root, adj)

print("\nThe degree of each node is: ")
printDegrees(Root, adj)
