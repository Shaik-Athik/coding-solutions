class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftsum = [0] * n
        rightsum = [0] * n
        
        for i in range(1, n):
            leftsum[i] = nums[i - 1] + leftsum[i - 1]
            
        for i in range(n - 2, -1, -1):
            rightsum[i] = nums[i + 1] + rightsum[i + 1]
            
        ans = []
        
        for i in range(n):
            ans.append(abs(leftsum[i] - rightsum[i]))
            
        return ans