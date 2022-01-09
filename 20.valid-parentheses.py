#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        match={'{':'}','(':')','[':']'}
        stack=[]
        for c in s:
            if c in match:
                stack.append(c)
            elif not stack or match[stack.pop()]!=c:
                return False
        return len(stack)==0

        
# @lc code=end

