'''
bin_search.py- it searches sorted arrays for a target value and returns the index in which the target is located.

Proudly Engineered by Zachary Roberts 27 JAN 2026
"It's like looking for a needle in a stack of needles."

SPECIFICATIONS:
Given a sorted array arr[] and an integer k, find the position(0-based indexing) at which k is present in the array using binary search. If k doesn't exist in arr[] return -1. 

Note: If multiple occurrences are there, please return the smallest index.

Input: arr[] = [1, 2, 3, 4, 5], k = 4
Output: 3
Explanation: 4 appears at index 3.

Input: arr[] = [11, 22, 33, 44, 55], k = 445
Output: -1
Explanation: 445 is not present.

Input: arr[] = [1, 1, 1, 1, 2], k = 1
Output: 0
Explanation: 1 appears at index 0.

'''
# commence testing structures to make this work.
target: int = 4  
arr: list= [1, 2, 3, 4, 5]

half: int = ((len(arr)) // 2)

for index, value in (enumerate(arr)):
   if value == target:
    print(index)
    break