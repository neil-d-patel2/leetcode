#Variables are dynamically types, the following is a completely fine operation.

n = 0

n = "abc"

this is because python determines types at runtime. 

Multiple assignments: (The following is completely valid)

n,m = 0, "abc"

Increment:

n += 1 (cannot do n++, unlike other languages. This is due to the python interpreter)

None is the same as null in other languages

if statements:

if n > 2:
    print(n)
elif:
    n *= 9
else:
    n += 2

However: Parentheses needed for multi-line conditions

if (n > 2 && n < 5):
    print("Success")

In python, && == and 

In python, or == ||

while loops (similar to most languages):

while n > 5:
    print(n)

for loops:

for i in range (5):
    print(i)

THIS OUTPUTS 0 to 4, its its equal to for(int i = 0; i < 5; i++) 

for i in range(2,6):
    print(i) # would print 2,3,4,5

lets say that we wanted to print from 5 to 2:

for i in range(5,1,-1): # tells python to decremement, not increment 
    print(i)

# Division is decimal by default

print(5 / 2) => 2.5 

to do integer Division

print( 5 // 2) => 2

most languages round towards 0 by default, so negative numbers round down 

print(-3 // 2) => -2 

Modulo:

print(10 % 3) => 1

To be consistent with other languages:

import math
print(math.fmod(-10,3)) => -1 

print(math.floor(3/2)) => 1

print(math.ceiling(3/2)) => 2

print(math.sqrt(2)) => sqrt(2)

print(math.pow(2,3))

If you ever need a max or min number,

float("inf")
float("-inf")

***Important***

Arrays:

arr = [1,2,3]

arr.append(4)
arr.append(5)
print(arr) => 1,2,3,4,5
print(arr.pop()) => 1,2,3,4

arr[0] = 3

print(arr) => 0,2,3,4

***

To initialize an arr of size n with default value of 1 

n = 5
arr = [1] * n 

Indexing:

***Important***

-1 is not out of bounds in python

arr = [1,2,3]
print(arr[-1]) => 3

***Sublists(aka slicing)*** (also important trick)

arr = [1,2,3,4]
#say i want the elements from index 2 to index 3

arr = [2:4] # would return 2,3,4

Unpacking:

a,b,c = [1,2,3]

#super helpful when you have to go through pairs or something 

looping throw arrays 

***IMPORTANT***
Zip:

nums1 = [1,3,5]
nums1 = [2,4,6]

for n1,n2 in zip(nums1,nums2):
    print(n1,n2)

# This would print the following:

12
34
56


# With index 
for i in range(len(nums)):
    print(nums[i])
# Without the index
for n in nums:
    print(n)

# with the index and the value 
for i,n in enumerate(nums):
    print(i,n)
#
nums = [1,2,3]
nums.reverse() # 3,2,1

***SORTING*** Lists

arr = [5,4,7,3,8]
arr.sort()
print(arr) # 3,4,5,7,8
arr.sort(reverse = True) # would sort in reverse order 

***If you want to do a custom sort***

***arr.sort(key=lambda x: len(x))***

#List comprehension

arr = [i for i in range(5)]
print(arr) # [0,1,2,3,4]

# For 2-d lists, use the list creation shorthand. Eg, for a 4x4 2d list

arr = [[1] * 4 for i in range(4)]

this would inititalize each row to a row of 4 1's.

[1,1,1,1,
1,1,1,1,
1,1,1,1,
1,1,1,1]

# You can slice string, however, they are immutable

s = "abs"
print(s[0:2]) $ prints ab

s[0] = "A" # is not allowed in python

# Concat

s += "def"
print(s) # would print abcdef

Numeric strings can be converted to ints, and ints can be converted to strings

print(int("123") + int("123")) # prints 246

print(str(123) + str(123)) # prints 123123

# if you need the ascii value of a char

print(ord("a"))
print(ord("b"))

strings = ["ab","bc","ef"]

print("".join(strings))

# Data Structures 

Queues, double ended queues by default 

from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
print(queue)# prints 3,2,1 (adds to the BACK of the queue)

queue.popleft() # removes from the LEFT of the queue 2,1
print(queue)
queue.appendleft() 3,2,1

queue.pop() # removes from from of the queue (normal) 3,2

# Hashset Note: ALL sets in python are hashsets, giving them O(1) lookup, insertion, removal!

mySet = set()

mySet.add(1)
mySet.add(2)

print(mySet) [1,2]

# to check if a number if in the set

print(1 in mySet) # Would print True 
mySet.remove(2)
print(mySet) # prints 1

#list to set
print(set[1,2,3])

print(set[i for i in range(5)]) # prints [0,1,2,3,4]

# Hashmaps (AKA dicts, theyre just key value pairs)

myMap["alice"] = 88
myMap["bob"] = 77

print(len(myMap)) = 2

print(myMap["alice"]) # prints 88
myMap.pop("alice") => removes kvp with key alice

print("alice" in myMap) # prints True 

myMap = {"alice": 90, "bob": 80} # another way to initialize a hashmap

***Dict comprehension***

myMap = { i: 2*i for i in range 3}

0,0
1,2
2,4

# Looping through a map ***THREE WAYS***

for key in myMap:
    print(key, myMap[key])

for val in myMap.values):
    print(val)

for key,val in myMap.items():
    print(key,val)























