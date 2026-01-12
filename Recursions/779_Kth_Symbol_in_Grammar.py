# Problem: 779. K-th Symbol in Grammar
# Link: https://leetcode.com/problems/k-th-symbol-in-grammar/
# Topic: Recursion / Binary Tree Traversal logic

class Solution(object):
    """
    Intuition:
    The grammar follows a pattern where each row is the previous row followed by its complement.
    Row 1: 0
    Row 2: 0 1 (Row 1 + complement of Row 1)
    Row 3: 0 1 1 0 (Row 2 + complement of Row 2)
    Row 4: 0 1 1 0 1 0 0 1 (Row 3 + complement of Row 3)
    
    We can solve this by finding if 'k' falls in the first half (same as previous row) 
    or the second half (complement of previous row).
    """

    # Time Complexity: O(n) - We make one recursive call for each row.
    # Space Complexity: O(n) - Depth of the recursion stack.
    def kthGrammar(self, n, k):
        # Base Case: Row 1 always starts with 0
        if n == 1:
            return 0
        
        # Calculate the midpoint of the current row (2^(n-1) / 2)
        mid = 2**(n-2)
        
        # If k is in the first half, it's identical to the value in the previous row
        if k <= mid:
            return self.kthGrammar(n-1, k)
        
        # If k is in the second half, it's the complement of the value in the previous row
        else:
            res = self.kthGrammar(n-1, k - mid)
            return 1 if res == 0 else 0