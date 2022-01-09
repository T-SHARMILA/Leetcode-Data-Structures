#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if not strs:
    #         return ''
    #     strs.sort()
    #     first =strs[0]
    #     last=strs[-1]
    #     i=0
    #     while i<len(first) and i<len(last) and first[i]==last[i]:
    #         i+=1
    #     return first[:i]
        
    def longestCommonPrefix(self,strs:List[str])->str:
        l=list(zip(*strs))
        prefix=""
        for i in l:
            if len(set(i))==1:
                prefix+=i[0]
            else:
                break
        return prefix
# @lc code=end

