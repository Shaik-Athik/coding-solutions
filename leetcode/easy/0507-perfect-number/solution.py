class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum_ = 0

        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                sum_ += i
        
        return sum_ == num