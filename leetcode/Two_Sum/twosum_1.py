from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i+1:]):
                if x + y == target:
                    return list((i, i + j + 1))
        return

if __name__ == '__main__':
    s = Solution()