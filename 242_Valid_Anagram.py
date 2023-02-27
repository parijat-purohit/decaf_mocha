class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        characterMap = {}
        for ch in s:
            if ch not in characterMap:
                characterMap[ch] = 1
            else:
                characterMap[ch] += 1
        for ch in t:
            if ch not in characterMap:
                return False
            else:
                characterMap[ch] -= 1
                if characterMap[ch] == 0:
                    characterMap.pop(ch)
        if characterMap:
            return False
        return True
"""
Time Complexity:
The time complexity of the solution is O(m + n),
where m and n are the lengths of the input strings s and t, respectively.
This is because the code iterates through both input strings once in two separate loops.
In the first loop, each character in string s is added to the characterMap dictionary,
which takes O(m) time. In the second loop, each character in string t is checked against
the characterMap dictionary, and then, if the character exists in the dictionary,
the count is decremented, which also takes O(n) time.

The space complexity of my solution is O(k), where k is the number of unique characters
in the input strings s and t. This is because the characterMap dictionary could potentially
store all k unique characters, each with a count of 1. In the worst-case scenario where all
characters in both strings are unique, the size of the dictionary will be k,
leading to a space complexity of O(k).

REMEMBER:
If I use a list to store the characters instead of a dictionary, the time complexity of my
solution would increase to O(m * n), where m and n are the lengths of the input strings s and t,
respectively. This is because for each character in string t, I would need to iterate over the
list of characters in string s to find a matching character. Since the worst-case scenario is
when no matching character is found in the list, I would need to iterate over the entire list of
characters in string s for each character in string t, leading to a time complexity of O(m * n).

Therefore, using a list to store the characters would not be an optimal solution for this problem,
and it would result in a slower algorithm. The dictionary/hashmap approach is a more efficient way
to store and lookup characters because it allows for constant-time lookup, whereas searching for a
character in a list requires linear time.
"""
