from collections.abc import ValuesView
print('UNIT 10 SESSION 1 QUESTIONS')
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', return True if the input string is valid and False otherwise.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
def is_valid(s):
  pass
UNDERSTAND
  what is considered a valid input string?
  what data structure comes to mind when thinking about a solution to this?
  can a string be empty?
  can a string be 1 characters?
  how can we use a stack in python?-->list or queue
PLAN
  using a stack data structure
  iterate through the string
    IF opening bracket:
      add opening brackets/paranthesis to stack
    ELSE if closing bracket and top element matches parantheis(but open):
      remove top
  return is stack empty
IMPLEMENT
'''
def is_valid(s):
  # base cases?
  stack = []
  for bracket in s:
    if bracket =='[' or bracket == '{' or bracket == '(':
      stack.append(bracket)
    elif bracket == ']' and stack[-1] =='[':
      stack.pop()
    elif bracket == ')' and stack[-1] =='(':
      stack.pop()
    elif bracket == '}' and stack[-1] =='{':
      stack.pop()
    else:
      return False
  return len(stack)==0
print(is_valid('()'))
print(is_valid('()[]{}'))
print(is_valid('(]'))
print('END OF QUESTION 1')
'''
Problem 2: Best Time to Buy & Sell Stock
You are given a list of integers prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
[7,1,5,3,6,4], output = 5
def max_profit(prices):
  pass
UNDERSTAND
  what do we return?
  is profit always guaranteed?
  what is the list prices?
  base case?
  can list be 0 or 1 in length?
PLAN
  brute force
    find low through first loop of list
    starting from lows index, find max
      if list[i]>max:
        max = list[i]
    profit =list[max] - list[low]
    return profit
IMPLEMENT
'''
def max_profit(prices):
  low = 0
  # find low
  for i in range(len(prices)-1):
    if prices[i]<prices[low]:
      low = i
  # find high
  high = low
  for i in range(low,len(prices)-1):
    if prices[i]>prices[high]:
      high = i
  profit = prices[high] - prices[low]
  return profit
print(max_profit([7,1,5,3,6,4]))
print(max_profit([7,6,4,3,1]))
print('END OF QUESTION 2')
'''
Problem 3: Shuffle Merge
Given the heads of two singly linked lists of integers, merge their nodes to make one list, taking nodes alternately between the two lists. If either list runs out of elements before the other, all nodes from the list with remaining nodes should be appended onto the end of the merged list. Return the head of the merged list.

def shuffle_merge(head_a, head_b):
  pass
UNDERSTAND
  merge two lists
  what happens if one list runs out of nodes first?
  can 1 list be empty?
  can both be empty? no, were given both heads, at least 1 node for each
  are we going to have to make a new list? new head?
  it says alternately, but based off examples which list gets its nodes added first?
PLAN
  make a new_list head
  make a pointer for thus new_list, new_curr
  iterate through both lists
  make pointers for each list, curr_a, curr_b
  while curr_a or curr_b:
    if curr_a:
      add to new_list, new_curr.next = curr_a
      new_curr = new_curr.next
    if curr_b:
      add to new_list, new_curr.next = curr_b
      new_curr = new_curr.next
  return new_list 
IMPLEMENT
'''
class Node:
  def __init__(self,value,next=None):
      self.value = value
      self.next = next
def shuffle_merge(head_a,head_b):
  new_list_head = Node(head_a.value)
  new_curr = new_list_head
  # curr_a starts at second node list a
  curr_a = head_a.next
  curr_b = head_b
  while curr_a or curr_b:
    # since weve added from list a first already, start adding from list b
    if curr_b:
      new_curr.next = curr_b
      curr_b = curr_b.next
      new_curr = new_curr.next
    if curr_a:
      new_curr.next = curr_a
      curr_a = curr_a.next
      new_curr = new_curr.next
  return new_list_head
def print_ll(head):
  lst = []
  while head:
    # print(head.value)
    if not head.next:
      lst.append(head.value)
    else:
      lst.append(f'{head.value} ->')
    head = head.next
  print(lst)
print('TEST CASE 1')
head_a = Node(1,Node(2,Node(3)))
head_b = Node(4,Node(5,Node(6)))
print_ll(head_a)
print_ll(head_b)
new_list = shuffle_merge(head_a,head_b)
print_ll(new_list)
print('TEST CASE 2')
head_a = Node(1,Node(2,Node(3)))
head_b = Node(4)
print_ll(head_a)
print_ll(head_b)
new_head =shuffle_merge(head_a,head_b)
print_ll(new_head)
print('END OF QUESTION 4')
'''
Problem 4: Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def group_anagrams(strs):
  pass
UNDERSTAND
  what is an anagram?
  base cases?
  can our string be empty?
  do we have to worry about order?
PLAN
  USING A DICTIONARY WHERE:
    keys = sorted string in alphabetical order
    values = list of all anagrams for that key
    -traverse list, adding new keys or append to list if key is present
    key = ''.join(sorted(strs[i])), turn current string to sorted key
    if key in anagrams:
      append strs[i] to its list
    else: key isnt present
      make a new key value pair
    return all values,values() as list
  
'''
str = 'adec'
a = ''.join(sorted(str))
print(a)
def group_anagrams(strs):
  anagrams = {}
  for i in range(len(strs)):
    sorted_string = ''.join(sorted(strs[i]))
    if sorted_string in anagrams:
      anagrams[sorted_string].append(strs[i])
    else:
      anagrams[sorted_string] = [strs[i]]
  return list(anagrams.values())
  # return anagrams.values()
strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))
print('END OF QUESTION 4')
'''
Problem 5: Sum Root to Leaf Numbers
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers.

A leaf node is a node with no children.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_numbers(root):
  pass 
UNDERSTAND
  what traversal is best to use here?
  base cases?
PLAN
  using DFS
  helper function dfs(node, curr_num):
    update curr_num + node.val
    if curr_num.right and .left is None:
      return curr_num
    recursive call for left and right children
    return sum from subtrees
  
'''
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def sum_numbers(root):
  def dfs(node, current_number):
      if node is None:
          return 0

      current_number = current_number * 10 + node.val

      # If the current node is a leaf, return the current number
      if node.left is None and node.right is None:
          return current_number

      # Recursively sum the numbers from the left and right subtrees
      left_sum = dfs(node.left, current_number)
      right_sum = dfs(node.right, current_number)

      return left_sum + right_sum

  # Start DFS with the root and initial current number as 0
  return dfs(root, 0)
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
one.left = two
one.right = three
print(sum_numbers(one))
  