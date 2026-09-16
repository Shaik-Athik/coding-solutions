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
**Runtime:** 1041 ms (beats 5.10%)  
**Memory:** 20.6 MB (beats 46.38%)  
**Submitted:** 2026-09-16T13:22:05.159Z  

```py
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = []
        for i in nums:
            if i not in ans:
                ans.append(i)
        
        for i in ans:
            if nums.count(i)==ans.count(i):
                return i
```

---

[View on LeetCode](https://leetcode.com/problems/single-number-ii/)