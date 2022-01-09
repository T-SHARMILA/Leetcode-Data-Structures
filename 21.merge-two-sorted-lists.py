#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # iteratively
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=cur=ListNode(0)
        while list1 and list2:
            if list1.val<list2.val:
                cur.next = list1
                list1=list1.next
            else:
                cur.next = list2
                list2=list2.next
            cur=cur.next
        cur.next=list1 or list2
        return dummy.next
    #recursively
    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if None in list1 and list2:
            return list1 or list2
        if list1.val<list2.val:
            list1.next=self.mergeTwoLists1(list1.next, list2)
            return list1
        else:
            list2.next=self.mergeTwoLists1(list1,list2.next)
            return list2
    # in-place, iteratively
    def mergeTwoLists(self, list1, list2):
        if None in list1 and list2:
            return list1 or list2
        dummy=cur=ListNode(self,0)
        dummy.next=list1
        while list1 and list2:
            if list1.val <list2.val:
                list1=list1.next
            else:
                nxt=cur.next
                temp=list2.next
                list2.next=next
                list2=temp
            cur=cur.next
        cur.next =list1 or list2
        return dummy.next




        
# @lc code=end

