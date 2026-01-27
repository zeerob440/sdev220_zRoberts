
'''
Sort 0s, 1s and 2s

sort0_1.py sorts a list in ascending order without using sort.  
Proudly Engineered by Zachary Roberts 26 JAN 2026

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

arr: list = [0, 1, 2, 0, 1, 2]

sort_sequence: list = []

for number in range(len(arr)):
    
    if number <= 0:
        sort_sequence.append(number)
    if number <= 1:
        sort_sequence.append(number)
    if number <= 2:
        sort_sequence.append(number)

print(sort_sequence)











