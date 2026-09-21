# Maximum Substrings With Distinct Start

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a string `s` consisting of lowercase English letters.

Return an integer denoting the  **maximum**  number of substrings you can split `s` into such that each  **substring**  starts with a  **distinct**  character (i.e., no two substrings start with the same character).

 

 **Example 1:** 

 **Input:**  s = "abab"

 **Output:**  2

 **Explanation:** 

- Split "abab" into "a" and "bab".
- Each substring starts with a distinct character i.e 'a' and 'b'. Thus, the answer is 2.

 **Example 2:** 

 **Input:**  s = "abcd"

 **Output:**  4

 **Explanation:** 

- Split "abcd" into "a", "b", "c", and "d".
- Each substring starts with a distinct character. Thus, the answer is 4.

 **Example 3:** 

 **Input:**  s = "aaaa"

 **Output:**  1

 **Explanation:** 

- All characters in "aaaa" are 'a'.
- Only one substring can start with 'a'. Thus, the answer is 1.

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 95.81%)  
**Memory:** 19.9 MB (beats 93.20%)  
**Submitted:** 2026-09-21T13:37:45.610Z  

```py
class Solution:
    def maxDistinct(self, s: str) -> int:
        
        res = set(s)

        return len(res)
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-substrings-with-distinct-start/)