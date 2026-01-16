class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        arr = [i +1 for i in range(n)]
        def helper(arr, start_index):
            if len(arr)==1:
                return arr[0]
            index_to_remove = (start_index + k-1) % len(arr)
            del arr[index_to_remove]
            return helper(arr,index_to_remove)
        return helper(arr,0)
    
    #second approach using josephus problem formula
    class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        survivor = 0
        for i in range(2, n+1):
            survivor = (survivor + k)% i
        return survivor +1