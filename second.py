n = 101

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        nums = []
        while n:
            nums.insert(0, n % 10)
            n = n // 10

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                j = i - 1
                while j > 0 and nums[j - 1] == nums[j]:
                    j -= 1
                nums[j] -= 1
                nums[j + 1:] = [9] * (len(nums) - j - 1)

        ret = nums.pop()
        flag = 10

        while nums:
            ret += nums.pop() * flag
            flag *= 10
        return ret

solu = Solution()
print(solu.monotoneIncreasingDigits(n))
