class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n-1
        write_index = n-1
        while left <= right:
            left_square = nums[left]**2
            right_square = nums[right]**2
            if left_square > right_square:
                result[write_index] = left_square
                left+=1
            else:
                result[write_index] = right_square
                right-=1
            write_index -=1
        return result