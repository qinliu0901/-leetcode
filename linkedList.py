# -*- coding: utf-8 -*-
"""
    linked list 链表
    @author: qinliu
    keypoints:
    1. dummyNode虚拟节点方法
"""

# 21. 合并两个有序链表
# https://leetcode-cn.com/problems/merge-two-sorted-lists
# 非递归用虚拟节点的方法
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        temp = dummy
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        else:
            temp.next = l2
        return dummy.next

