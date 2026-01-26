class Solution(object):
    def isPalindrome(self, x):
        convert = str(x)
        return convert == convert[::-1]
sol = Solution()
print(sol.isPalindrome(121))
"""
:type x: int
:rtype: bool
"""
