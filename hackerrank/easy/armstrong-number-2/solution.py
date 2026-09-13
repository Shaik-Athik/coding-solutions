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
