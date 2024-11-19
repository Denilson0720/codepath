print('UNIT 10 SESSION 2')
'''
Problem 1: Contains Duplicates
Given an integer array nums, return True if any value appears at least twice in the array, and return False if every element is distinct.

def contains_duplicate(nums):
  pass

Example Usage:

Example #1: 
Input: nums = [1,2,3,1]
Output: True

Example #2:
Input: nums = [1,2,3,4]
Output: False

Example #3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: True
UNDERSTAND
  what are we supposed to return?
  base cases?
PLAN
  using sets
    -make an empty set
    -iterate through all the values in the array adding each to the set
    -if we can add it great, continue
    -else return false, item is already present in set, meaning duplicate
IMPLEMENT    
'''
def contains_duplicates(nums):
  my_set = set()
  for n in nums:
    if n in my_set:
      return True
    my_set.add(n)
  return False
print(contains_duplicates([1,2,3,4,5,5]))
print(contains_duplicates([1,2,3,4,5]))
print(contains_duplicates([1]))
print(contains_duplicates([]))
print('END OF QUESTION 1')
'''
Problem 2: Remove Element
Given a list of integers nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, for your response to be acceptable, you need to do the following things:

Change the list nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k
Example #1:
Input: nums = [3,2,2,3], val = 3
Expected Output: 2
nums should be [2,2,_,_]
Explanation: Your function should return k = 2,
with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example #2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5
nums should be [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

def remove_element(nums, val):
  pass
  
UNDERSTAND
  what are we supposed to return?
  does order matter for our end resulting nums array?
  what should nums be at the end?
  what do we replace val with?
PLAN
  -iterate through nums
  -rewrite the array
  -make a cursor/poitner that will be used to indicate a non-val value
  k=0
  -if nums[i]!=val
    nums[k] = nums[i]
    move your pointer to the next element, k+=1
  -now k should be the amount of non-val elements
  -SECOND LOOP, rewrite val elements as '-' starting from k till end
  for i in range(k,len(nums))
    nums[i] = '-'
  
    
IMPLEMENT
'''
def remove_elements(nums,val):
  # Pointer for the next position to place a non-val element
    k = 0

    # Iterate over each element in the list
    for i in range(len(nums)):
        # If the current element is not equal to val, move it to the position k
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    # Replace the remaining elements with underscores
    for i in range(k, len(nums)):
        nums[i] = '_'
    print(nums)
    # Return the number of elements that are not equal to val
    return k
print(remove_elements([1,2,5,4,5],5))
print(remove_elements([0,1,2,2,3,0,4,2],2))
print(remove_elements([3,2,2,3],3))
print('END OF QUESTION 2')
'''
Problem 3: Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

def gcd_of_stings(str1, str2):
  pass


Example #1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example #2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example #3:
Input: st1 = "LEET", str2 = "CODE"
Output: ""  
UNDERSTAND
  what do it means for x to divide str1 and str2
    x is concatinated with itself one of more times and fits in either strings
    example 1: ABCABC and ABC --> ABC, both strings can be formed by repeating ABC 
    example 2: ABABAB and ABAB --> AB, both strings can be formed by repeating AB
      output cannot be ABAB as ABABAB cannot be formed by repeating it.
PLAN
`  find longest string
  have two pointers iterate both
  form new string using pointers
  while new_str length >0:
    if new_str*2 != longest string
      new_str.remove(-1)
  return new_str
'''
def gcd_of_strings(str1, str2):
  # Check if concatenation of str1 and str2 in both orders is the same
  if str1 + str2 != str2 + str1:
      return ""

  # Iterate from the length of the smaller string down to 1
  min_length = min(len(str1), len(str2))
  # your going to go only till both substrings are diviible by smaller string length
  for i in range(min_length, 0, -1):
      # Check if the current length divides both strings
      if len(str1) % i == 0 and len(str2) % i == 0:
          candidate = str1[:i]
        # check if candidate can make str1, no remainder
        # check if candidate can make str2, no remainder
          if candidate * (len(str1) // i) == str1 and candidate * (len(str2) // i) == str2:
              return candidate

  return ""
print(gcd_of_strings('ABABAB','ABAB'))
print(gcd_of_strings('ABCABC','ABC'))
# print(str*2)
print('END OF QUESTION 3')
'''
Problem 4: Check Balanced Binary Tree
Given the root of a binary tree, return True if the tree is balanced and False otherwise.

A balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
Input Tree #1:

      3
     /  \
    9   20
       /  \  
      15   7

Input: root = 3
Output: True

Input Tree #2:

          1
         / \
        2   2
       / \  
      3   3
     / \
    4   4  

Input: root = 1
Output: False


Input Tree #3: Empty Tree
Input: root = 1
Output: True

def is_balanced(root):
  pass
UNDERSTAND
  what is meant by a balanced tree?
  what if we dont have subrtrees?
  base cases?
  are we guaranteed a root, and or subtrees?
PLAN
  recursively
  using DFS
  recursively check if your left and right subtrees heights are <=1
'''
class TreeNode:
  def __init__(self,val,left =None,right = None):
    self.val = val
    self.left = left
    self.right = right
def check_balance_and_height(node):
  if not node:
      return True, 0

  left_balanced, left_height = check_balance_and_height(node.left)
  right_balanced, right_height = check_balance_and_height(node.right)

  balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
  height = max(left_height, right_height) + 1

  return balanced, height

def is_balanced(root):
  balanced, height = check_balance_and_height(root)
  return balanced
#    3
#  /  \
# 9   20
#    /  \  
#   15   7
three = TreeNode(3)
nine = TreeNode(9)
twenty = TreeNode(20)
fifteen = TreeNode(15)
seven = TreeNode(7)
three.left, three.right = nine, twenty
twenty.left, twenty.right = fifteen, seven
print(is_balanced(three))
#       1
#      / \
#     2   2
#    / \  
#   3   3
#  / \
# 4   4  
one = TreeNode(1)
first_two = TreeNode(2)
second_two = TreeNode(2)
first_three = TreeNode(3)
second_three = TreeNode(3)
first_four = TreeNode(4)
second_four = TreeNode(4)
one.left, one.right = first_two, second_two
first_two.left, first_two.right = first_three, second_three
first_three.left, first_three.right = first_four, second_four
print(is_balanced(one))
print('END OF QUESTION 4')
'''
Problem 5: Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

def subarray_sum(nums, k):
  pass

Example Usage:

Example #1:
Input: nums = [1, 1, 1], k = 2
Output: 2

Example #2:
Input: nums = [1, 2, 3], k = 3
Output: 2
UNDERSTAND
  what is meant by a subarray?
  what is the sum of a subarray?
PLAN  
  -using a dictionary
IMPLEMENT
'''
def subarray_sum(nums, k):
  # dictionary is going to keep track of occurances of sums
  cumulative_sum = {0: 0}
  current_sum = 0
  count = 0

  for num in nums:
      
      current_sum += num
      # if current_sum is k increase count
      if current_sum == k:
          count += 1
      # if current_sum is in dictionary, increase count
      if current_sum - k in cumulative_sum:
          count += cumulative_sum[current_sum - k]
    
      if current_sum in cumulative_sum:
          cumulative_sum[current_sum] += 1
      else:
          cumulative_sum[current_sum] = 1

  return count
print(subarray_sum([1,2,3],3))
print(subarray_sum([1,1,1],2))
print(subarray_sum([3,1,2],3))
  