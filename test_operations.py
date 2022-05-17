from BST_operations import *

#Input the tree in a preorder traversal format
a = [7,5,3,2,4,6,12,8,13]

root = preorder_bst_iter(a, len(a))
print("Preorder traversal")
preorder(root)

#insert a new node into the tree
insert_recur(root,9)
print("Postorder traversal")
postorder(root)

#Delete a node from the tree
deletion(root,5)
print("Preorder traversal")
preorder(root)

#Delete another node from the tree
deletion(root,6)
print("Postorder traversal")
postorder(root)

#Delete another node not present in the tree
deletion(root,1)

#Print min and max element from the tree
print(min(root))
print(max(root))
