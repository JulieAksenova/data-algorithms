import heapq as hq
from typing import List
from collections import defaultdict, deque, Counter
import copy
import time
from itertools import combinations
import pandas as pd
import ast


class Solution:
    def minimumDeletions(self, name_list: str, k: int) -> int:
        df = pd.read_csv(list_wine)
        groups = {f"group{i}": 0 for i in range(1, 7)}
        for i in df["quality"]:
            groups["group" + str(i - 2)] += 1

        res = len(df["quality"])
        for a in groups.values():
            deleted = 0
            for b in groups.values():
                if a > b:
                    deleted += b
                elif b > a + k:
                    deleted += b - (a + k)
            res = min(res, deleted)

        return(res)
       


if __name__ == "__main__":      
   
    list_wine = "wine_analysis/WineQT.csv"
    k = 431
    start = time.time()
    sol = Solution()
    result = sol.minimumDeletions(list_wine, k)
    print("Result:", result)
    end = time.time()
    print(f"{end - start:.6f}") ## время в секундах


#     Output
# "bdiyfvez"
# Expected
# "bdevfziy"