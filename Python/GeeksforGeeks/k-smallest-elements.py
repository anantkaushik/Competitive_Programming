"""
You are given an array of n-elements you have to find k smallest elements from the array but they must be in the 
same order as they are in given array and we are allowed to use only O(1) extra space.

Examples: 
Input : arr[] = {4, 2, 6, 1, 5}, 
            k = 3
Output : 4 2 1
Explanation : 1, 2 and 4 are three smallest 
numbers and 4 2 1 is their order in given array

Input : arr[] = {4, 12, 16, 21, 25}, 
            k = 3
Output : 4 12 16
Explanation : 4, 12 and 16 are 3 smallest numbers
and 4 12 16 is their order in given array
"""
def k_smallest_numbers(arr, k):
    for i in range(k, len(arr)):

        max_num = arr[k-1]
        pos = k-1
        for j in range(k-2, -1, -1):
            if arr[j] > max_num:
                max_num = arr[j]
                pos = j

        if arr[pos] > arr[i]:
            while pos < k-1:
                arr[pos] = arr[pos + 1]
                pos += 1

            arr[k-1] = arr[i]

    for i in range(k):
        print(arr[i], end=" ")
