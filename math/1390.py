class Solution:    
    def sumFourDivisors(self, nums: List[int]) -> int:
       
        result = 0
        for n in nums:
            i = 1
            count = 0
            d_sum = 0
            while i * i <= n:
                if n % i == 0:
                    count += 2 if i != n//i else 1
                    d_sum += i + n//i
                i += 1
            if count == 4:
                result += d_sum
        return result
