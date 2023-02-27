class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphabetMap = {}
        counter = 0

        if not s:
            return True

        for x in s:
            if ord(x) in range(65, 91):
                alphabetMap[counter] = chr(ord(x)+32)
                counter+=1
            elif ord(x) in range(97, 123):
                alphabetMap[counter] = x
                counter+=1
            elif ord(x) in range(48, 58):
                alphabetMap[counter] = x
                counter+=1

        leftCounter, rightCounter = 0, len(alphabetMap) - 1
        while leftCounter<rightCounter:
            if alphabetMap[leftCounter] != alphabetMap[rightCounter]:
                return False
            leftCounter+=1
            rightCounter-=1
        return True

"""
The entire motivation to write this code this way to get you introduced with the ASCII code of an uppercase, lowercase letter or a digit.
Remember ASCII code for A-Z is within range 65-90. For a-z the range varies from 97 to 122.
For the digits 0-9 it is simply 48-57.

The first conditional statement if ord(x) in range(65, 91): checks if the current character x is an uppercase letter. If so, it adds the corresponding lowercase letter to the alphabetMap dictionary using the counter variable as the key, and increments counter by 1. This converts the uppercase letter to lowercase and adds it to the alphabetMap dictionary.

The second conditional statement elif ord(x) in range(97, 123): checks if the current character x is a lowercase letter. If so, it adds the character to the alphabetMap dictionary using the counter variable as the key, and increments counter by 1. This adds the lowercase letter to the alphabetMap dictionary.

The third conditional statement elif ord(x) in range(48, 58): checks if the current character x is a digit. If so, it adds the digit to the alphabetMap dictionary using the counter variable as the key, and increments counter by 1. This adds the digit to the alphabetMap dictionary.

Time Complexity: O(n)
Space Complexity: O(n)
"""


# Solution 2
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        # This line takes a string and returns a new string containing only
        # lowercase alphanumeric characters from the original string.
        s = ''.join(x.lower() for x in s if x.isalnum())

        leftCounter, rightCounter = 0, len(s) - 1
        while leftCounter<rightCounter:
            if s[leftCounter] != s[rightCounter]:
                return False
            leftCounter+=1
            rightCounter-=1
        return True
    
"""
Time Complexity:
The time complexity of this code is O(n),
where n is the length of the input string s.
This is because the code iterates over the string
once to remove non-alphanumeric characters
and once to check for palindromicity, both of which take linear time.

Space Complexity:
The space complexity of this code is O(n),
where n is the length of the input string s.
This is because the code creates a new string
containing only alphanumeric characters, which could potentially be as long
as the original string s. The two integer variables created
in the code take constant space and do not depend
on the length of the input string.
"""