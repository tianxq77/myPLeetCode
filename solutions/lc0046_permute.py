from typing import List

from sqlalchemy import false

'''
回溯求解框架
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Backtracking回溯函数，都是“在当前状态下，遍历所有可行决策，做一个→深入→回来撤销→换下一个
        # 需要维护的结构为：当前路径、剩余可用元素（用列表维护或者是使用索引维护）
        n=len(nums)
        res=[]
        path=[]
        used=[false]*n
        def backtrack():
            if len(path) == n:
                res.append(path.copy())
                return
            else:
                for i in range(n):
                    if used[i]!=True:
                        used[i] = True
                        path.append(nums[i])
                        backtrack()
                        used[i]=False
                        path.pop()

        backtrack()
        return res



if __name__=="__main__":
    s=Solution()
    nums = [1, 2, 3]
    print(s.permute(nums))
