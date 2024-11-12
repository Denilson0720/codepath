from collections import deque
print('UNIT 9 SESSION 2')
'''
Problem 1: Level Order Traversal of Binary Tree
Given the following pseudocode and the root of a binary tree, return a list of the level order traversal of it’s nodes’ values (i.e., from left to right, level by level).

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    # If the tree is empty:
    # return an empty list

    # Create an empty queue using deque
    # Create an empty list to store the explored nodes

    # Add the root to the queue

    # While the queue is not empty:
    # Pop the next node off the queue (pop from the left side!)
    # Add the popped node to the list of explored nodes

    # Add each of the popped node's children to the end of the queue

    # Return the list of visited nodes
    pass
      4
     / \
    2   6
   / \  
  1   3

Example Input: root = 4
Expected Output: [4, 2, 6, 1, 3]

UNDERSTAND
  what is level order traversal?
  what is a queue? how do we implement a queue?
    dequeue/remove/pop from here -->[first,second,third,last] <-- add from here/queue
    from collections import deque
    queue = deque()
    append() --> append to right side of queue, is now last in line
    popleft()--> dequeue/remove from left side, next element up in line
  what is it asking us to do?
  
PLAN
  implement level order traversal using given pseudo code
IMPLEMENT
'''
class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right
def level_order_traversal(root):
  if root is None:
    return []
  lst = []
  queue = deque()
  queue.append(root)
  while queue:
    node = queue.popleft()
    lst.append(node.val)
    if node.left is not None:
      queue.append(node.left)
    if node.right is not None:
      queue.append(node.right)
  return lst
#     4
#    / \
#   2   6
#  / \  
# 1   3
four = TreeNode(4)
two = TreeNode(2)
six = TreeNode(6)
one = TreeNode(1)
three = TreeNode(3)
four.left = two
four.right = six
two.left = one
two.right = three
print(level_order_traversal(four))
'''
time complexity: O(n) --> we are visiting all the nodes in the tree once
space complexity: O(n) --> we are creating a list whose size is dependent on the input size of the bst
'''
# queue = deque()
# queue.append(1)
# print(queue)
# popped = queue.popleft()
# print(popped)
print('END OF QUESTION 1')
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

Example Input: root = 3
Expected Output: 2
Shortest path from root node to a leaf node is 3 -> 9. Number of nodes in path is 2.

Example Input Tree #2:

   2
    \
     3
      \
       4
        \
         5
          \
           6        

Example Input: root = 2
Expected Output: 5
Shortest path from root node to a leaf node is 2 -> 3 -> 4 -> 5 -> 6.
Number of nodes in path is 5.
UNDERSTAND
  what is meant by shortest path?
    shortest path, min amount of nodes from root to leaf
  base cases? can a tree be empty? can a tree only have a root, no leaves?
    no cant be empty, yes can be only root present\
  what are our traversal methods?
    BFS(level order), DFS(inorder,preorder,postorder)
PLAN
  using the same idea from the previous question
  make queue, queue will hold tuples(node,depth)
  queue.append((root,1))
  while queue:
    node,depth = queue.popleft()
    if node is leaf node:
      return depth, because as it is a BFS it is the first encounter of a leaf node, return the earliest depth value
    if node.left:
      add node.left, depth+1
    if next_level.right:
      add node.right, depth+1
  return -1

IMPLEMENT
'''
def min_depth(root):
  queue = deque()
  
  queue.append((root,1))
  depth = 0
  while queue:
    node,depth = queue.popleft()
    # at the very first sight of a leaf node well return its depth before it is increased again
    if node.left is None and node.right is None:
      return depth
    # otherwise add leaf nodes and increase depth
    if node.left:
      queue.append((node.left,depth+1))
    if node.right:
      queue.append((node.right,depth+1))
  return 0
#     4
#    / \
#   2   6
#  / \  
# 1   3
print(min_depth(four))
 #   3
 #  / \
 # 9  20
 #    / \  
 #   15  7
three = TreeNode(3)
nine = TreeNode(9)
twenty = TreeNode(20)
fifteen = TreeNode(15)
seven = TreeNode(7)
three.left = nine
three.right = twenty
twenty.left = fifteen
twenty.right = seven
print(min_depth(three))
print('END OF QUESTION 2')
'''
Problem 3: Odd-Even Level Sum Difference in Binary Tree
Given the root of a binary tree, return the difference between the sum of all node values in odd levels and sum of all node values in even levels.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

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
  what does it mean sum of all odd-even levels?
  what traversal method would make sense here?
    -given we need to keep track of each node value per level, BFS
PLAN
  even_sum, odd_sum = 0
  queue.append((root,1))
  while queue:
    curr,level = queue.popleft()
    if level%2==0:
      even_sum += curr.val
    elif level%2!=0:
      odd_sum += curr.val
    if curr.left:
      queue.append((curr,level+1))
    if curr.right:
      queue.append((curr,level+1))
  return odd_sum - even_sum
IMPLEMENT
'''
def level_diff(root):
  even_sum = 0 
  odd_sum = 0
  queue = deque()
  # (node,level)
  queue.append((root,1))
  while queue:
    curr,level = queue.popleft()
    if level %2 ==0:
      even_sum += curr.val
    else:
      odd_sum += curr.val
    if curr.left:
      queue.append((curr.left,level+1))
    if curr.right:
      queue.append((curr.right,level+1))
  diff = odd_sum - even_sum
  return diff
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
root = TreeNode(6)
three = TreeNode(3)
eight = TreeNode(8)
five = TreeNode(5)
four = TreeNode(4)
two = TreeNode(2)
one = TreeNode(1)
seven = TreeNode(7)
second_three = TreeNode(3)
root.left = three
root.right = eight
three.left = five
eight.left = four
eight.right = two
four.left = one
four.right = seven
two.right = second_three
print(level_diff(root))
print('END OF QUESTION 3')
'''
Problem 4: Level Order Traversal of Binary Tree with Nested Lists
Given the root of a binary tree, write a function level_order() that returns the level order traversal of its nodes’ values (i.e., from left to right, level by level). level_order() should return a list of lists, where each inner list contains the node values of a single level in the tree.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

def level_order(root):
  pass

Example Input Tree
     3
    / \
   9  20
      / \
     15  7

Input: root = 3
Expected Output: [ [3], [9, 20], [15, 7]]
UNDERSTAND
  what traversal method can be used here?
  what it is the expected return of our function?
PLAN
  use queue, find current queue length and only add nodes for that size.
  keep on adding nodes to queue, using a for in range(len(queue)) helps ensure that we dont add    nodes from others levels to same sublist
  
  lst = [], where we will store lists
  use queue to keep track of visited nodes
  while queue:
    level_count = len(queue)
    level_nodes = [], sublist to be added at the end
    ensures that we dont add nodes from another level to the same sublist
    for i in range(level_count): 
      node = popleft()
      level_nodes.append(node.val)
      add leaf nodes if availabale, to queue
    lst.append(level_nodes)
  return lst
      
      
    
  
    
  
IMPLEMENT
'''
def level_order(root):
  if not root:
      return []

  lst = []
  queue = deque()
  queue.append(root)

  while queue:
      level_count = len(queue)
      level_nodes = []

      for i in range(level_count):
          node = queue.popleft()
          level_nodes.append(node.val)
          if node.left:
              queue.append(node.left)
          if node.right:
              queue.append(node.right)

      lst.append(level_nodes)

  return lst
  