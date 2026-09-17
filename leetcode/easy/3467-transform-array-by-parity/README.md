# Transform Array by Parity

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `nums`. Transform `nums` by performing the following operations in the  **exact**  order specified:

- Replace each even number with 0.
- Replace each odd numbers with 1.
- Sort the modified array in non-decreasing order.

Return the resulting array after performing these operations.

 

 **Example 1:** 

 **Input:**  nums = [4,3,2,1]

 **Output:**  [0,0,1,1]

 **Explanation:** 

- Replace the even numbers (4 and 2) with 0 and the odd numbers (3 and 1) with 1. Now, nums = [0, 1, 0, 1].
- After sorting nums in non-descending order, nums = [0, 0, 1, 1].

 **Example 2:** 

 **Input:**  nums = [1,5,1,4,2]

 **Output:**  [0,0,1,1,1]

 **Explanation:** 

- Replace the even numbers (4 and 2) with 0 and the odd numbers (1, 5 and 1) with 1. Now, nums = [1, 1, 1, 0, 0].
- After sorting nums in non-descending order, nums = [0, 0, 1, 1, 1].

 

 **Constraints:** 

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 1000

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.2 MB (beats 56.47%)  
**Submitted:** 2026-09-17T06:13:01.810Z  

```py
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            if x % 2 == 0:
                ans.append(0)
            else:
                ans.append(1)
        
        ans.sort()
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/transform-array-by-parity/)