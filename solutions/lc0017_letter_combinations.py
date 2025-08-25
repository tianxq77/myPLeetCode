from typing import List

"""
回溯
遍历输入的每个数字
对于每个数字，根据其map中对应的

"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums_map={
            "2":"abc",
            "3":"dfe",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res=[]
        path=[]
        def trackback():


