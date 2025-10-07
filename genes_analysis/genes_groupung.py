import time
from typing import List
import pandas as pd

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

                
        df = pd.read_csv("genes_analysis/promoters.data", header=None, delimiter=",")

        codes = df[2]
        print(codes)


        codes_list = list(codes.values)
        groups = [codes_list[i : i + k] for i in range(0, len(codes), k)]
        print(groups)

        fill = str(groups[0][0])
        while k - len(groups[-1]) > 0:
            groups[-1].append(fill)
       

        return groups[-1]




if __name__ == "__main__":      
   
    list_wine = "wine_analysis/WineQT.csv"
    k = 4
    start = time.time()
    sol = Solution()
    result = sol.divideString(list_wine, k, 'x')
    print("Result:", result)
    end = time.time()
    print(f"{end - start:.6f}") ## время в секундах