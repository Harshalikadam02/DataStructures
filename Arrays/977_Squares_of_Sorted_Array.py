# Problem: 977. Squares of a Sorted Array
# Link: https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    # Approach 1: Brute Force (Square and Sort)
    # Time Complexity: O(n log n) | Space Complexity: O(n)
    def sortedSquares(self, array):
        n = len(array)
        res = [0] * n
        for i in range(n):
            res[i]= array[i]**2
        res.sort()
        return res

    # Approach 2: Optimized (Two Pointers)
    # Time Complexity: O(n) | Space Complexity: O(n)
    def sortedSquares_v2(self, array):
        n = len(array)
        res = [0] * n
        i, j = 0, n - 1
        
        for k in reversed(range(n)):
            if array[i]**2 > array[j]**2:
                res[k] = array[i]**2
                i += 1
            else:
                res[k] = array[j]**2
                j -= 1
        return res