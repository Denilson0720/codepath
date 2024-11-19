from collections import deque
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
        # print(root.val)
        print(root.key)
        inorder_traversal(root.right)
def inorder_traversal_by_value(root):
    if root is None:
        return None
    if root:
        inorder_traversal_by_value(root.left)
        print(root.val)
        inorder_traversal_by_value(root.right)
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
# testing myself

# understand
# univalued - all node have equal value
# i dont have to worry about it being nalanced or not
# plan
# base case covers
    # empty tree
    # once i go beyond a leaf node
# if node==None:
    # return True
# if node.left!=node:
    # return False
# if node.right!=node:
    # return False
# recursive case:
    # return uni(node.left) and uni(node.right)
def is_univalued(node):
    if node==None:
        return True
    if node.left and node.left.val!=node.val:
        return False
    if node.right and node.right.val!=node.val:
        return False
    return is_univalued(node.left) and is_univalued(node.right)
print('node_1 is: ', is_univalued(node_1))

# binary tree height

# understand
    # height is the amount of nodes from root and furtheset leaf node, bot inclusive of root and leaf
    # ill have to traverse all nodes, not really important, well see
    # will have to acount that left subtree and right subtree might not be the same height so will have to find the max between both
# plan  
    # go down each subtree adding 1 everytime we reach a new node
    # find max between left and right subtree
    # base case:
        # if Node==None:
            # return 0
    # left_height = height(left)
    # right_height = height(right)
    # recursive case:
        # return 1+ max(left, right )
# implement
def height(root):
    if root==None:
        return -1
    left_height = height(root.left)
    right_height = height(root.right)
    
    return 1+ max(left_height,right_height)
print('height is: ', height(node_1))


# bst insert
# def insert(root,key,value):
class TreeNode:
    def __init__(self,key,val,left=None,right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
'''
    10
   /  \
  5    11
/   \
2    6  
'''
ten=TreeNode(10,10)
five = TreeNode(5,5)
eleven = TreeNode(11,11)
two = TreeNode(2,2)
six = TreeNode(6,6)
ten.left = five
ten.right = eleven
five.left = two
five.right = six
print('inorder tree is: ')
print(inorder_traversal(ten))
# understand
    # tree is sorted by key, node has key,value
    # because it is a bst i dont need to visit every single node as i can conditionally traverse left or right subtree
    # two base cases: where do i stop traversing?
        # if root.key == key:
            # root.val = value
        # if root==None:
            # return Node(key,value)
    #recrusive steps
        # if root.key>key:
            # root.left = insert(root.left,key,value)
        #else , if root.key<key:
            # root.right = insert(root.right,key,value)
    # return Node(root,key,value)
# implement
def insert(root,key,value):
    # update value
    if root.key==key:
        root.val = value
    if root==None:
        return TreeNode(key,value)
    if root.key>key:
        # theres no way to assing a ndoe from bottom up so we go top to bottom assigning them
        root.left =insert(root.left,key,value)
    elif root.key<key:
        root.right = insert(root.right,key,value)
    # redudant but serves as fallback, since this was already taken care of in our first check
    # else:
        # return root
    return root
# print()
new_tree = insert(ten,11,'naruto')
inorder_traversal_by_value(new_tree)

print('next question, removal of bst:')
# removal of bst

'''
def remove_bst(root, key):
	# Locate the node to be removed
	# If the node is a leaf node:
		# Remove the node by redirecting the appropriate child reference of its parent to None
        # make node.child = None, by returning None
	# If the node has one parent:
		# Replace the node with its child, updating its parent's nodes child reference appropriately
	# If the node has two children:
		# Find the node's inorder successor (smallest node in right subtree)
		# Swap the value of the node and its inorder successor
		# Recursively remove the successor (which now has the current node's value)
	# Return the root of the updated tree
	pass
    
        10
       /  \
      5    15
     / \
    1   8
       /  \
       6   9
inorder traversal : 1,5,6,8,9,10,15

'''
ten = TreeNode(10,10)
five = TreeNode(5,5)
fifteen = TreeNode(15,15)
one  = TreeNode(1,1)
eight = TreeNode(8,8)
six = TreeNode(6,6)
nine  = TreeNode(9,9)
ten.left = five
ten.right = fifteen
five.left = one
five.right = eight
eight.left = six
eight.right = nine
inorder_traversal(ten)
# used to find inorder succesor,smallest ndoe in the right subtree
def find_min(node):
    current=node
    while current.left:
        current = current.left
    # return the whole node
    return current
def remove_bst(root,key):
    if root is None:
        return root
    # located the node
    if root.key<key:
        root.right = remove_bst(root.right,key)
    elif root.key>key:
        root.left = remove_bst(root.left,key)
    # found node to removed
    else:
        # if node is a leaf node
        if root.left is None and root.right is None:
            root = None
        # if node only has 1 child, two cases make either root.right or root.left is new value
            # if root.left is None, use root.rights value for the new root value
        elif root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        # if root has two child nodes
        else:
            #use the smallest node in the nodes right subtree as the new value for that node
            #remove the smallest node using remove_bst(root.right) from the right subtree
            # find min returns the ndoe as is, smallest key
            temp = find_min(root.right)
            root.key = temp.key
            root.val = temp.val
            # remove smallest node using remove_bst from right subtree
            root.right = remove_bst(root.right,temp.key)
    return root
print('removal, new tree: ')
new_tree = remove_bst(ten,8)
inorder_traversal(new_tree)
# inorder succesor using a given root but a a specific node current
# THIS SOLUTION ONLY TAKES INTO ACCOUNT IF THE NODE HAS A RIGHT SUBTREE
def inorder_succesor(root,current):
    if root is None:
        return None
    if current.right is None and current.left is None:
        return current
    #if left subtree is non existent
    if current.left is None:
        return current.right
      # find minimum of the right subtree of current
    temp = current.right
    while temp.left:
        temp = temp.left
    return temp
result = inorder_succesor(ten,five)
print(result.key)
print('----')
def print_rand(root):
    if root is None:
        return None
    # print(root.val)
    if root:
        print_rand(root.left)
        print(root.val)
        print_rand(root.right)

    # print_rand(root.left) and print_rand(root.right)
print_rand(ten)
def max_node(root):
    if root is None:
        return -9999
    max_left = max_node(root.left)
    max_right = max_node(root.right)

    return max(max_left,max_right,root.val)
print(max_node(ten))
print('LEVEL ORDER TRAVERSAL:')
# return a list of the level order traversal of a bst
def level_order_traversal(root):
    if not root:
        return []
    queue = deque()
    lst = []
    queue.append(root)
    while queue:
        node = queue.popleft()
        lst.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return lst
'''
        10
       /  \
      5    15
     / \
    1   8
       /  \
       6   9
inorder traversal : 1,5,6,8,9,10,15
level order: 10,5,15,1,8,6,9

'''
ten = TreeNode(10,10)
five = TreeNode(5,5)
fifteen = TreeNode(15,15)
one  = TreeNode(1,1)
eight = TreeNode(8,8)
six = TreeNode(6,6)
nine  = TreeNode(9,9)
ten.left = five
ten.right = fifteen
five.left = one
five.right = eight
eight.left = six
eight.right = nine
print(level_order_traversal(ten))
print('SHORTEST PATH QUESTION:')
'''
Problem 2: Find Minimum Depth of Binary Tree
Given the root of a binary tree, return its minimum depth. The minimum depth is the number of nodes along the shortest path from the root down to the nearest leaf node.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

def min_depth(root):
pass

Example Input Tree #1:

   3
  / \
 9  20
    / \  
   15  7
root = 3
output = 2 
-dont have to track the path itself
    -just return the number of nodes
    shortest = 1
    update accordingly
-traversal methods: BFS, DFS
    BFS would allow us to look at the tree on a level by level basis,meaning a leaf node would be picked up early wether or not its in the right or left subtree
PLAN
    if not root:
        return 0
    if not root.left or right:
        return 1
    using a queue that is goign to keep track of the level by level order of the binary tree
    the queue is going to hold tuples(node,depth) of each consequent node 
    node,depth = q.popleft()
    if we run into a leaf node, node.left and node.right ==None return depth
    if node.left:
        q.append(node.left)
    if node.right:
        q.append(ndoe.right)
    return -1, fallback


'''
def shortest_path_nodes(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    q = deque()
    q.append((root,1))
    while q:
        node,depth = q.popleft()
        # if we reach a leaf node
        if not node.left and not node.right:
            return depth
        if node.left:
            q.append((node.left,depth+1))
        if node.right:
            q.append((node.right,depth+1))
    return -1
print(shortest_path_nodes(ten))
root = TreeNode(1,1)
print(shortest_path_nodes(root))
# empty tree
print(shortest_path_nodes(None))
print('EVEN ODD LEVEL DIFFERENCE')
'''
def level_difference(root):
  pass

Example Input Tree
          6
         / \
        3   8
       /   / \  
      5   4   2
         / \   \
        1   7   3
Expected Output: -5
Explanation: 
Odd level sum: 6 + 5 + 4 + 2 = 17
Even level sum: 3 + 8 + 1 + 7 + 3 = 22
Odd level sum - even level sum: 17 - 22 = -5
UNDERSTAND
    root is always guaranteed
    base cases:
    if not root.left and root.right:
        return root.val
    return odd sum - even sum
PLAN
    odd_sum = 0
    even_sum = 0
    traversal using BFS approach
    using a queue thats going to keep track of each consequent node in a level by level order
    im going to store the nodes as tuples(node,depth)
    while queue:
        node = queue.popleft()
        if depth is odd:
            odd_sum+=node.val
        if depth is even:
            add val to even sum
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return odd_sum - even_sum
IMPLEMENT
'''
def level_difference(root):
    if not root.left and not root.right:
        return root.val
    odd_sum = 0
    even_sum = 0
    q = deque()
    q.append((root,1))
    while q:
        node,depth = q.popleft()
        if depth%2!=0:
            odd_sum+=node.val
        if depth%2==0:
            even_sum+=node.val
        if node.left:
            q.append((node.left,depth+1))
        if node.right:
            q.append((node.right,depth+1))
    return odd_sum - even_sum
# print(level_difference())
#     6
#    / \
#   3   8
#  /   / \  
# 5   4   2
#    / \   \
#   1   7   3
# even = 11+11 = 22
# odd = 6 + 11 = 17
# 17 -22 = -5
root = TreeNode(6,6)
three = TreeNode(3,3)
eight = TreeNode(8,8)
five = TreeNode(5,5)
four = TreeNode(4,4)
two = TreeNode(2,2)
one = TreeNode(1,1)
seven = TreeNode(7,7)
second_three = TreeNode(3,3)
root.left = three
root.right = eight
three.left = five
eight.left = four
eight.right = two
four.left = one
four.right = seven
two.right = second_three
print(level_difference(root))