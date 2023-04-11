from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i, x in enumerate(nums):
            if numDict.get(x) == None:
                numDict[x] = [i]
            else:
                numDict[x].append(i)
                
        for i, x in enumerate(nums):
            if numDict.get(target - x) != None:
                for j in numDict.get(target - x):
                    if j != i:
                        return list((i, j))
        return

if __name__ == '__main__':
    s = Solution()