# Left and Right Sum Differences

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a  **0-indexed**  integer array `nums` of size `n`.

Define two arrays `leftSum` and `rightSum` where:

- leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
- rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.

Return an integer array `answer` of size `n` where `answer[i] = |leftSum[i] - rightSum[i]|`.

 

 **Example 1:** 

```
Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

```

 **Example 2:** 

```
Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].

```

 

 **Constraints:** 

- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 70.85%)  
**Memory:** 19.6 MB (beats 5.78%)  
**Submitted:** 2026-09-13T08:53:35.904Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/left-and-right-sum-differences/)