class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen_nums = []
        for val in nums:
            if val in seen_nums:
                return True
            seen_nums.append(val)
        return False