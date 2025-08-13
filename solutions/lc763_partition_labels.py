from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        # n = len(s)
        last_occur = {}
        # last = [0] * 26
        # for i in range(n):
        for index, char in enumerate(s):
            last_occur[char] = index
            # last[ord(s[i]) - ord('a')] = i

        start = 0
        end = 0
        # for j in range (n):
        #     end=max(last[ord(s[ j]) - ord('a')],end)
        #     if j == end:
        #         res.append(end-start+1)
        #         start=j+1
        for index, char in enumerate(s):
            end = max(last_occur[char], end)
            if index == end:
                res.append(end - start + 1)
                start = index + 1
        return res


if __name__ == "__main__":
    s = "ababcc"
    print(Solution().partitionLabels(s))
