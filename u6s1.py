print('UNIT 6 SESSION 1 QUESTIONS')
def print_ll(head):
  lst = []
  while head:
    # print(head.value)
    if head.next:
      lst.append(f'{head.value} ->')
    else:
      lst.append(head.value)
    head = head.next
  print(lst)
'''
Problem 1: Nested Constructors
Step 1: Copy the following code into Replit.

Step 2: Add a line of code (outside of the class) to create the linked list 4 -> 3 -> 2 in a single assignment statement.

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
UNDERSTAND
  how would we normally have made a linked list beforehand?
  it the next attribute required for an object of the Node class?
PLAN
  make a linked list 4->3->2 in a single line by nesting
IMPLEMENT
'''
class Node:
  def __init__(self,value,next=None):
    self.value = value
    self.next = next
node_1 = Node(4,Node(3,Node(2)))
print_ll(node_1)
print('END OF QUESTION 1')
'''
Problem 2: Find Frequency
Given the head of a linked list and a value val, return the frequency of val in the list. Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def count_element(head, val):
  pass
Example Usage:

# Input List: 3 -> 1 -> 2 -> 1
# Input: head = 3, val = 1
Example Output:

# 2
UNDERSTAND
  what can we check to see the value of the node?
  is val guaranteed to show up in the list?
  will head always be more than a single node?
PLAN
  count = 0
  iterate through list
    if node.val == val:
      increase count by 1
  return count
IMPLEMENT
'''
def count_element(head,val):
  count = 0
  while head:
    if head.value == val:
      count+=1
    head = head.next
  return count
# Input List: 3 -> 1 -> 2 -> 1
# Input: head = 3, val = 1
test_case_1 = Node(3,Node(1,Node(2,Node(1))))
# output --> 2
print(count_element(test_case_1,1))
# time complexity: O(n), our operations are directly correlated to the number of ndoes in the LL
# space complexity: O(1), we are not making any new data strucutre memory to store stuff
print('END OF QUESTION 2')
'''
Problem 3: Remove Tail
The following code attempts to remove the tail of a singly linked list. However, it has a bug!

Step 1: Copy this code into Replit.

Step 2: Create your own test cases to run the code against, and use print statements and the stack trace to identify and fix the bug so that the function correctly removes the tail of the list.

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 

  # Start from the head and find the second-to-last node
    current = head
    while current.next: 
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head
Example Usage:

# Input List: 1 -> 2 -> 3 -> 4
# Input: head = 1
Example Output:

# Expected Return Value: 1
# Expected Result List: 1 -> 2 -> 3
UNDERSTAND
  what should we do if the linked list lasts a head or is only a single node?
    in that case, are the base cases correct?
  how do we delete the tail? conceptually?
    where do we need to be?
    do we need to be at the last element or the one before(second to last)?
    how do we get there?
  PLAN
    look at code
    base cases are correct
    point is to land at the second to last node so:
    FIX THIS
    while current.next.next:
      current = current.next
IMPLEMENT
'''
def remove_tail(head):
  if head is None: # If the list is empty, return None
      return None
  if head.next is None: # If there's only one node, removing it leaves the list empty
      return None 

# Start from the head and find the second-to-last node
  current = head
  # while current.next: 
  # FIXED
  while current.next.next:
      current = current.next

  current.next = None # Remove the last node by setting second-to-last node to None
  return head
# Input List: 1 -> 2 -> 3 -> 4
# Input: head = 1
# Example Output:
# Expected Return Value: 1
# Expected Result List: 1 -> 2 -> 3
test_case_1 = Node(1,Node(2,Node(3,Node(4))))
print_ll(test_case_1)
new_ll = remove_tail(test_case_1)
print_ll(new_ll)
print('END OF QUESTION 3')
'''
Problem 4: Find the Middle
A variation of the two-pointer technique introduced in Unit 4 is to have a slow and a fast pointer that increment at different rates. Given the head of a linked list, use the slow-fast pointer technique to find the middle node of a linked list. If there are two middle nodes, return the second middle node.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
  pass
Example Usage:

# Input List:
# 1 -> 2 -> 3
# Input: head = 1
Example Output:

# Expected Return Value: 2
UNDERSTAND
  how can a fast and slow pointer help us here?
  what if there is only 1 node?
  how do we make sure we return the second middle node?
PLAN
  1->2->3
  sf
     s  f
  1->2->3->4->5
  sf     
     s  f 
        s     f
  1->2->3->4->5->6->7->8
  sf
     s  f
        s.    f
           s        f
              s           f = None
  using a slow and fast pointer, move slow by 1 node and fast by 2 nodes every iteration
  iterate pointers until fast is not None
IMPLEMENT
'''
def find_middle(head):
  slow = head
  fast = head
  while fast.next and fast.next.next:
    slow =slow.next
    fast = fast.next.next
  if fast.next:
    slow = slow.next
  return slow.value
test1 = Node(1,Node(2,Node(3)))
print_ll(test1)
test2 = Node(1,Node(2,Node(3,Node(4,Node(5)))))
print_ll(test2)
test3 = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8))))))))
print_ll(test3)
print(find_middle(test1))
print(find_middle(test2))
print(find_middle(test3))
# time -> O(n), operations is directly correlated to number of nodes
# space -> O(1), were not mkaing any new memory allocations, jsut moving pointers
print('END OF QUESTION 4')
'''
Problem 5: Is Palindrome?
Given the head of a singly linked list, return True if the values of the linked list are palindromic and False otherwise. Use the two-pointer technique in your solution.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def is_palindrome(head):
  pass
Example Usage:

# Input List:
# 1 -> 2 -> 1
# Input: head = 1
Example Output:

# True
UNDERSTAND
  what is a palindrome?
  what methods that weve done previously can be used here?
  do we need to use another data structure here?
  
PLAN
  lst = []
  iterate through list adding node values to list
  check if lst is the same forwards and back
IMPLEMENT
'''
def is_palindrome(head):
  lst = []
  while head:
    lst.append(head.value)
    head = head.next
  return lst==lst[::-1]

test1 = Node(1,Node(2,Node(1)))
test2 = Node(1,Node(2,Node(2,Node(1))))
test3 = Node(1,Node(2,Node(3,Node(2,Node(1)))))
test3 = Node(1,Node(2,Node(3,Node(4,Node(3,Node(2,Node(1)))))))
test4 = Node(1,Node(2,Node(3,Node(4,Node(2,Node(2,Node(1)))))))
print(is_palindrome(test1))
print(is_palindrome(test2))
print(is_palindrome(test3))
print(is_palindrome(test4))
print('END OF QUESTION 5')













def is_same_from_mid(head):
  start,mid,end = head,head,head
  while end.next and end.next.next:
    # move mid by 1, slow
    mid = mid.next
    # move end by 2, fast
    end = end.next.next
  # edge case if there are 2 middle nodes, move mid up 1 node once more
  if end.next:
    mid = mid.next

  print('mid:',mid.value,'start:',start.value)
  while mid.next:
    if start.value != mid.value:
      return False
    # move pointers by 1
    mid = mid.next
    start = start.next
  return True
