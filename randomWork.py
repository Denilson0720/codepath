# return kth distinct string in a list of strings
def kth_distinct_string(lst,k):
    # make a frequency table
    freq ={}
    for str in lst:
        if str not in freq:
            freq[str]=1
        else:
            freq[str]+=1
    
    # as we iter trhough dict decrease k every time we find distinct until we hit 0 and return key
    '''
        for key,value in freq.items():
        if k == 0 and value == 1:
            return key
        elif value==1:
            k-=1
        return 'none'
    '''
    #BECAUSE DICTIONARY DOES NOT GUARANTEE AN ORDER OF ACCESS,INSTEAD we can iter through the list again and check their dict values from there
    #this guarantees we are checking the correct k index
    for str in lst:
        if freq[str]==1 and k==0:
            return str
        elif freq[str]==1:
            k-=1
    return 'none'

print(kth_distinct_string(['d','db','a','c'],2))
print(kth_distinct_string(['d','d','db','db'],3))
print(kth_distinct_string(['d','d','db','db'],1))
print(kth_distinct_string(['d','d','db','db'],2))
'''
Problem 2: Binary Tree Height
Given the root of a binary tree, write a function height() that returns the height of a binary tree.

Evaluate the time complexity of your function.

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
   
def height(root):
	pass
Example Usage:

Example Input Tree #1

      4
     / \
    /   \
   2     5
  / \    
 1   3    

Input: root = 4
Expected Output: 3

Example Input Tree #2 

      4 

Input: root = 4
Expected Output: 1
UNDERSTAND
    what is meant by height of a binary tree?
    recursively thinking, how far down the tree would we go? 

'''
def inorder_traversal(root):
    if root is None:
        return None
    if root:
        inorder_traversal(root.left)
        print(root.val)
        # print(root.key/)
        inorder_traversal(root.right)
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val =val
        self.left = left
        self.right = right

def levels(root):
    if not root:
        return 0
    
    left_height = levels(root.left)
    right_height = levels(root.right)

    return max(left_height,right_height)+1

one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
four.left = two
four.right= five
two.left = one
two.right = three
print(levels(four))
# inorder_traversal(four)
'''
Problem 3: BST Insert
Given the root of a binary search tree, insert a new node with a given key and value into the tree.
Return the root of the modified tree. The tree is sorted by key. If a node with the given key already exists, update the the existing key’s value. 
You do not need to maintain a balanced tree.

Evaluate the time complexity of your function.

class TreeNode():
     def __init__(self, key, value, left=None, right=None):
         self.key = key
         self.val = value
         self.left = left
         self.right = right

def insert(root, key, value):
  pass
Example Usage:

Example Input Tree #1: (tree depicted using keys)

      10
     /  \
    /    \
   8      15
  / \    
 1   6    

Input: root = 10, key = 9, value = 'Naruto' 
Expected Output: root = 10
Expected Output Tree:

      10
     /  \
    /    \
   8      15
  / \    
 1   6
      \
       9    


Example Input Tree #2: Empty Tree (None)

Input: root = None, key = 4, value = "Sailor Moon"
Expected Output: root = 4
Expected Output Tree:

      4
UNDERSTAND
    what are some things to point out?
        we do not need to maintain a balanced tree
        IT IS a binary search tree, we need to maintain BST ORDER where root.left<root and root.right>root
    are we comparing keys or values?
        keys are being checked, we do not want to have multiple nodes with the same key but instead update their value
    how cna we find a leaf node?
    do we have to check every single node?
        yes
PLAN
    checkk if the subtree does not already have a node with the given key:
        go down a subtree till we find a leaf node
        make its child node the new key, value node
    if we find the key already existent, update the value
'''
print('_________')
class TreeNode:
    def __init__(self,key,val,left = None,right= None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
def insert(root,key,value):
    if not root:
        return None
    if root.key == key:
        root.value = value
        return 
    insert(root.left)
    insert(root.right)

def insert(root,key,value):
  # base case, weve reached an empty desired spot
  # or....our tree is empty 
  if root is None:
    return TreeNode(key,value)
  # if keys match, update value
  if root.key == key:
    root.value = value
    # return
  elif key < root.key:
    # send down the left rabbit hole 
    root.left = insert(root.left,key,value)
  elif key>root.key:
    # send down the right rabbit hole
    root.right = insert(root.right,key,value)
  else:
    root.val= value
  return root
'''
      10
    /    \
    8    15
  /  \
  1  6
'''
node_1 = TreeNode(10,'a')
node_2 = TreeNode(8,'b')
node_3 = TreeNode(15,'c')
node_1.left = node_2
node_1.right =node_3
node_4 = TreeNode(1,'d')
node_5 = TreeNode(6,'e')
node_2.left = node_4
node_2.right = node_5
# inorder_traversal(node_1)
naruto = TreeNode(9,'naruto')
new = insert(node_1,9,'naruto')
inorder_traversal(new)
