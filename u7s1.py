# UNIT 7 SESSION 1 PROBLEMS
'''
Problem 1: Hello Hello
A recursive function is a function that calls itself within the body of the function.

Step 1: Copy the recursive function repeat_hello() into Replit and run it.

Step 2: Then create another function repeat_hello_iterative() that produces the same output without using recursion.

Compare your iterative (non-recursive) solution to the recursive solution provided. What is similar? What is different?

def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)
		
repeat_hello(5)

UNDERSTAND
    what does it mean to have a recursive function?
        being able to break down a big problem into many smaller ones
        where the base case is the stopping point of the recursion and our recursive case is where the function calls itself with a smaller or simpler version of the problem
    what are the benefits of using a recursive function?
        breaking down the problem and being able to think of the smallest version
    what part of the function prevents our recursive function from going on forever?
        base case
    what is the recursive case?
    in the solution above, what is the base case?
PLAN
    use the recursive functions
    make an iterative function
    compare both
IMPLEMENT
'''
def repeat_hello(n):
    # base case covered by n>0, once we reach 0 we wont be able to call the function anymore
    if n>0:
        print('hello')
        repeat_hello(n-1)
print('recursive approach')
repeat_hello(5)
def repeat_hello_iterative(n):
    while n>0:
        print('hello')
        n=-1
print('iterative approach')
repeat_hello(5)
# both solutions do the same thing
# our dependent counter/ stepper is located in the function call itself in the recursive approach whereas in the iterative
# we are decremeenting n ourselves each step
print('END OF QUESTION 1')
'''
Problem 2: Factorial Cases
Given the base case and recursive case, write a function factorial() that returns the factorial of a non-negative integer n. The factorial of a number is the product of all numbers between 1 and n.

Base Case: The smallest number we can find a factorial of is 0. By definition, the factorial of 0 is 1.

Recursive Case: We can restate the problem to say that the factorial of n is n * the factorial of n-1.

def factorial(n):
	pass
Example Usage:

# Example Input: 5
Example Output:

# Expected Output: 120
# Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120
UNDERSTAND
    what is meant by the base case and the recursive case?
        as we are doing multiple recursive steps well get closer and closer to the base case which will be our stopping point.
        the recursive case is what data we use to determine the next step in our recursion
    what is our recursive case going to look like?
PLAN
    use base and recursive cases approapriately
    def factorial(n):
        if n <= 0:
            return 1
        return n*fact(n-1))
IMPLEMENT
''' 
def factorial(n):
    # assuming n is never negative
    if n==0:
        return 1
    return n*factorial(n-1)
# 5 -> 5 * fact(5-1)-> 5*4*fact(4-1)->5*4*3*fact(3-1)->5*4*3* 2*fact(2-1) -> 5*4*3*2* 1*fact(0) -> 5*4*3*2*1*1
print(factorial(5))
# TIME COMPLEXITY -> O(N), processing one element everytime but we are calling the function within itself n times
# SPACE COMPLEXITY -> O(N), we are not making any new memory allocations for data strucutre or anything like that, BUT 
# we are calling the function repeatly n times, there fore adding to the callstack n times so O(N)
# CALL STACK counts as space added
print('END FO QUESTION 2')
'''
Problem 3: Recursive Sum
Without using the built-in sum() function, write a function sum_list() that calculates the sum of all values in a list recursively.

What is the time complexity of this function? What is the space complexity?

def sum_list(lst):
	pass
Example Usage:

# Example Input: [1, 2, 3, 4, 5]
Example Output:

# Expected Output: 15
# Explanation: 1 + 2 + 3 + 4 + 5 = 15
UNDERSTAND
    what would our base case/last case look like?
        if not lst:
            return 0
    how can we think about this recursively? what values would shrink or increase every step to get closer to our base case?
    what methods can we use to shorten our problem set into a smaller one?
        list slicing
        forwards lst[1:]
        backwards lst[:1]
    what would our recursive case look like?
PLAN
    base case:
    if lst is empty:
        return 0
    recursive case:
    return smaller list either shrinking forwards or back
    return lst[0]+ sum_list(lst[1:])
IMPLEMENT
'''
def sum_list(lst):
    if not lst:
        # if we have an empty list dont add anything to sum
        return 0
    return lst[0]+sum_list(lst[1:])
print(sum_list([1,2,3,4,5]))
# TIME COMPLEXITY -> 0(N), because the function calls itself n times and its only processing the first element of every subsequent list
# SPACE COMPLEXITY -> 0(N), were not making any new memoery allocations for a data strucutre or anything BUT we are calling the function n times
# therefore adding to the call stack n times, so space complexity is dependent on n (length of list)
print('END OF QUESITON 3')
# lst =[1,2,3,4,5]
# print(lst[:-1])
# print(lst[1:])
# newlst = lst[1:]
# print(newlst[1:])
'''
Problem 4: Recursive Power of 2
Given an integer n, return True if n is a power of two. Otherwise, return `False``.

An integer n is a power of two if there exists an integer x such that n == 2ˣ.

Solve the problem recursively. What is the time complexity of this function? What is the space complexity?

def is_power_of_two(n):
	pass
UNDERSTAND
    what do power of two look like?
        look for an x(power of)where the result is n
        2**0 = 1 -> this is our base case
        2**1 = 2
        2**2 = 4
        2**3 = 8
        2**4 = 16
        2**5 = 32
        
        what can we take away from this? what relation do you see?
            *in order for a number n to be a power of two, it has to be completely divisble by 2, no remainder*
            *if a number is not divisble by 2, then we can rule it out completely*
            say we have n == 33 and 33%2!=0 so False
            say we have n == 32 and 32%2==0 so True but we must check all of its n//2 values as well to make sure they are also divisble by 2.
            power of 2s must be divisle by 2 and divisble by 2 numbers must be even, but evens dont guarantee being a power of 2
    --->   power of 2s must be even, BUT evens dotn guarantee being a power of 2, ex: 6, 18, 30
    NEGATIVE CASE:
        n = 6
        6%2 == 0 -> move on to next recursive step, n//2 n = 3
        3%2 !=0 -> return False
        6 is not a power of 2
    POSITIVE CASE:
        n = 96
        96%2==0 -> move on n//2 n = 48
        48%2 == 0 -> move on n//2 n == 24
        24%2==0 -> move on n//2 n==16
        16%2 ==0 -> move on n//2 n==8
        8%2==0 -> move on n//2 n==4
        4%2==0 -> move on n//2 n==2
        2%2==0 -> move on n//2 n==1
        n==1 weve reached base case , return True
    96 is a power of 2


    how would we solve this iteratively?
    break this problem down to the very last step
        what would our base case look like?
    what would our recursive case have to look like to reach the base case?
PLAN
    base case:
        # if weve reached n==1
        if n==1:
            return True
        else if we reach a negative or IF at any point we have something not divisible by 2 then:
            return False
        
        return is_power_of_two(n//2), try again with n divided by 2
IMPLEMENT
'''

def is_power_of_two(n):
    # Base case: 1 is 2^0, so it's a power of two
    if n == 1:
        return True
    # If n is less than 1 or not divisible by 2, it’s not a power of two
    elif n <= 0 or n % 2 != 0:
        return False
    # Recursive step: divide n by 2 and check again
    # we use floor division to make sure were working with integers instead of floats at every step
    return is_power_of_two(n // 2)
print(is_power_of_two(5))
print(is_power_of_two(6))
print(is_power_of_two(8))
print(is_power_of_two(1))
print('END OF QUESTION 4')
'''
Problem 5: Binary Search I
Binary search is a searching algorithm that allows us to efficiently find the index of a given value within a sorted list. Given the pseudo code for binary search below, implement an iterative (non-recursive) implementation of binary search. There is also a recursive alternative that we’ll cover in the session 2 problem set!

Evaluate the time and space complexity of your implementation.

def binary_search(lst, target):
	# Initialize a left pointer to the 0th index in the list
	# Initialize a right pointer to the last index in the list
	
	# While left pointer is less than right pointer:
		# Find the middle index of the array
		
		# If the value at the middle index is the target value:
			# Return the middle index
		# Else if the value at the middle index is less than our target value:
			# Update pointer(s) to only search right half of the list in next loop iteration
		# Else
			# Update pointer(s) to only search left half of the list in next loop iteration
	
	# If we search whole list and haven't found target value, return -1

def binary_search(lst, target):
	pass
Example Usage:

# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
Example Output:

# Expected Output: 5
# Explanation: 11 has index 5 in the list
UNDERSTAND 
    when does binary search actually work?
    explain binary search in simple terms, dictionary
    how does the problem set we use change between every iteration of the search?
PLAN
    follow the psuedo code and implement

    def binary_search(lst, target):
	# Initialize a left pointer to the 0th index in the list
	# Initialize a right pointer to the last index in the list
	
	# While left pointer is less than right pointer:
		# Find the middle index of the array
		
		# If the value at the middle index is the target value:
			# Return the middle index
		# Else if the value at the middle index is less than our target value:
			# Update pointer(s) to only search right half of the list in next loop iteration
		# Else
			# Update pointer(s) to only search left half of the list in next loop iteration
	
	# If we search whole list and haven't found target value, return -1
IMPLEMENT
'''
def binary_search(lst,target):
    left = 0
    right = len(lst) - 1
    while left<=right:
        mid = left+(right-left)//2
        if lst[mid] == target:
            return mid
        elif lst[mid]<target:
            print(lst[mid],' is less than ', target,' moved left up')
            left = mid+1
        else:
            print(lst[mid],' is greater than ', target, ' moved right down')
            right = mid - 1
    return -1
print(binary_search([1,2,3,4,5,6,7,8,9,10],10))
# iter 1
# mid = 5 < 10 so left up, l = 6 right = 10
# [6,7,8,9,10]
# iter 2
# mid = 8 <10 so left up, l = 9, right = 10
# [9,10]
# iter 3
# mid = 9<10 so left up l= 10, right = 10
# [10]
# iter 4 
# mid =10 return index for 10
print('END OF QUESTION 5')





