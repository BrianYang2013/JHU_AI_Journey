# Solution:
# https://leetcode-cn.com/problems/two-sum/solution/liang-shu-zhi-he-by-leetcode-solution/
# Hash is good at finding a value in lots of data, O(1)
import random
import time


class Solution:
    def two_sum_0(self, nums: list[int], target: int) -> list[int]:
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

    def two_sum(self, nums: list[int], target: int) -> list[int]:
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


# Prepare test data
nums = list(range(10, 1000))  # Create list, with element 10 to xx-1
nums.extend((2, 7))  # Add 2 and 7
random.shuffle(nums)  # shuffle
print(nums)
target = 9

# Prepare for the test
s = Solution()
run = 100

# Test
start = time.time_ns()
for i in range(run):
    s.two_sum_0(nums, target)
end = time.time_ns()
print(s.two_sum_0(nums, target))
print("runtime {}".format((end - start) / run))

start = time.time_ns()
for i in range(run):
    s.two_sum(nums, target)
end = time.time_ns()
print(s.two_sum(nums, target))
print("runtime {}".format((end - start) / run))
