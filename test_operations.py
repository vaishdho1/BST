from BST_operations import *

#Input the tree in a preorder traversal format
a = [7,5,3,2,4,6,12,8,13]

root = preorder_bst_iter(a, len(a))
print("Preorder traversal")
preorder(root)
'''
7
5
3
2
4
6
12
8
13
'''

#insert a new node into the tree
insert_recur(root,9)
print("Postorder traversal")
postorder(root)

'''
2
4
3
6
5
9
8
13
12
7
'''

#Delete a node from the tree
deletion(root,5)
print("Preorder traversal")
preorder(root)
'''
7
6
3
2
4
12
8
9
13
'''

#Delete another node from the tree
deletion(root,6)
print("Postorder traversal")
postorder(root) 
'''
2
4
3
9
8
13
12
7
'''

#Delete another node not present in the tree
deletion(root,1) #Could not find the elemnt

#Print min and max element from the tree
print(min(root)) #2
print(max(root)) #13

#search a given key recursively and iteratively
print(search_key_iter(root,2)) #True
print(search_key_rec(root,1)) #False
