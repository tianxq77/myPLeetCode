from typing import List


class Solution:

    def jump(self, nums: List[int]) -> int:
        n= len(nums)
        if n == 1:
            return 0
        #示当前跳跃的覆盖范围已用完，才进行一次新的跳跃
        farest=0  #表示从当前跳跃范围内的所有位置出发，能到达的最远位置，初始为 0
        cur_end=0 #表示当前跳跃能覆盖的最远位置，初始为 0
        times=0
        for i in range(n):
            farest=max(farest,i+nums[i])
            if i==cur_end:#如果 i到达 cur_end，表示当前跳跃的覆盖范围已用完，必须进行一次新的跳跃
                cur_end=farest
                times+=1
            if cur_end>=n-1:
                return times
        return times





    # 错位出现在，没有选择正确的跳跃位置
    # 贪心算法通过局部最优选择逐步逼近全局最优解。在跳跃游戏II中，贪心策略的关键是：每次跳跃时，选择能覆盖最远距离的跳跃点，从而尽量减少总跳跃次数。
    # def jump(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     farest = 0
    #     times = 0
    #     for i in range(n):
    #
    #         if i + nums[i] > farest:
    #             # 只在必须跳跃时（i == cur_end）增加 times
    #             times = times + 1
    #             farest = i + nums[i]
    #         if farest >= n - 1:
    #             return times
    #     return n - 1
