from Tree.TreeNode import TreeNode


class BinaryTree:
    def __init__(self, node):
        self.root = node

    # display needs BFS or DFS
    def display(self):
        index = self.root
        while index is not None:
            print(index.value)


'''4 becomes left child of 2 
           1 
       /       \ 
      2          3 
    /   \       /  \ 
   4    None  None  None 
  /  \ 
None None'''
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
myTree = BinaryTree(node1)
node1.left = node2
node1.right = node3
node2.left = node4
