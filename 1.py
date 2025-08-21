# # 01背包
# # V 背包容量
# # n个商品 价值wi  体积vi
# # if curV+vi<=V
# # dp[i+1]=dp[i]+wi
# # curV+=vi
# # else
# # dp[i+1]=dp[i]
#
# #dp[i+1]=max(dp[i],dp[i-1]+(wi,vi))
# # dp[i][j] =max(dp[i-1][j]，dp[i-1][j-vi]+wi]
# # 初始化条件：dp[0][j]=0
# #dp[i][0]=0
# class Solution:
#     def maxW(self,w,v,V):
#         n=len(w)
#         dp=[[0]*n]for _ in range (V)
#
#         for i in range(1,n):
#             for j in range(1,V):
#                 if 0<j-v[i]:
#                     dp[i][j] =max(dp[i-1][j],dp[i-1][j-v[i]]+w[i])
#         return dp[n-1][V-1]
#
#
#
#
#
