# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements
# in the order they were present in nums initially.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        for index in range(1, len(nums)):
            if nums[index] != nums[k-1]: # THIS ALSO WORKS WITH nums[k-1] instead of index-1
                nums[k] = nums[index]
                k += 1
        return k

# This uses the two pointer approach. In the case that the
# input is not sorted, use nums.sort() **Unless they want to preserve the order

    def removeDuplicatesTwo(self, nums) -> int:
        # This one is different:
        # Given an integer array nums sorted in non-decreasing order,
        # remove some duplicates in-place such that each unique element appears at most twice.
        # The relative order of the elements should be kept the same.
        # note: Because it's sorted, using a two pointer approach is good
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]: # use nums[k-2]
                nums[k] = nums[i]
                k += 1
        return k
