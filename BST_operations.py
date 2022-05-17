
INT_MIN=-float('inf')
INT_MAX=float('inf')

class Node:

    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        

def preorder_bst_iter(self, a, size):
  
   root = Node(a[0])
   s = []
   s.append(root)
   i = 1
   while i < size:
      temp = None
      while (len(s) > 0 and a[i] > s[-1].value):
          temp = s.pop()

      if temp != None:
          temp.right = Node(a[i])
          s.append(temp.right)

      else:
          temp = s[-1]
          temp.left = Node(a[i])
          s.append(temp.left)
      i=i+1

    return root
      

def min(root):
    if root == None:
        return "Tree is empty"
    while root.left != None:
        root = root.left
    return root.value

def max(root):
    if root == None:
        return "Tree is empty"
    while root.right != None:
        root = root.right
    return root.value

def deletion (root, value):
  
    if root == None:
        print("Node not present in the tree")
        return root
    if value < root.value:
        root.left = deletion(root.left,value)
    elif value > root.value:
        root.right = deletion(root.right,value)
    else:
        if root.right is None:
            temp = root.left
            return temp
        elif root.left is None:
            temp = root.right
            return temp
        succ_parent = root
        succ = root.right

        while succ.left:
            succ_parent = succ
            succ = succ.left

        if succ_parent == root:
            succ_parent.right = succ.right
        else:
            succ_parent.left = succ.right

        root.value = succ.value
        return root

    return root




def inorder(root):
        if root:
            inorder (root.left)
            print (root.value)
            inorder (root.right)
        return

def preorder(root):
    if root:
        print (root.value)
        preorder (root.left)
        preorder (root.right)
    return

def postorder(root):
    if root:
        postorder (root.left)
        postorder (root.right)
        print (root.value)
    return

def search_key_iter (root,value):
  
    while root:
        if value == root.value:
            return True
        if value > root.value:
            root = root.right
        else:
            root = root.left
    return False


def search_key_rec(root, value):
  
    if root == None:
        return False
    if root.value == value:
        return True
    else:
        if value > root.value:
            return search_key_rec(root.right, value)

        return search_key_rec(root.left, value)


def insert_recur(root,value):
   
    if root == None:
        return Node(value)
    else:
        if root.value == value:
            return root
        if value > root.value:
            root.right = insert_recur(root.right,value)
        else:
            root.left = insert_recur(root.left,value)

    return root
















