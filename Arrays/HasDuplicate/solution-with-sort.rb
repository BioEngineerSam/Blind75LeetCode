# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
    nums.sort!
    i = 0
    while i < nums.size do
        if nums[i] == nums[i+1]
            return true
        end
        i += 1
    end
    false
end