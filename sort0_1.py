
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

# It makes soup sandwiches. 
#def soupSandwichMaker(arr):



arr: list = [0, 1, 2, 0, 1, 2]
sort_sequence: list = []

for number in arr:
    if number == 0:
        sort_sequence.append(number)
        

for number in arr:
    if number == 1:
        sort_sequence.append(number)
       

for number in arr:
    if number == 2:
        sort_sequence.append(number)
        
arr = sort_sequence

#print(arr)  
print(sort_sequence) 







