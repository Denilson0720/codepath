print('UNIT 7 SESSION 2')
'''
Problem 1: Neatly Nested
Given a string, return True if it is a nesting of zero or more pairs of parentheses. Return False otherwise. A valid pair of parentheses is defined as ().
The input string will only contain the characters ( or ). Your solution must be recursive.

Evaluate the time and space complexity of your solution.

def is_nested(paren_s):
	pass
Example Usage:

# Example Input: "(())"
Example Output:

# Expected Output: True
UNDERSTNAD
    what are some positive cases?
        '((()))'
        '(())'
        '((((()))))'
        or '' as an empty string is also good
    how can we break this problem into smaller ones?
        '((()))' to '(())' to '()' to ''
    what is our base case, simplest positive case?
        if string is '': True
    recursive case:
        return shortened string shrinking from both ends everytime
PLAN
    our goal will be to reach the base case of '' to return True, if at any point our strings ending and starting valyes are not equal, return False
    for every recursive step we provide a smaller string by slicing away both start and ending characters

    if string=='':
        return True
    if string[0]==( and string[-1]==)
        return is_nsted(s[1:-1])
    return False if ends are not what they need to be, emaning well never get to the True base case
'''
def is_nested(paren_s):
    if paren_s == '':
        return True
    if paren_s[0]=='(' and paren_s[-1]==')':
        # print(paren_s[0],' is not equal to ', paren_s[-1])
        return is_nested(paren_s[1:-1])
    # return is_nested(paren_s[1:-1])
    return False
print(is_nested('((()))'))
print(is_nested('((((((()))))))'))
print(is_nested(''))
print(is_nested('(()'))
print('END OF QUESTION 1')
# time -> 0(N^2), at every recursive step we are doing N operations by removing the first and last characters of the string, and we does this n/2 times
# space -> O(N^2), at every step we are creating a new substirng through slicing and takes up 0(n) space and this is done n/2 times
'''
Problem 2: How Many 1s
Given a sorted list of integers containing only 0s and 1s, count the total number of 1’s in the array in O(log n) time.

def count_ones(lst):
	pass
Example Usage:

# Example Input: [0, 0, 0, 0, 1, 1, 1] , len = 7 , first occurance of 1 = index of 4, so 7-4 = 3 total 1s
Example Output:

# Expected Output: 3
UNDERSTAND
    how is binary search O(log n) time
    how can we benefit from the binary search appraoch here?
PLAN
    use binary search to find the first occurence of 1
    subtract len by first occurance of 1 to find total number of 1s
    # Example Input: [0, 0, 0, 0, 1, 1, 1] , len = 7 , first occurance of 1 = index of 4, so 7-4 = 3 total 1s
    [0,0,1,1,1,1,1]

IMPLEMENT
'''
def count_ones(lst):
    start = 0
    end = len(lst) - 1
    first_occurance = 0
    while start<=end:
        mid = start + (end-start)//2
        if lst[mid] ==1:
            first_occurance = mid
            end = mid -1
        else:
            start = mid+1
    return len(lst) - first_occurance
print(count_ones([0,0,0,0,1,1,1]))
print('END OF QUESITON 2')
'''
Problem 3: Binary Search IV
Thus far, we’ve mostly been using an iterative implementation of the binary search algorithm. Recursive implementations of binary search are also very common. Implement binary_search() recursively.

def binary_search(nums, target):
  pass
Example Usage:

# Example Input: nums = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
Example Output:

# Expected Output: 5
# Explanation: 11 has index 5 in the list
UNDERSTAND
  -how can we think of binary search in a recursive manner?
  -base cases?
PLAN
  -instead of manually moving our pointers left and right
  -call the method recursively but with either:
    left being moved to mid+1
    right being moved to mid-1
'''
def binary_search_recursive(arr, target, left=0, right=None):
  if right is None:
      right = len(arr) - 1

  # Base case: the search interval is empty
  if left > right:
      return -1  # Target not found

  mid = (left + right) // 2

  if arr[mid] == target:
      return mid  # Target found
  elif arr[mid] < target:
      return binary_search_recursive(arr, target, mid + 1, right)
  else:
      return binary_search_recursive(arr, target, left, mid - 1)

# Example Usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

print(binary_search_recursive(arr,7))
print('END OF QUESTION 3')
'''
Problem 4: Count Rotations
You are given a circularly sorted list of integers. A circularly sorted list of integers is a sorted list whose elements have then been rotated some number of times such that the last element of the array becomes the first element of the array. Write a function count_rotations() that returns the total number of times the array is rotated. Assume there are no duplicates in the array.

def count_rotations(nums):
  pass
Example Usage:

# Example Input: [8, 9, 10, 2, 5, 6]
Example Output:

# Expected Output: 3
# Explanation: Array is rotated 3 times:
  # Sorted Array: [2, 5, 6, 8, 9, 10]
  # First Rotation: [10, 2, 5, 6, 8, 9]
  # Second Rotation: [9, 10, 2, 5, 6, 8]
  # Third Rotation: [8, 9, 10, 2, 5, 6]
UNDERSTAND
  what are some important key points?
    -assume no duplicates
    -list is ordered
    -max number of rotations is len(lst)
PLAN
  -iterative method
  find where our lowest integer is located
    low = len(lst)-1
    while lst[low-1]>lst[low]
      low--
  set rotation_count= 0
  while lst[low-1]> lst[low]
    low--
    count++
  return count
IMPLEMENT
'''
def count_rotations(nums):
  rotation_count = 0
  if len(nums)<=1:
    return 1
  low = len(nums)-1
  # find where our lowest integer is
  while nums[low-1]<nums[low]:
    low-=1
  lowest_point = low
  # increment rota_count by comparing low to lowest_point
  low-=1
  # return len(nums) - (len(nums) - lowest_point)
  while nums[low]>nums[lowest_point] and low>=0:
    low-=1
    rotation_count+=1
  return rotation_count

def count_rotations_2(nums):
  if len(nums)<=1:
    return 1
  low = len(nums)-1
  # find where our lowest integer is
  while nums[low-1]<nums[low]:
    low-=1
  low_diff = len(nums)-low
  return len(nums) - low_diff
print(count_rotations([10,2,5,6,8,9]))
print(count_rotations_2([10,2,5,6,8,9]))
print(count_rotations([9,10,2,5,6,8]))
print(count_rotations_2([9,10,2,5,6,8]))
print(count_rotations([6,8,9,10,2,5]))
print(count_rotations_2([6,8,9,10,2,5]))
print('END OF QUESTION 4')
'''
Problem 5: Merge Sort I
Merge sort is a sorting algorithm that takes in an unsorted list and returns a sorted list in O(n log n) time which is faster than many other sorting algorithms that have O(n²) time complexity. It uses a divide and conquer approach.

Merge sort works by using a divide and conquer approach: it divides the array into two halves until each sublist contains only a single element, then it recursively sorts each sublist, and merges the sorted sublists into a sorted array.

Given the pseudo-code and helper function merge() below, implement the merge_sort() function.

# Helper function: Merges two sorted lists into one sorted list
def merge(left, right):
  result = [] # List to store the merged result
  i = j = 0 # Pointers to iterate over left and right input arrays

  # Compare elements from left and right halves of the list and add them to the
  # result list in the correct order
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
        result.append(left[i])
        i += 1
    else:
        result.append(right[j])
        j += 1
  # Add any remaining elements from the left half to the result list
  while i < len(left):
      result.append(left[i])
      i += 1

  # Add any remaining elements from the right half to the result list
  while j < len(right):
      result.append(right[j])
      j += 1

  return result

def merge_sort(lst):
  pass
Example Usage:

# Example Input: [5,3,4,2,1]
Example Output:

# Expected Output: [1,2,3,4,5]
UNDERSTAND
  -base cases?
  -how will our recursive cases work?
    -half our probelm set until only 1 element is present in each subset
    -find mid and use slicing to do so
PLAN
  base case, if len(lst)<=1, return lst
  recursive case,
    find mid, len(lst)//2
    left_half = merge[:mid]
    right_half = merge[mid:]
  return merge(left,right)
IMPLEMENT
'''
def merge(left, right):
  result = [] # List to store the merged result
  i = j = 0 # Pointers to iterate over left and right input arrays

  # Compare elements from left and right halves of the list and add them to the
  # result list in the correct order
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
        result.append(left[i])
        i += 1
    else:
        result.append(right[j])
        j += 1
  # Add any remaining elements from the left half to the result list
  while i < len(left):
      result.append(left[i])
      i += 1

  # Add any remaining elements from the right half to the result list
  while j < len(right):
      result.append(right[j])
      j += 1

  return result
def merge_sort(lst):
  if len(lst)<=1:
    return lst
  # left = 0 
  # right = len(lst)-1
  mid  = (len(lst))//2
  # recursion to each sublist youve made
  # left half up until the calculated mid point for that sublist
  left_half = merge_sort(lst[:mid])
  # right half starting from the calculated mid point for that sublist
  right_half = merge_sort(lst[mid:])
  return merge(left_half,right_half)

print(merge_sort([1,5,3,2,1]))
print('END OF QUESTION 5')
