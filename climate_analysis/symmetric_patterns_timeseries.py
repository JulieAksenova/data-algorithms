import time
from typing import List
import pandas as pd


class Solution:
    def Symmetric_patterns(self, data: str, k_min: int, k_max: int) -> int:

        def is_palindrome(seq):
            left, right = 0, len(seq) - 1
            while left < right:
                if seq[left] != seq[right]:
                    return False
                left += 1
                right -= 1
            return True

        
        df = pd.read_csv(data)
        temps = df['meantemp'].astype(int).values.tolist()
        
        m = len(temps)
        count = 0

        for left in range(m):
            for length in range(k_min, k_max + 1):
                right = left + length
                if right <= m:
                    if is_palindrome(temps[left : right]):
                        print(temps[left : right])
                        count += 1

        print(count)


if __name__ == "__main__":      
   
    data_csv = "climate_analysis/DailyDelhiClimateTrain.csv"
    k_min = 10
    k_max = 20
    start = time.time()
    sol = Solution()
    result = sol.Symmetric_patterns(data_csv, k_min, k_max)
    print("Result:", result)
    end = time.time()
    print(f"{end - start:.6f}") ## время в секундах