print('UNIT 9 SESSINO 1 PROBLEMS')
class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
'''
Problem 1: Is Symmetric Tree
Given the root of a binary tree, return True if the tree’s left and right subtrees are mirrors of each other
 (i.e., tree is symmetric around its center). Return False otherwise.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
	pass

Example Usage:

Example Tree #1:

       1
     /   \
    /     \
   2       2
  / \     / \
 3   4   4   3
           |
 

Input: root = 1
Expected Output: True


Example Tree #2:

        1
      /   \
     /     \
    2       2
     \       \
      3       3
         

Input: root = 1
Expected Output: False
UNDERSTAND
    does not have to be a balanced tree
    it is not a BST tree
    imagining a mirror directly in the middle of the tree
PLAN


    METHOD 1, using list helper function
        save INORDER traversal of both left and right subtrees in lists
        compare lists
        if left list == right list backwards


    METHOD 2,using recursive helper function
        if root is None:
            return True
        helper functino(left,right):
            use helper function to test compare the left and right subtrees
            compare innner and outer values of the subtree
            our main objective is to get to the base case where our we go past the leaf nodes and return True
            if anything stops us, false
            base cases, trying to get to leaf nodes, what stops us?:
                if left and right are None:
                    return True
                if left or right are None:
                    return False
                if left!=right:
                    return False
                # compare innner and outer nodes
                return helper(left.left,right.right) and helper(left.right,right.left)  
'''
# METHOD 1
def inorder_traversal(node):
    lst =[]
    def traversal(node):
        if not node:
            return None
        if node:
            traversal(node.left)
            lst.append(node.val)
            traversal(node.right)
    traversal(node)
    return lst
def is_symmetric(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    left_inorder = inorder_traversal(root.left)
    right_inorder = inorder_traversal(root.right)
    return left_inorder == right_inorder[::-1]
one  = TreeNode(1)
l_two = TreeNode(2)
r_two = TreeNode(2)
l_three = TreeNode(3)
l_four = TreeNode(4)
r_three = TreeNode(3)
r_four = TreeNode(4)
one.left = l_two
one.right = r_two
l_two.left = l_three
l_two.right = l_four
r_two.left = r_four
r_two.right = r_three
# print(inorder_traversal(one))
print(is_symmetric(one))
# METHOD 2
def is_mirror(left,right):
    # weve passed leaf nodes
    if not left and not right:
        return True
    # one subtree is missing
    if not left or not right:
        return False
    # not symmetric
    if left.val!=right.val:
        return False
    # compare outer and innner nodes of subtrees
    return is_mirror(left.left,right.right) and is_mirror(left.right,right.left)
def is_symmetric_2(root):
    if not root:
        return True
    return is_mirror(root.left,root.right)
print(is_symmetric_2(one))
print('END OF QUESTION 1')
'''
Problem 2: Root-to-Leaf Paths
Given the root of a binary tree, return a list of all root-to-leaf paths in any order.

A leaf is a node with no children.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def binary_tree_paths(root):
	pass

Example Usage:

Example Input Tree #1:

  1
 / \
2   3
 \  
  5         

Example Input: root = 1
Expected Output: ["1->2->5", "1->3"]
["1->3", "1->2->5"] is also valid

Example Input Tree #2:

  1    

Example Input: root = 1
Expected Output: ["1"]
UNDERSTAND
    paths do not have to be given in any order
    must return list
    leaf node is a node with no children
PLAN   
    using a helper function, apply DFS on tree and have it append a path(string) to a paths list
    helper function(root,path,paths):
        if not root:
            return
        if path:
            # concatinate with new node
            path += str(node.val)
        else:
            start makig the path
            path = str(node.val)
        if root is leaf: left and right are None
            paths.append(path)
        else: 
            helper(root.left,path,paths)
            helper(root.right,path,paths)
            
        
    def binary_tree_paths(root):
        paths = []
        if not root:
            return []
        helper(root,[],paths)

'''
def helper(node,path,paths):
    if not node:
        return 
    if path:
        # if we have a path already started
        # concatinate to it the new node value
        path += ' -> ' + str(node.val)
    else:
        # start the path
        path = str(node.val)
    # if our node
    if not node.left and not node.right:
        paths.append(path)
    else:
        helper(node.left,path,paths)
        helper(node.right,path,paths)

def binary_tree_paths(root):
    paths = []
    if not root:
        return []
    helper(root,'',paths)
    return paths
'''
  1
 / \
2   3
 \  
  5      
'''
one  = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
five = TreeNode(5)
one.left = two
one.right = three
two.right = five
print(binary_tree_paths(one))
print('END OF QUESTION 2')
'''
Problem 3: Minimum Difference in BST
Given the root of a binary search tree, return the minimum difference between the values of any two different nodes in the tree.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_diff_in_bst(root):
	pass

Example Usage:

Example Input Tree #1:

    4
   / \
  2   6
 / \  
1   3

Example Input: root = 4
Expected Output: 1 
Explanation: The smallest difference between any two nodes is 1 (2 - 1 = 1, 3 - 2 = 1)

Example Input Tree  #2: 

   1
  / \
 0  48
    / \  
   12 49

Example Input: root = 1
Expected Output: 1 
Explanation: The smallest difference between any two nodes is 1 (1 - 0 = 1)
UDNERSTAND
    no duplicates, because BST
    the two ndoes can be anywhere
    root cannot be none because question guarantees leaf nodes, has to have leaf nodes
    what traversal method can help us here?
        what order does inorder traversal return?
PLAN
    use a helper function that returns a list of inorder traversal of the node values
    loop through list to find min difference of consecutive elements
IMPLEMENT
'''
def inorder_traversal_list(root):
    lst = []
    def list_maker(root):
        if not root:
            return None
        if root:
            list_maker(root.left)
            lst.append(root.val)
            list_maker(root.right)
    list_maker(root)
    return lst
def min_diff_in_bst(root):
    lst = inorder_traversal_list(root)
    print(lst)
    min_diff = float('inf')
    for i in range(1,len(lst)):
        diff = lst[i] - lst[i-1]
        # print(diff)
        if diff<min_diff:
            min_diff = diff
    return min_diff
'''
    4
   / \
  2   6
 / \  
1   3
'''
four = TreeNode(4)
two = TreeNode(2)
six = TreeNode(6)
one = TreeNode(1)
three = TreeNode(3)
four.left = two
four.right = six
two.left = one
two.right = three
print(min_diff_in_bst(four))
print('END OF QUESTION 3')
'''
Problem 4: Increasing Order Search Tree
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node of the tree is now the root of tree and every node has no left child and only one right child.

Return the root of the modified tree

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def increasing_bst(root):
	pass

Example Usage:

Example Input Tree #1:

    5
   / \
  1   7


Example Input: root = 5
Expected Output: root = 1

Expected Output Tree #1:

1 
 \
  5
   \
    7


Example Input Tree #2:

       5
      / \
     /   \
    3     6
   / \     \  
  2   4     8
 /         / \
1         7   9

Input: root = 5
Expected Output: root = 1
Expected Output Tree #2:

1
 \
  2
   \
    3
     \
      4
       \
        5 
         \
          6
           \
            7
             \
              8
               \ 
                9
UNDERSTAND
    what pattern can we recognize here?
    what traversal method can help us here to set the nodes in the desired manner?
    what if our root has no leaf nodes?
PLAN
    aquire the inorder traversal as a list of the BST
    make a new root using the first index of the list
    traverse the list and add to the right subtree each list element value
    return root
IMPLEMENT
'''
def inorder_traversal_list(root):
    lst = []
    def list_maker(root):
        if not root:
            return None
        if root:
            list_maker(root.left)
            lst.append(root.val)
            list_maker(root.right)
    list_maker(root)
    return lst
def increasing_bst(root):
    lst = inorder_traversal_list(root)
    new_root = TreeNode(lst[0])
    curr = new_root
    # for node_value in range(1,len(lst)):
    for node_value in lst[1:]:
        curr.right = TreeNode(node_value)
        curr = curr.right
    return new_root
'''
   5
   / \
  1   7
'''
five = TreeNode(5)
one = TreeNode(1)
seven = TreeNode(7)
five.left = one
five.right = seven
new_list = increasing_bst(five)
def print_list(root):
    curr = root
    while curr:
        print(curr.val)
        curr = curr.right
print_list(new_list)
print(inorder_traversal_list(new_list))
print('END OF QUESITON 4')
'''
Problem 5: Equal Tree Split
Given the root of a binary tree, return True if removing an edge between two nodes can split the tree into two trees with an equal number of nodes. Return False otherwise.

Evaluate the time complexity of the function.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def can_split(root):
	pass

Example Usage:

Example Input Tree #1:

       1
      / \
     /   \
    2     3
   / \     \  
  4   5     7

Example Input: root = 1
Expected Output: True
Explanation: Deleting the edge between node 1 and its left child, node 2 gives the following
two trees, each of size 3

  Tree 1    Tree 2        
              1
               \
    2           3
   / \           \  
  4   5           7



Example Input Tree #2:

       1
      /  \
     /    \
    2      3
   / \    / \  
  4   5  6   7

Example Input: root = 1
Expected Output: False
Explanation: It is not possible to split the tree into two trees of equal size by deleting 
an edge
UNDERSTAND
    what information is important to us?
    do we care about the tree being balanced?
    do we care about the node values?
PLAN
    using a helper function, find the total number of nodes in the tree
    return True if even, False if odd
IMPLEMENT
'''
def count_nodes(root):
    if not root:
        return 0
    return 1+count_nodes(root.left)+count_nodes(root.right)
def can_split(root):
    count = count_nodes(root)
    return count%2==0
#       1
#      / \
#     /   \
#    2     3
#   / \     \  
#  4   5     7
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
print(can_split(root))
#       1
#      / \
#     /   \
#    2     3
#   / \   / \  
#  4   5 6   7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(can_split(root))
