class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Store the keys we have already viewed
        seen_keys = {}
        # Iterate through the list of nums to see their key and value pairs
        for key, num in enumerate(nums):
            print(key, num)
            # Calculate the complement to the current num value needed to equal target
            complement = target - num
            print(complement)
            # The first iteration will not see anything in seen_keys but that is okay as we beging actually comparing on key #1 (as we begin at key #0)
            if complement in seen_keys:
                # If we find the complement in the seen_keys we will find it in the complements position, as we are storing the index in the position of the num value
                return [seen_keys[complement], key]
            # store the index in the position of the num value
            seen_keys[num] = key
            print(seen_keys)
        return [0,0]