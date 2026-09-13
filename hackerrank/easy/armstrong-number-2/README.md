# Armstrong number 2

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. Write a program to test whether a given number is an Armstrong number or not.

 **Input Format** 

First line consists of an integer T which is the number of testcases.And then there will be T line-separated numbers each line consisting of a single integer N.

 **Constraints** 

1 < N < 999

 **Output Format** 

T number of line separted strings,each line consisting of a string "Yes",if N is an armstrong number and "No",if N isn't an armstrong number.

 **Sample Input** 

3
345
1
0

 **Sample Output** 

No
Yes
Yes

 **Explanation** 

3^3 + 4^3 + 5^3 is not equal to 345.Hence 345 isn't an armstrong number. 1^3 = 1.Hence 1 is an armstrong number. 0^3 = 0.Hence 0 is an armstrong number.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-13T17:55:06.759Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for _ in range(t):
    n = int(input())
    armstrong = 0
    temp = n
    
    while temp>0:
        digit = temp % 10
        armstrong += (digit) ** 3
        temp //= 10
    
    if armstrong == n:
        print("Yes")
    else:
        print("No")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/armstrong-number-2/problem)