# Single Number II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums` where every element appears  **three times**  except for one, which appears  **exactly once**.  *Find the single element and return it*.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

 **Example 1:** 

```
Input: nums = [2,2,3,2]
Output: 3

```

 **Example 2:** 

```
Input: nums = [0,1,0,1,0,1,99]
Output: 99

```

 

 **Constraints:** 

- 1 <= nums.length <= 3 * 104
- -231 <= nums[i] <= 231 - 1
- Each element in nums appears exactly three times except for one element which appears once.

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 45.71%)  
**Memory:** 20.6 MB (beats 63.12%)  
**Submitted:** 2026-09-16T13:29:26.013Z  

```py
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()

        for i in range(0, len(nums) - 1, 3):
            if i + 1 >= len(nums) or nums[i] != nums[i + 1]:
                return nums[i]

        return nums[-1]
```

---

[View on LeetCode](https://leetcode.com/problems/single-number-ii/)