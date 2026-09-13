# CV

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### CV

Chef has a string $S$ with length $N$. He needs to find the number of indices $i$ ($1 \le i \le N-1$) such that the $i$-th character of this string is a consonant and the $i+1$-th character is a vowel. However, he is busy, so he asks for your help.

Note: The letters 'a', 'e', 'i', 'o', 'u' are vowels; all other lowercase English letters are consonants.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains a single string $S$ with length $N$.
### Output

For each test case, print a single line containing one integer ― the number of occurrences of a vowel immediately after a consonant.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
- $S$ contains only lowercase English letters
### Subtasks

 **Subtask #1 (100 points):**  original constraints

### Sample 1:
Input
Output

```
3
6
bazeci
3
abu
1
o
```

```
3
1
0
```

### Explanation:

 **Example case 1:**  The vowel 'a' follows after the consonant 'b', 'e' follows after 'z' and 'i' follows after 'c', so the answer is $3$.

 **Example case 2:**  The only vowel 'u' follows after 'b', so the answer is $1$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-13T18:00:42.322Z  

```py
# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    count = 0
    
    for i in range(n-1):
        if s[i] not in 'aeiou' and s[i+1] in 'aeiou':
            count += 1
    print(count)
```

---

[View on CodeChef](https://www.codechef.com/problems/CV)