class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenthesesMap = {')': '(', '}': '{', ']': '['}
        stack = []
        for x in s:
            if x in parenthesesMap.values(): # dictionary value
                stack.append(x)
            elif not stack or parenthesesMap[x] != stack.pop(): #dictionary key and stack top item comparison
                    return False
        return not stack  # stack could have inputs like '({'

"""
Time complexity: The time complexity of this code is O(n), where n is the length of the input string s.
This is because the code processes each character in the input string exactly once,
performing a constant amount of work for each character. Dictionary lookup operation is O(1).

Space complexity: The space complexity of this code is also O(n),
where n is the length of the input string s.
This is because the maximum size of the stack is equal to the number of opening parentheses in the input string,
which can be at most n/2 if the input string is well-formed.
In the worst case scenario, it would be equal to n.
Therefore, the space required to store the stack is proportional to the
number of opening parentheses in the input string, which gives a space complexity of O(n).
Additionally, the parenthesesMap dictionary has a constant size,
so its contribution to the overall space complexity is also constant.

"""