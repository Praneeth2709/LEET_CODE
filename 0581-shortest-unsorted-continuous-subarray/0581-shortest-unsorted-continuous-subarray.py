class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max_so_far = float('-inf')
        min_so_far = float('inf')
        right = -1
        left = -1
        for i in range(len(nums)):
            if nums[i] < max_so_far:
                right = i
            else:
                max_so_far = nums[i]
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > min_so_far:
                left = i
            else:
                min_so_far = nums[i]
        if right == -1:
            return 0
        return right - left + 1