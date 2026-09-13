# Python If-Else

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

A *set* is an unordered collection of elements without duplicate entries. 
<br /> 
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

__Example__

    >>> print set()
    set([])

    >>> print set('HackerRank')
    set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

    >>> print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
    set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

    >>> print set((1,2,3,4,5,5))
    set([1, 2, 3, 4, 5])

    >>> print set(set(['H','a','c','k','e','r','r','a','n','k']))
    set(['a', 'c', 'r', 'e', 'H', 'k', 'n'])

    >>> print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
    set(['Hacker', 'Rank'])

    >>> print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
    set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])


Basically, sets are used for membership testing and eliminating duplicate entries.
<br><br>
__Task__  

Now, let's use our knowledge of sets and help Mickey. 

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used: $$ Average = \frac{Sum\;of\;Distinct\;Heights}{Total\;Number\;of\;Distinct\;Heights} $$

**Function Description**   

Complete the *average* function in the editor below.   

*average* has the following parameters:   

- *int arr:* an array of integers    

**Returns**   

- *float:* the resulting float value rounded to 3 places after the decimal   


**Input Format**

The first line contains the integer, $N$, the size of $arr$.<br>
The second line contains the $N$ space-separated integers, $arr[i]$.<br>



**Constraints**

$0 \lt N \le 100$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-13T17:38:36.156Z  

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

[View on HackerRank](https://www.hackerrank.com/challenges/py-introduction-to-sets/problem)