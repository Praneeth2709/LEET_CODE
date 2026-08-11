class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []
        for i in range(2 * n):
            current_idx = i % n
            current_value = nums[current_idx]
            while stack and nums[stack[-1]] < current_value:
                prev_idx = stack.pop()
                ans[prev_idx] = current_value
            if i < n:
                stack.append(current_idx)
        return ans
        