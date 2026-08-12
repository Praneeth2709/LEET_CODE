class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        no_deletion = arr[0]
        one_deletion = float('-inf')
        max_sum = arr[0]
        for i in range(1,n):
            prev_no_deletion = no_deletion
            no_deletion = max(arr[i], no_deletion + arr[i])
            one_deletion = max(prev_no_deletion, one_deletion + arr[i])
            max_sum = max(max_sum, no_deletion, one_deletion)
        return max_sum
        