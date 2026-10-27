"""LeetCode 1 - Two Sum (Easy).

Return indices of the two numbers that add up to target. Exactly one solution exists.
One pass with a hash map: O(n) time, O(n) space.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    assert sorted(s.twoSum([-1, -2, -3, -4, -5], -8)) == [2, 4]
    print("two_sum: all tests passed")
