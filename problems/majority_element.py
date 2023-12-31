#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times.
#  You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

#First Approach

#THIS IS IN PYTHON 3
import statistics

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mode = statistics.mode(nums)
        return mode

    #Assuming they don't want to use statistics


    # One approach assumes that the majority element
    # will always be in the middle of the array
    # since the majority element is whatever element is present more than
    # n/2
    def majorityElement(self, num: List[int]) -> int:
        nums.sort() # Sort the elements
        n = len(nums)
        # middle index = n // 2
        # return nums[n//2]
        middle_index = n // 2
        return nums[middle_index]

######## Using a Hash Map

    # Method is to use a hash map to count the occurances of
    # each element in the array, and find the one that is
    # present more than n/2 times.
    def majorityElement(self, num: List[int]) -> int:
        n = len(nums)
        m = defaultdict(int) # This is the syntax for a hashmap in python

        for num in nums:
            m[nums] += 1 # for each num: it will iterate over the hashmap
            # This will create an entry with key: num and value: 0
            # or increment by 1
        mid_index = n//2
        for key, value in m.items():
            if value > mid_index:
                return key

        return 0
        # if no majority element is found, returns 0
        # This covers the edge case that the mode is not the majority like [1,1,2,3,4]
        # Mode is 1, but 1 does not appear > n//2
