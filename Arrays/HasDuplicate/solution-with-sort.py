class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sorted_nums = sorted(nums)
        i = 0
        while i < len(sorted_nums) - 1:
            if sorted_nums[i] == sorted_nums[i+1]:
                return True
            i += 1
        return False