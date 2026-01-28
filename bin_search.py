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
arr: list= [1, 2, 3, 4, 5]
k = 9
# commence testing structures to make this work.
def binarySearchIndices(arr, k): 
    # the left most index in a list
    leftest_index: int = 0
    #the right most index in a list
    rightest_index: int = (len(arr) - 1)
    while leftest_index <= rightest_index:
        center_index: int = leftest_index + (rightest_index - leftest_index) // 2

        if arr[center_index] < k:
            leftest_index = center_index + 1
        elif arr[center_index] > k:
            rightest_index = center_index -1
        else:
            return center_index
    #k: int = -1           
    return -1

    
if binarySearchIndices(arr, k) != -1:                
    k_index_location: str = f'{k} found at index: {binarySearchIndices(arr, k)}'
    print(k_index_location)
else:
    not_k_index_location: str = f'{k} does not exist. Search results in: {binarySearchIndices(arr, k)}'
    print (not_k_index_location)


