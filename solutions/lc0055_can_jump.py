from typing import List


class Solution:
    # 更新每一步可以到达的最远距离
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farest = 0
        for i in range(n):
            if i > farest:
                return False
            farest = max(farest, i + nums[i])
        return True



