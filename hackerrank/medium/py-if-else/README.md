# Python If-Else

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

<sub>Check [Tutorial](https://www.hackerrank.com/challenges/py-if-else/tutorial) tab to know how to solve.</sub>  

**Task**		
Given an integer, $n$, perform the following conditional actions:

* If $n$ is odd, print `Weird`
* If $n$ is even and in the inclusive range of $2$ to $5$, print `Not Weird`
* If $n$ is even and in the inclusive range of $6$ to $20$, print `Weird`
* If $n$ is even and greater than $20$, print `Not Weird`


**Input Format**

A single line containing a positive integer, $n$.

**Constraints**

- $ 1 \le n \le 100$

**Output Format**

Print `Weird` if the number is weird.  Otherwise, print `Not Weird`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-13T17:38:28.551Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2<=n<=5:
    print("Not Weird")
elif n % 2 == 0 and 6<=n<=20:
    print("Weird")
elif n % 2 == 0 and n>20:
    print("Not Weird")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/py-if-else/problem)