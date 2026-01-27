
'''
Sort 0s, 1s and 2s

sort0_1.py sorts a list in ascending order without using sort.  

Proudly Engineered by Zachary Roberts 26 JAN 2026

"Soup sandwiches come in all shapes and sizes." - DS Gazely D Company 2/54 Infantry Infantry Training Brigade 2004

SPECIFICATIONS:
Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
Note: You need to solve this problem without utilizing the built-in sort function.

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s, 1s and 2s are segregated into ascending order.
Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: 0s, 1s and 2s are segregated into ascending order.
'''

# It unmakes soup sandwiches. 
def unSoupSandwichMaker(arr):
    # stores soup sandwich ingredients, reconstitutes order. (actual sandwiches) 
    sort_sequence: list = []
    # get 0's into sort_sequence
    for number in arr:
        if number == 0:
            sort_sequence.append(number)
        
    # get 1 into sort_sequence
    for number in arr:
        if number == 1:
            sort_sequence.append(number)
       
    # get 2's into sort_sequence
    for number in arr:
        if number == 2:
            sort_sequence.append(number)

    # make arr == sort_sequence        
    arr = sort_sequence

    return print(arr)

arr: list = [0, 1, 2, 0, 1, 2]

unSoupSandwichMaker(arr)

arr: list = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] 

unSoupSandwichMaker(arr)








