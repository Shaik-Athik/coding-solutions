# Single Number III

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in  **any order**.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

 **Example 1:** 

```
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

```

 **Example 2:** 

```
Input: nums = [-1,0]
Output: [-1,0]

```

 **Example 3:** 

```
Input: nums = [0,1]
Output: [1,0]

```

 

 **Constraints:** 

- 2 <= nums.length <= 3 * 104
- -231 <= nums[i] <= 231 - 1
- Each integer in nums will appear twice, only two integers will appear once.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 65.95%)  
**Memory:** 20.8 MB (beats 62.92%)  
**Submitted:** 2026-09-16T13:52:30.247Z  

```py
class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        diff = xor & -xor

        a, b = 0, 0

        for num in nums:
            if diff & num:
                a ^= num
            else:
                b ^= num
        
        return [a,b]
```

---

[View on LeetCode](https://leetcode.com/problems/single-number-iii/)