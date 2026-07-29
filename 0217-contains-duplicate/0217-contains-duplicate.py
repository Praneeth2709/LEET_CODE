class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] == nums[left + 1] or nums[right] == nums[right - 1]:
                return True
            left += 1
            right -= 1
        return False