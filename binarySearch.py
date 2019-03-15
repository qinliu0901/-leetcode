# -*- coding: utf-8 -*-
"""
    binary search二分查找
    @author: qinliu
    keypoints:
    1. start+1 < end --->这样的写法比较通用，还适合于找到数值插入位置，不会死循环
    2. mid = int(start + (end - start)/2) --->当start与end较大时，start + end可能会溢出
    3. nums[mid] =>< target ---> 判断目标值与mid
    4. nums[start]nums[end] ?= target --->从while循环出来之后不是相交就是相邻

"""

# 704. 二分查找 [1,2,3,4] 3  --> 2
# https://leetcode-cn.com/problems/binary-search/
class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start+1 < end:
            mid = int(start + (end - start)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        



# 4. 寻找两个有序数组的中位数 
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/

class Solution:
    """找到两个数组中的第k大的元素，当nums1[k//2 - 1]<nums2[k//2 - 1]时，
    说明nums1[k//2 - 1]前面的数都位于合并数组的前k个,所以可挪动nums1的起始位置"""
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1) + len(nums2)
        if n % 2 ==1:
            return self.findKth(nums1, nums2, n//2 + 1)
        else:
            left = self.findKth(nums1, nums2, n//2)
            right = self.findKth(nums1, nums2, n//2 + 1)
            return (left + right)/2.0
        
    def findKth(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k-1]
        if len(nums2) == 0:
            return nums1[k-1]
        if k ==1:
            return min(nums1[0], nums2[0])
        a = nums1[k//2 - 1] if len(nums1) >= k//2 else None
        b = nums2[k//2 - 1] if len(nums2) >= k//2 else None
        
        if b is None or (a is not None and a<b):
            return self.findKth(nums1[k//2:], nums2, k - k//2)
        return self.findKth(nums1, nums2[k//2:], k - k//2)


# 35. 搜索插入位置
# https://leetcode-cn.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums, target) :
        start = 0
        end = len(nums) - 1
        if len(nums) == 0:
            return 0
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        
        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        return len(nums)


# 34. 在排序数组中查找元素的第一个和最后一个位置
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
class Solution:
    # 用两次二分法，找到左右边界
    def searchRange(self, nums, target):
        if not nums:
            return [-1,-1]
        start, end = 0, len(nums) - 1
        left, right = -1, -1
        # 找右边界
        while start +1 < end:
            mid = start + (end - start)//2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
                
        if nums[start] == target:
            right = start
        if nums[end] == target:
            right = end
              
        # 找左边界
        start, end = 0, len(nums) - 1
        while start +1 < end:
            mid = start + (end - start)//2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
                
        if nums[end] == target:
            left = end
        if nums[start] == target:
            left = start

        if left == -1 and right == -1:
            return [-1,-1]
        return [left,right]
            
            