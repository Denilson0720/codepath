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
'''
Problem 6: In-order Traversal
Given the root of a binary tree, return a list representing the inorder traversal of its nodes' values. In an inorder traversal we traverse the left subtree, then the current node, then the right subtree.

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def inorder_traversal(root):
	pass

Example Usage:

Example Input Tree #1: 
     1
      \
       2
      / 
     3    

Input: root = 1
Expected Output: [1,3,2]

Example Input Tree #2 : 

Input: root = None
Output: []

Example Input Tree #3:
    1  

Input: root = 1
Output: [1]
UNDERSTAND
    what is inorder traversal?
        left root right
    what is our base case, when do we stop going down our tree?
    what can we do to add to a list but make sure it doesnt get overwritten with every recursive step?
PLAN
    parent function(node):
    lst = []
        child_function(): the one that does the traversal and adds to lst
            if not node:
                return None
            if node:
                inorder(left)
                lst.append(node.val)
                inorder(right)

'''
def inorder_traversal(root):
    lst = []
    def traversal(root):
        if not root:
            return None
        if root:
            traversal(root.left)
            # print(root.val)
            lst.append(root.val)
            traversal(root.right)
    traversal(root)
    return lst
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)

one.right = two
two.left = three
print(inorder_traversal(one))
print('END OF QUESTION 6')
'''
Problem 7: Binary Tree Size
Given the root of a binary tree, write a function size() that returns the number of nodes in the binary tree.

Evaluate the time complexity of your function.

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def size(root):
	pass

Example Usage:

Example Input Tree #1: 

      4
     / \
    /   \
   2     5
  / \    
 1   3    

Input: root = 4
Expected Output: 5

Example Input Tree #2: 

Empty tree (None)
Input: root = None
Expected Output: 0
UNDERSTAND
    what question is similar to this one?
    do we have to visit every single node?
    would it be helpful to have a helper function?
        -have a sum to add to within scope?
PLAN
    parent function(root):
        sum = 0
        helper(root): the one that does traversala and adds to sum
            if not Node:
                return 0
            if Node:
                helper(root.left)
                sum+=1
                helper(root.right)
        return sum
IMPLEMENT
'''
# print(size(one))
def size(root):
    if not root:
        return 0
    return 1 + size(root.left) + size(root.right)
print(size(one))
print('END OF QUESITON 7')
'''
Problem 8: Binary Tree Find
Given a value and the root of a tree, write a function find() that returns True if there is a node with the given value in the tree. Assume the tree is balanced.

Evaluate the time complexity of your solution.

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def find(root, value):
	pass

Example Input Tree #1: 

      1
     / \
    /   \
   2     5
  / \    
 4   3    

Input: root = 1, value = 5
Expected Output: True

Example Input Tree #2: 

      1
     / \
    /   \
   2     5
  / \    
 4   3    

Input: root = 1, value = 10
Expected Output: False
UNDERSTAND
    do we have to visit every node?
    base case?
        if root.val = key:
            return True
        else root.left==None and root.right ==None:
            return False
    recursive case?
        return left and right traversal
IMPLEMENT
'''

def find(root,value):
    if root is None:
        return False
    if root.val == value:
        return True
    print(root.val)
    # if root.left == None and root.right== None:
        # return False
    # we use or instead of and because we just care if the value is found anywhere in the tree
    # if we used and then it would need to be found in the left and right subtree to return True, which is wrong
    return find(root.left,value) or find(root.right,value)

'''
      1
     / \
    /   \
   2     5
  / \    
 4   3   
'''
class TreeNode:
    def __init__(self,val,left =None,right = None):
        self.val =val
        self.right = right
        self.left = left
    
one = TreeNode(1)
two = TreeNode(2)
four = TreeNode(4)
three = TreeNode(3)
five = TreeNode(5)
one.left = two
one.right = five
two.left = four
two.right = three
# print('meow')
print(inorder_traversal(one))
print(find(one,4))
print('END OF QUESTION 8')
'''
Problem 9: Binary Search Tree Find
Given a value and the root of a binary search tree,
 write a function find_bst() that returns True if there is a node with the given value in the tree.
Assume the tree is balanced.

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def find_bst(root, value):
	pass


# Example Input Tree #1: 

      4
     / \
    /   \
   2     5
  / \    
 1   3    

Input: root = 4, value = 5
Expected Output: True

Example Input Tree #2: 

      4
     / \
    /   \
   2     5
  / \    
 1   3    

Input: root = 4, value = 10
Expected Output: False
UNDERSTAND
    what are the characterisitcs of a bst tree?
    do we HAVE to look at every single node in the tree?
        -no since it is a bst it is ordered in such a way that we ignore specific branches
PLAN
    base case:
        if we reach an None: 
            return False
        if we find the node:
            return True
        if value>root.val:
            return root.right
        if value<root.val:
            return root.left
'''
def bst_find(root,value):
    if root is None:
        return False
    if root.val == value:
        return True
    if value>root.val:
        return bst_find(root.right,value)
    else:
        return bst_find(root.left,value)
'''
      4
     / \
    /   \
   2     5
  / \    
 1   3    
'''
one = TreeNode(1)
two = TreeNode(2)
four = TreeNode(4)
three = TreeNode(3)
five = TreeNode(5)
four.left = two
four.right = five
two.left = one
two.right = three
print(inorder_traversal(four))
print(bst_find(four,5))
print(bst_find(four,1))
print(bst_find(four,6))
print('END OF QUESTION 9')
'''
Problem 10: BST Descending Leaves
Given the root of a binary search tree, write a function descending_leaves() that returns a list of the values of all leaves in the BST in descending order. Assume the tree is balanced.

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def descending_leaves(root):
	pass

Example Input Tree #1: 

      4
     / \
    /   \
   2     5
  / \    
 1   3    

Input: root = 4
Expected Output: [5, 3, 1]

Example Input Tree #2: 
 10 

Input: root = 4
Expected Output: [10]
UNDERSTAND
    how can we gather all node values?
    what can we do to return a list of the values in descedngins order?
PLAN
    make a list of ndoe values in inorder traversal order
    return the list sorted backwards
IMPLEMENT
'''
def descending_leaves(root):
    lst = []
    def helper(root):
        if root is None:
            return None
        if root:
            helper(root.left)
            lst.append(root.val)
            helper(root.right)
    helper(root)
    return lst[::-1]
one = TreeNode(1)
two = TreeNode(2)
four = TreeNode(4)
three = TreeNode(3)
five = TreeNode(5)
four.left = two
four.right = five
two.left = one
two.right = three
print(inorder_traversal(four))
print(descending_leaves(four))
print('END OF QUESTION 10')