from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 遍历数组，计算前缀乘积和后缀乘积
        #pre[i]=pre[i-1]*num[i]
        #suf[i]=suf[i+1]*num[i]
        #ans[i]=pre[i]*suf[i]
        # n=len(nums)
        # pre=[1]*n
        # suf=[1]*n
        # ans = [0] * n
        # for i in range(1,n):
        #     pre[i]=pre[i-1]*nums[i-1]
        #     suf[n-i-1]=suf[n-i]*nums[n-i]
        # for i in range(n):
        #     ans[i]=pre[i]*suf[i]
        #
        # return ans


# 优化空间复杂度
        n=len(nums)
        ans=[1]*n
        for i in range(1,n):
            ans[i]=ans[i-1]*nums[i-1]

        left=1
        for i in range(n-1,-1,-1):
            ans[i]=ans[i]*left
            left=left*nums[i]
        return ans





if __name__ == '__main__':
    solution=Solution()
    nums = [1,2,3,4]
    print(solution.productExceptSelf(nums))