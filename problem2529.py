'''
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

Example 1:

Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
Example 2:

Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
'''

# Approach 1 if interviewer is ok to use inbuilt methods/functions
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
         neg_count = bisect_right(nums, -1)
         pos_count = len(nums) - bisect_right(nums, 0)
         return max(neg_count, pos_count)

# Approach 2 if interviewer is not ok to use inbuilt functions
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Find the first positive number's index
        def first_positive_index():
            i, j = 0, len(nums)
            while i < j:
                mid = (i + j) // 2
                if nums[mid] <= 0:  # Move right if nums[mid] is negative or zero
                    i = mid + 1
                else:
                    j = mid
            return i  # First positive index
        
        # Find the first zero's index (or first non-negative number)
        def first_non_negative_index():
            i, j = 0, len(nums)
            while i < j:
                mid = (i + j) // 2
                if nums[mid] < 0:  # Move right if nums[mid] is negative
                    i = mid + 1
                else:
                    j = mid
            return i  # First non-negative index

        neg_count = first_non_negative_index()
        pos_count = len(nums) - first_positive_index()
        return max(neg_count, pos_count)
