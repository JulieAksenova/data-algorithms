import time
from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:





if __name__ == "__main__":      
   
    list_wine = "wine_analysis/WineQT.csv"
    k = 431
    start = time.time()
    sol = Solution()
    result = sol.divideString(list_wine, k)
    print("Result:", result)
    end = time.time()
    print(f"{end - start:.6f}") ## время в секундах