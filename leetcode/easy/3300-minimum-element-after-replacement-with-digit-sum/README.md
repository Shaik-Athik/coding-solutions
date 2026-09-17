# Minimum Element After Replacement With Digit Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `nums`.

You replace each element in `nums` with the  **sum**  of its digits.

Return the  **minimum**  element in `nums` after all replacements.

 

 **Example 1:** 

 **Input:**  nums = [10,12,13,14]

 **Output:**  1

 **Explanation:** 

`nums` becomes `[1, 3, 4, 5]` after all replacements, with minimum element 1.

 **Example 2:** 

 **Input:**  nums = [1,2,3,4]

 **Output:**  1

 **Explanation:** 

`nums` becomes `[1, 2, 3, 4]` after all replacements, with minimum element 1.

 **Example 3:** 

 **Input:**  nums = [999,19,199]

 **Output:**  10

 **Explanation:** 

`nums` becomes `[27, 10, 19]` after all replacements, with minimum element 10.

 

 **Constraints:** 

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 104

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 28.51%)  
**Memory:** 19.3 MB (beats 25.68%)  
**Submitted:** 2026-09-17T06:28:16.634Z  

```py
class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sumofdigits(num: int) -> int:
            s = str(num)
            n = 0
            for ch in s:
                n += int(ch)
            return n
        
        ans = []
        for num in nums:
            ans.append(sumofdigits(num))
        
        return min(ans)
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/)