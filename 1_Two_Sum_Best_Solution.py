class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i, n in enumerate(nums):
            if target - n in hashMap:
                return [hashMap[target - n], i]
            hashMap[n] = i


"""
The above solution is not mine. I found it on youtube.
https://www.youtube.com/watch?v=KLlXCFG5TnA

Time Complexity:
The point I want to discuss is that, instead of checking a value in the list
we are checking a value in the hashMap which is a dictionary (key-value pair).
Remember  The time complexity of looking up an element in a list is O(n),
where n is the number of elements in the list, because it requires iterating
through the list until the target element is found or the end of the list is reached.

In contrast, the time complexity of looking up an element in a dictionary (or hash map)
is O(1) on average, because it involves computing the hash code of the target key and using
it to locate the corresponding value in the dictionary, which takes constant time on average,
regardless of the size of the dictionary.

Therefore, using a dictionary for lookup operations can be much faster than using a list for large datasets,
especially if the lookup operations are frequent or if the dataset is frequently updated.

Space Complexity:
The space complexity is O(n) as we are now using a hashMap dictionary which could use each and
every element of the nums.
"""