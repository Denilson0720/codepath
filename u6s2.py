class Node:
  def __init__(self,value,next = None):
    self.value = value
    self.next = next
def print_ll_w_list(head):
  lst = []
  while head:
    # print(head.value)
    if head.next:
      lst.append(f'{head.value} ->')
    else:
      lst.append(head.value)
    head = head.next
  print(lst)
def print_ll(head):
  while head:
    print(head.value)
    head = head.next
  
'''
Problem 1: Detect Circular Linked List
A circular linked list is a linked list where the tail node points at the head node. Given the head of a linked list, write a function is_circular() that returns True if the linked list is circular and False otherwise.

Note: a circular list is more than just a cycle - specifically connecting the first and last nodes.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head):
  pass
Example Usage:

# num1 -> num2 -> num3 -> num1
print(is_circular(num1))

# var1 -> var2 -> var3
print(is_circular(var1))
Example Output:

True
False
UNDERSTAND
  what methods that weve used before can help us here?
  in a circular linked list, if we have a chaser that is faster than a normal nodes speed, would the chaser eventually catch up to the normal node?
PLAN
  using fast and slow pointer
  slow = head
  fast = head.next
  while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True, it is circular
  return False
IMPLEMENT
'''
def is_curcular(head):
  slow = head
  fast = head.next
  while fast.next and fast.next.next:
    if slow == fast:
      return True
    slow = slow.next
    fast = fast.next.next
  return False
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = head
test2 = Node(1,Node(2,Node(3,Node(4))))
# print_ll_w_list(head) --> goes forever
# print_ll(head) --> goes forever
print(is_curcular(head))
print(is_curcular(test2))
print('END OF QUESTION 1')
'''
Problem 2: Find Last Node in a Linked List Cycle
Given the head of a singly linked list, write a function that returns the last node in the cycle. If there is no cycle in the linked list, return None.

def find_last_node_in_cycle(head):
  pass
Example Input: num1 -> num2 -> num3 -> num4 -> num2

Example Output: num4
UNDERSTAND
  how do we check if a node is a last of its cycle?
  is a node a memory or just the value? can we compare the memory location?
PLAN
  iterate through list after head, using curr
  if curr.next == head:
    return curr
  return None
IMPLEMENT
'''
# WRONG
# def find_last_node_in_cycle(head):
#   curr = head.next
#   while curr:
#     if curr.next == head:
#       return curr.value
#     curr = curr.next
#   return None
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = head
test2 = Node(1,Node(2,Node(3,Node(4,Node(1)))))

def find_last_node_in_cycle(head):
    if not head or not head.next:
        return None

    slow = fast = head
    has_cycle = False

    # Phase 1: Detecting the cycle using the Floyd's Cycle Detection Algorithm
    # here we just check if there is a cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    # If there's no cycle, return None
    if not has_cycle:
        return None
    # 1,2,3,4 and 4 back to 2

    # Phase 2: Identifying the start of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Find the last node in the cycle
    cycle_start = slow
    last_node = cycle_start
    while last_node.next != cycle_start:
        last_node = last_node.next

    return last_node.value
'''

Input: A list with a cycle (e.g., 1 -> 2 -> 3 -> 4 -> 5 -> 2)

PHASE 1
1   2   3   4   5   BACK TO 2
SF
    S.  F
        S.      F 
        F   S          
                SF<- THEY MET AGAIN, there is a cycle

PHASE 2
OUR SECOND ITERATION
Move slow and fast pointer by 1 node per step, and they'll meet at the start of the cycle
They met at Node 2
1.  2.  3.  4.  5
S               F
    SF 

PHASE 3
NOW SAVE THIS CYCLE START, cycle_start = slow or fast
Using another pointer (last_node) move it until its .next is cycle_start
SHOULD GIVE YOU LAST NODE
1   2   3.  4.  5
   C L 
    C   L
    C        L 
    C            L and its .next is C so return L
   
'''
print(find_last_node_in_cycle(head))
# shoudl return None as there is no cycle
print(find_last_node_in_cycle(test2))
print('END OF QUESTION 2')
'''
Problem 3: Partition List Around Value
Given the head of a linked list and a value val, partition a linked list around val such that all nodes with values less than val come before nodes with values greater than or equal to val.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def partition(head, val):
  pass
Example Input:

# 1 -> 4 -> 3 -> 2 -> 5 -> 2
# head = 1, val = 3
Result Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5 or 2 -> 2 -> 1 -> 5 -> 4 -> 3
UNDERSTAND
  in order to partition this correctly, are we swapping only the node values or the nodes themselves?
  does vals location matter?
  how should our partition affect the list order?
    VAL CAN GO ANYWHERE
    order:less than numbers, greater than numbers, value can be here
    order:value can be here,less than numbers, greater than numbers
    order:less than numbers,value can be here, greater than numbers
  is our value the partition itself? no
  what method that weve used before can we use here?
PLAN
  using dummy heads make 2 seperate lists, small and large
  any values less than val go in small
  any values greater than val go in large
  concat both lists, link small pointer to head of large list head
  DUMMY HEADS
  small_dummy = Node('')
  small_pointer = small_dummy
  large_dummy = Node('')
  large_pointer = large_dummy
  curr = head
  while curr.next:
    if curr.val<val:
      small.next = Node(curr.val)
      small = small.next
    elif curr.val=>val:
      large.next = Node(curr.val)
      large = large.next
    curr = curr.next
  CONCAT BOTH LISTS
  small_pointer.next = large_dummy
  return small_pointer.next

IMPLEMENT
'''
def partition(head,val):
  small_dummy = Node('')
  # used to traverse and create small list
  small_pointer = small_dummy
  large_dummy = Node('')
  # use to traverse and create large list
  large_pointer = large_dummy
  curr = head
  # traversing original list
  while curr:
    if curr.value<val:
      small_pointer.next = Node(curr.value)
      small_pointer = small_pointer.next
    elif curr.value>= val:
      large_pointer.next = Node(curr.value)
      large_pointer = large_pointer.next
    curr = curr.next
  # concat
  small_pointer.next = large_dummy.next
  return small_dummy.next
# 1 -> 4 -> 3 -> 2 -> 5 -> 2
# expected outout 1,2,2,4,5 , with 3 being anywhere
head = Node(1,Node(4,Node(3,Node(2,Node(5,Node(2))))))
new_head = partition(head,3)
print_ll_w_list(new_head)

print('END OF QUESTION 3')
def remove_node(head,val):
  dummy_head = Node('')
  dummy_head.next = head
  curr = dummy_head
  while curr.next:
    if curr.next.value == val:
      # skip over node to delete
      curr.next = curr.next.next
    curr = curr.next
  # return dummy_head.next
'''
Problem 4: Convert Binary Number in a Linked List to Integer
You are given the head of a linked list. Each value in the linked list is either 0 or 1, and the entire linked list represents a binary number. Return an integer that is the decimal value of the number represented by the linked list. The most significant bit is at the head of the linked list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def binary_to_int(head):
  pass
Example Usage:

# 1 -> 0 -> 1
num1 = 1
num2 = 0
num3 = 1
int_num = binary_to_int(num1)
# 101 in binary 

print(int_num)
Example Output: 5
UNDERSTAND
  how do we convert a binary number to an integer?
    1 0 1 = 1*2^2 + 0*2^1 + 1*2^0 = 4 + 0 + 1
  what data will be useful to know first?
    -length of list
    -what technique can we use to acquire this value?
PLAN
  SINGLE PASS
  length = 0
  find out legnth of list first, our binary conversion power will start from here
  ITERATE THROUGH NODES ADDING TO SUM
  sum = 0
  power = length-1
  curr = head
  while curr:
    sum += curr.value * 2**power
    curr = curr.next
    power -=1
  return sum
IMPLEMENT
'''
def binary_to_int(head):
  length = 0
  curr = head
  # get length
  while curr:
    length+=1
    curr = curr.next
  curr = head
  sum = 0
  power = length -1
  while curr and power>=0:
    sum+=curr.value *2**power
    curr = curr.next
    power-=1
  return sum
binary_head = Node(1,Node(0,Node(1)))
print(binary_to_int(binary_head))
binary_head_2 = Node(1,Node(0,Node(1,Node(0,Node(1,Node(0,Node(1)))))))
print(binary_to_int(binary_head_2))
print('END OF QUESTION 4')
'''
Problem 5: Add Two Numbers Represented by Linked Lists
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def add_two_numbers(head_a, head_b):
    pass

Example Usage:

# list 1: 2 -> 4 -> 3 (342)
# list 2: 5 -> 6 -> 4 (465)
# head_a = 2, head_b = 5

sum = add_two_numbers(head_a, head_b)
print(sum)
Example Output: 807
UNDERSTAND
  what are we given?
  what can we take advantage of? what do we not need to worry about?
    -reverse order is already taking care of natural sum order
    -no negative or non existent numbers, every node is valid and positive
  what techniques used before could be beneficial to use here?
  what do we have to keep track of?
    -carry over values
PLAN
  create a result_head = Node('')
  result = result_head , use this pointer to add and iter through new list
  curr_a = head_a
  curr_b = head_b
  carry = 0
  while curr_a or curr_b:
    sum = curr_a.value + curr_b.value
    val = 0 if sum>10 else sum
    result.value = val + carry
    carry = sum % 10
    result.next = Node('')
    result = result.next
    curr_a = curr_a.next
    curr_b = curr_b.next
  return result_head.next
'''
def add_two_numbers(head_a,head_b):
  result_head = Node('')
  result = result_head
  curr_a = head_a
  curr_b = head_b
  carry = 0
  while curr_a or curr_b:
    a_val = curr_a.value if curr_a else 0
    b_val = curr_b.value if curr_b else 0
    # val = 0 if sum>=10 else sum
    # result.value = val
    # carry = sum%10
    # result.next = Node('')
    # result = result.next
    # curr_a = curr_a.next
    # curr_b = curr_b.next
    sum = a_val + b_val + carry
    carry = sum // 10
    val = sum % 10
    result.next = Node(val)
    result = result.next
    if curr_a:
        curr_a = curr_a.next
    if curr_b:
        curr_b = curr_b.next
  return result_head.next
# list 1: 2 -> 4 -> 3 (342)
# list 2: 5 -> 6 -> 4 (465)
num1 = Node(2,Node(4,Node(3)))
num2 = Node(5,Node(6,Node(4)))
sum = add_two_numbers(num1,num2)
print('END OF QUESTION 5')
# SOLUTUION TO MOCK INT.
# magazine 
# ransom note
# check if ransom note can be made of magazine, return boolean
#   A and a are different characters
#   an empty ransom note can be made of an empty magazine
#   an empty ransom note returns True
def is_ransom(ransom_note,magazine):
  new_mag = list(magazine)
  for char in range(len(ransom_note)):
    if ransom_note[char] not in magazine:
      return False
    new_mag.remove(ransom_note[char])
  # print(new_mag)
  return True
print(is_ransom('hello','hello world'))
print(is_ransom('he llo','hello world'))
print(is_ransom('he','hllo'))
    