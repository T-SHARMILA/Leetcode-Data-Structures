#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x>0 and x%10==0):
            return False
        revert=0
        while(x>revert):
            revert=revert*10+x%10
            x=x//10
        return revert==x or x==revert//10




        
# @lc code=end

