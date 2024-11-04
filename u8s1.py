print('UNIT 8 SESSION 1 PROBLEMS')
'''
Problem 1: Build a Binary Tree I
Given the following TreeNode class, create the binary tree depicted in the image below.
        10
       /  \
      4    6
Binary Tree Example

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
UNDERSTAND
    what is a binary tree?
          10
        /    \
       4      2
      / \    
     1   2   
    what is a balnced binary tree?
    -refers to height of the longest path a node to the the bottom most leaf node 
    -for a tree to be balanced the difference of the left and right subtree must not be mroe than 1

    EXAMPLE OF NON BALANCED BUNARY TREE
                          10    height: 3
                        /    \
             height:2  4      2    height : 0
                    / \    
         height:0  1   2   height:0
        left subtree height: 2
        right subtree height:0
        2-0 = 0... not balanced
    what is the difference between a binary tree and a binary search tree?
PLAN
   using the TreeNode class make an object of such, assign TreeNode objects for left and right parameters 
IMPLEMENT
'''
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(10,TreeNode(4),TreeNode(6))
print('root: ', root.val)
print('left node: ',root.left.val)
print('right node: ',root.right.val)
print('END OF QUESTION 1')
'''
Problem 2: 3-Node Sum I
Given the root of a binary tree that has exactly 3 nodes: the root, its left child, and its right child, return True if the value of the root is equal to the sum of the values of its two children. Return False otherwise.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
	pass

Example Usage:

Example Input Tree #1: 
  10
 /  \
4    6
Input: root = 10
Expected Output: True

Example Input Tree #2: 
  5
 / \
3   1
Input: root = 5
Expected Output: False
UNDERSTAND
    how can access the values of our nodes?
    what are we guaranteed about the binary tree?
PLAN
    compare the root.val and root.left and root.right values
IMPLEMENT
'''
def check_tree(root):
    # ternary operators:
    # True if condition else False
    return True if root.val==(root.left.val+root.right.val) else False
root = TreeNode(10,TreeNode(4),TreeNode(6))
root2 = TreeNode(5,TreeNode(3),TreeNode(1))
print(check_tree(root))
print(check_tree(root2))
# time complextiy: O(1) -> we know we only have 3 nodes and so we check them directly in constant time
print('END OF QUESTION 2')
'''
Problem 3: 3-Node Sum II
Given the root of a binary tree that has at most 3 nodes: 
the root, its left child, and its right child,
return True if the value of the root is equal to the sum of the values of its two children. Return False otherwise.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
	pass

Example Usage:

Example Input Tree #1: 
  10
 /  
10    
Input: root = 10
Expected Output: True

Example Input Tree #2: 
  5
 / \
3   2
Input: root = 5
Expected Output: True

Example Input Tree #3: 
  5
   \
    2
Input: root = 5
Expected Output: False

Example Input Tree #4: 
Empty Tree (None)
Input: root = None
Expected Output: False
UNDERSTAND
    this question IS NOT the same as the previous
    what is the key difference? "at most 3 nodes"
    are we guaranteed 3 nodes? root, left and right?
PLAN
    sum = 0
    conditinoally check it the root has left and right child nodes, add them to sum
    compare sum to root.val
IMPLEMENT
'''
def check_tree_2(root):
    sum = 0
    if root.left:
        sum+=root.left.val
    if root.right:
        sum+=root.right.val
    return True if sum==root.val else False
#     10
#   /   \
#  10
root_1 = TreeNode(10,TreeNode(10))
#     5
#   /  \
#  3   2
root_2 = TreeNode(5,TreeNode(3),TreeNode(2))
#    5
#     \
#      2
root_3 = TreeNode(5,None,TreeNode(2))
print(check_tree_2(root_1))
print(check_tree_2(root_2))
print(check_tree_2(root_3))
# print(root_3.val,root_3.left,root_3.right.val)
# time complextiy: O(1) -> constant time, we are checking directly, the left and right nodes
print('END OF QUESTION 3')
'''
Problem 4: Find Leftmost Node I
Given the root of a binary tree, write a function that finds the value of the left most node in the tree.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
	pass

Example Usage:


Example Input Tree #1: 

      1
     / \
    /   \
   2     5
  / \    
 4   3    

Input: root = 1
Expected Output: 4

Example Input Tree #2: 

     1
      \
       2
      / 
     3    

Input: root = 1
Expected Output: 1

Example Input Tree #3: 

Input: root = None
Output: None
UNDERSTAND
    what does leftmost node mean?
    how do we access this leftmost node?
PLAN
    make a pointer to keep track of locatino in binary tree
    while root.left
        pointer = root.left
    return pointer.val
IMPLEMENT
'''
def left_most(root):
    if root is None:
        return None
    curr = root
    while curr.left:
        curr = curr.left
    return 4
#      1
#     / \
#    2   5
#  / \
# 4   3
# root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(3)),TreeNode(5))
one = TreeNode(1)
two = TreeNode(2)
five = TreeNode(5)
four = TreeNode(4)
three = TreeNode(3)
one.left = two
one.right = five
two.left = four
two.right = three
print(left_most(one))
# print(one.val)
# print('meow')
print('END OF QUESTION 4')
'''
Problem 5: Find Leftmost Node II
If you implemented the previous left_most() function iteratively, implement it recursively. If you implemented it recursively, implement it iteratively.

Evaluate the time complexity of the function.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
	pass
UNDERSTAND
    how can we think of this recursively?
    what will be our base case?
    what will be our recursive case?
    how can we think about our base case? what will it stop?
PLAN
    base case, to stop recursive steps down the tree:
    if node==None:
        return None
    if node.left==None:
        return Node
    check if node:
        left_most(node.left)
IMPLEMENT
'''
def left_most_recursively(root):
    if root is None:
        return None
    if root.left is None:
        return root.val
    return left_most_recursively(root.left)
one  = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
one.left = two
two.left = three
print(left_most_recursively(one))
print('END OF QUESTION 5')