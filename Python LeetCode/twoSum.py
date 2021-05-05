class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found_values = set()
        for a in nums:
            if target - a in found_values:
                x = nums.index(target - a)
                nums[x] = nums[nums.index(a)] - 1
                return [x,nums.index(a)]
            found_values.add(a)
        return [0,0]