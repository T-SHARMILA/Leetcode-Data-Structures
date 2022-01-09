#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        doubles={'CM':900,'CD':400,'XL':40,'XC':90,'IV':4,'IX':9}
        singles={'M':1000,'D':500,'L':50,'C':100,'V':5,'X':10,'I':1}
        integer=0
        i=0
        while(i<len(s)):
            if i<len(s)-1 and s[i:i+2] in doubles:
                integer+=doubles[s[i:i+2]]
                i+=2
            else:
                integer+=singles[s[i]]
                i+=1
        return integer

        
# @lc code=end

