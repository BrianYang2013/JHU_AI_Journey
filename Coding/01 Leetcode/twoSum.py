# 链接：https://leetcode-cn.com/problems/two-sum/solution/liang-shu-zhi-he-by-leetcode-solution/
import time

class Solution:
    def twoSum00(self, nums: list[int], target: int) -> list[int]:
        """
        Time:   O(n^2)
        Space:  O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Time:   O(n)
        Space:  O(n)
        """
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

# Test
nums = [2,7,11,15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
target = 9

s = Solution()
run = 1000

start = time.time_ns()
for i in range(run):
    s.twoSum00(nums, target)
end = time.time_ns()
print(s.twoSum00(nums, target))
print("runtime {}".format((end-start)/run))

start = time.time_ns()
for i in range(run):
    s.twoSum(nums, target)
end = time.time_ns()
print(s.twoSum(nums, target))
print("runtime {}".format((end-start)/run))