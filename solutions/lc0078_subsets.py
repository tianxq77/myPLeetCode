from typing import List

'''
不重复子集

每个元素有选和不选两种可能

'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        # 每次递归先将当前子集加入结果，然后依次选择后续元素或不选
        def trackback(start,path):
            res.append(path.copy())
            for i in range(start,n):
                path.append(nums[i])
                trackback(i+1,path)
                path.pop()
        trackback(0,[])
        return res


if __name__=="__main__":
    s=Solution()
    nums = [1, 2, 3]
    print(s.subsets(nums))