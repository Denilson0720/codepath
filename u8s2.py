print('UNIT 8 SESSION 2 PROBLEMS')
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    if root is None:
        return None
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root is None:
        return None
    if root:
        print(root.val)
        inorder_traversal(root.left)
        inorder_traversal(root.right)

def postorder_traversal(root):
    if root is None:
        return None
    if root:
        inorder_traversal(root.left)
        inorder_traversal(root.right)
        print(root.val)
'''
Problem 1: Is Uni-valued
A binary tree is uni-valued if every node in the tree has the same value. Given the root of a binary tree, return True if the given tree is uni-valued and False otherwise.

Evaluate the time complexity of your solution.

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def is_univalued(root):
	pass
Example Usage:

Example Input Tree #1

      1
     / \
    /   \
   1     1
  / \     \
 1   1     1

Input: root = 1
Expected Output: True

Example Input Tree #2

      1
     / \
    /   \
   1     2
  / \     \
 1   1     1

Input: root = 1
Expected Output: False
UNDERSTAND
    what methods do we have available to us to visit each node and find out their values?
        -dfs
            preorder root,left,right
            inorder left,root,right
            postorder left,right,root
        -bfs
    what does it mean to be univalued?
    what can be our base case?
        what can we say its purpose is for?
            -were trying to reach the base case where root is None, and we return True, if something stops us return False
    what is our recursive case?
        -what traversal can we do here?
PLAN
    pick any of the depth first search approahces, inorder
    compare if root.left and root.right are the same as current root
    if not return false
IMPLEMENT
'''

def is_univalued(root):
    if root is None:
        return True
    if root.left and root.left.val!=root.val:
        return False
    if root.right and root.right.val!=root.val:
        return False
    return is_univalued(root.left) and is_univalued(root.right)
#time complexity: O(n) - > we are visiting eveyr single node, operations depends on number of nodes in tree
#     1
#    / \
#   2   3 
root = TreeNode(1,TreeNode(2),TreeNode(3))
print(is_univalued(root))
print('END OF QUESTION 1')
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
  what is being reffered to by height?
    -the number of edges between the root node and the deepest child node
  is there an inbuilt method that can we use here?
  what traversal can we use here that can be helpful to us?
  will a recursion or iterative method work best?
PLAN 
  RECURSIVE
  travel down left and right subtree
  increase counter by 1 for every level we go down
  return max for every subtree we go down
IMPLEMENT
'''
def height(root):
  # Base case: if the root is None, the height is -1 (since there are no edges)
  if root is None:
      return -1

  # Recursively find the height of the left and right subtrees
  left_height = height(root.left)
  right_height = height(root.right)

  # The height of the tree is the maximum height of the subtrees plus one for the root
  return max(left_height, right_height) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(6)
print(height(root))
print('END OF QUESTION 2')
'''
Problem 3: BST Insert
Given the root of a binary search tree, insert a new node with a given key and value into the tree. Return the root of the modified tree. The tree is sorted by key. If a node with the given key already exists, update the the existing key’s value. You do not need to maintain a balanced tree.

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
  what order do BSTs have?
  how can recursion help us here?
  what value are we going to change if any? key or value
  base cases?
    root is None
    if node key valready exists in tree, update value
  what can we take advtange of given its a BST?
    if our key is greater than or less than to a current node key, we can go either down the left or right subtree
PLAN
  RECURSION
  MAKE CONDITIONAL CHECKS USING KEY
  if root is None, make new Node, return Node(meaning tree is empty)
  if key < root: GO DOWN LEFT SUBTREE(BECUASE BST ORDER)
    recursively go down the left side, insert(root.left,key,value)
    root.left = insert(root.left,key,value)
  elif key > root: GO DOWN RIGHT SUBTREE
    recursively go down the right subtree, insert(root.right,key,value)
    root.right = insert(root.right,key,value)
  # return root
  else: 
    weve reached our insert spot
    root.val = value
  return root
  
IMPLEMENT
'''
class TreeNode():
   def __init__(self, key, value, left=None, right=None):
       self.key = key
       self.val = value
       self.left = left
       self.right = right
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
# traverse_inorder(node_1)
print('--')
insert(node_1,10,'meow')
# traverse_inorder(node_1)
# traverse_inorder(node_1)
print('END OF QUESTION 3')
'''
Problem 4: BST Remove I
Use the provided pseudocode to solve the problem below. Given a key and the root of a binary search tree, remove the node with the given key. Return the root of the modified tree.

The tree is sorted by key. If multiple nodes with the given key exist, remove the first node you find. If you need to remove a node with two children, use the in-order successor of that node, which is the smallest value in its right subtree. You do not need to maintain a balanced tree.

Evaluate the time complexity of your function.

class TreeNode():
     def __init__(self, key, value, left=None, right=None):
         self.key = key
         self.val = value
         self.left = left
         self.right = right

def remove_bst(root, key):
  # Locate the node to be removed
  # If the node is a leaf node:
    # Remove the node by redirecting the appropriate child reference of its parent to None
  # If the node has one parent:
    # Replace the node with its child, updating its parent's nodes child reference appropriately
  # If the node has two children:
    # Find the node's inorder successor (smallest node in right subtree)
    # Swap the value of the node and its inorder successor
    # Recursively remove the successor (which now has the current node's value)
  # Return the root of the updated tree
  pass

Example Usage:

Example Input Tree #1: (tree depicted using keys) 

      10
     /  \
    /    \
   5      15
  / \     / \
 1   8   13  16


Input: root = 10, key = 10
Expected Output: 13
Expected Output Tree:

      13
     /  \
    /    \
   5      15
  / \       \
 1   8      16


Example Input Tree #2: (tree depicted using keys)

      10
     /  \
    /    \
   5      15
  / \     / \
 1   8   13  16
      \
       9 

Input: root = 10, key = 8
Expected Output: 10 (Should return a node object)
Expected Output Tree

      10
     /  \
    /    \
   5      15
  / \     / \
 1   9  13  16


Example Input Tree #3: (tree depicted using keys)

      10
     /  \
    /    \
   5      15
  / \     / \
 1   8   13  16
      \
       9 

Input: root = 10, key = 9
Expected Output: 10 (Should return a node object)
Expected Output Tree

      10
     /  \
    /    \
   5      15
  / \     / \
 1   8  13  16
UNDERSTAND
  what are we tasked to do, what value are we supposed to look for?
  what node should replace our removed node?
    -if we take a good look at our examples we should notice that when we have     two children, the inorder successor that would replace that node is also       the min node for its right subtree.
    -look for min to replace in case of two children nodes
  what can we take advantage of?
  base cases?
PLAN
  follow psuedo code
  def remove_bst(root, key):
    # Locate the node to be removed
    # If the node is a leaf node:
      # Remove the node by redirecting the appropriate child reference of its parent to None
    # If the node has one parent:
      # Replace the node with its child, updating its parent's nodes child reference appropriately
    # If the node has two children:
      # Find the node's inorder successor (smallest node in right subtree)
      # Swap the value of the node and its inorder successor
      # Recursively remove the successor (which now has the current node's value)
    # Return the root of the updated tree
IMPLEMENT
  
'''
class TreeNode:
  def __init__(self, key=0, value=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def find_min(node):
  # Helper function to find the minimum value node in a BST
  while node.left:
      node = node.left
  return node

def remove_bst(root, key):
  if root is None:
      return root

  # Locate the node to be removed
  if key < root.key:
    # go left subtree
      root.left = remove_bst(root.left, key)
  elif key > root.key:
    # go right subtree
      root.right = remove_bst(root.right, key)
  else:
       # Node to be removed found

      # If the node is a leaf node (no children)
      # make itself None
      if root.left is None and root.right is None:
          root = None

      # If the node has only one child, make either existing child values its own value
      elif root.left is None:
          root = root.right
      elif root.right is None:
          root = root.left

      # If the node has two children
      else:
          # Find the node's inorder successor (smallest node in right subtree)
          temp = find_min(root.right)
          # Swap the value of the node and its inorder successor
          root.key = temp.key
          root.val = temp.val
          # Recursively remove the successor (which now has the current node's value)
          # use remove_bst to remove temp.key as we have swapped it
          root.right = remove_bst(root.right, temp.key)
  return root
node_1 = TreeNode(10,10)
node_2 = TreeNode(8,8)
node_3 = TreeNode(15,15)
node_1.left = node_2
node_1.right =node_3
node_4 = TreeNode(1,1)
node_5 = TreeNode(6,6)
node_2.left = node_4
node_2.right = node_5

inorder_traversal(node_1)
print('removing')

new_tree = remove_bst(node_1,15)
inorder_traversal(new_tree)
# traverse_inorder(node_1)
print('END OF QUESTION 4')
'''
Problem 5: BST In-order Successor
In the remove_bst() problem, we summarized the in-order successor of a given node as the smallest node in the given node’s right subtree. This is true if the given node has a right subtree.

More generally, the in-order successor is the node with the smallest key greater than the key of the given node. Given the root of a binary search tree, and a TreeNode current, write a function that returns the in-order successor of the current node. Assume the tree is balanced.

Evaluate the time complexity of your solution.

class TreeNode():
      def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.val = value
            self.left = left
            self.right = right

def inorder_successor(root, current):
      pass
      
Example Input Tree #1: (tree depicted using keys)

          10
         /  \
        /    \
       5      15
      / \    
     1   8
        / \
       6   9

Input: root = 10, current = 5
Expected Output: 6 (Should return a node object)

Example Input Tree #2: (tree depicted using keys)

          10
         /  \
        /    \
       5      15
      / \    
     1   8
        / \
       6   9 
inorder - 1,5,6,8,9,10,15

Input: root = 10, current = 6
Expected Output: 8 (Should return a node object)
UNDERSTAND
  -can we reuse code from the previous problem?
  -in the previous problem we looked for min, which gave us the inorder           succesor, would this be enough?
PLAN
  if node has right subtree, successor is left most of that subtree
  if noe right subtree, one of parent nodes
IMPLEMENTATION
        10
       /  \
      5    15
     / 
    1   
    inorder succesor of 5 is 10
'''

def inorder_successor(root, node):
  # IF node has a right subtree
  if node.right:
      # The successor is the leftmost node of the right subtree
      return find_min(node.right)
  # IF we dont have a right subtree well have to return the root, so traberse up
  # Traverse up the parent nodes
  # successor set to none where we will only change it if we go left
  successor = None
  while root:
      #we go left, reassign succesor to root
      if node.val < root.val:
          successor = root
          root = root.left
      # we cannot go into the right subtree, it cant be there so we dont move succesor
      elif node.val > root.val:
          root = root.right
      # we have found the node, so break out of loop
      else:
          break
  return successor

def find_min(node):
  while node.left:
      node = node.left
  return node   
# traverse_inorder(node_1)
print(inorder_successor(node_1,node_2))
