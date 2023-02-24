class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            if target - n in nums and i!=nums.index(target-n):
                return [i, nums.index(target-n)]

""" 
Time Complexity:
The time complexity of this code is O(n^2) because it has a nested loop.
The outer loop iterates through each element of the list, and the inner loop
checks whether the target minus the current element exists in the list.
Since the inner loop also iterates through the entire list,
the time complexity becomes O(n^2).

Specifically, for each iteration of the outer loop, the inner loop iterates
through the entire list to check whether the target minus the current element
exists in the list. Therefore, the worst-case scenario occurs when the target
minus the current element is at the end of the list, which requires the inner
loop to iterate through the entire list. In this case, the total number of
iterations is n*(n-1)/2, which is proportional to n^2.
"""
"""
Space Complexity:
The space complexity of this code is O(1) because the algorithm does not use
any additional data structures or arrays to store elements besides the input
nums and target. The algorithm only uses a constant amount of space to store
two integers, i, index of target-n, and the result list of size 2. Therefore,
the space complexity is O(1), which is constant and does not depend on the
input size.
"""