class Solution(object):
    def findTheWinner(self, n, k):
        """
        Find the winner in a circular elimination game using recursion.
        :type n: int
        :type k: int
        :rtype: int
        """
        arr = [i + 1 for i in range(n)]
        
        def helper(arr, start_index):
            if len(arr) == 1:
                return arr[0]
            index_to_remove = (start_index + k - 1) % len(arr)
            del arr[index_to_remove]
            return helper(arr, index_to_remove)
        
        return helper(arr, 0)

    def findTheWinnerJosephus(self, n, k):
        """
        Find the winner using Josephus problem formula.
        :type n: int
        :type k: int
        :rtype: int
        """
        survivor = 0
        for i in range(2, n + 1):
            survivor = (survivor + k) % i
        return survivor + 1