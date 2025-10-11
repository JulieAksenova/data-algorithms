import time
from typing import List
import pandas as pd


class Solution:
    def LongestWindow(self, data: str, t_min: int, t_max: int) -> int:

        df = pd.read_csv(data)
        temps = df['meantemp'].astype(float).values.tolist()
    
        m = len(temps)
        
        conditions = {
            'min': 0,
            'aver': 0,
            'max': 0
        }
        window = {}
        have, need = 0, len(conditions) 
        res, res_len = [-1, -1], float("inf")
        left = 0

        for right, d in enumerate(temps):
            if d <= t_min:
                window['min'] = window.get('min', 0) + 1
            elif d > t_min and d <= t_max:
                window['aver'] = window.get('aver', 0) + 1
            elif d > t_max:
                window['max'] = window.get('max', 0) + 1
            have = sum(1 for v in window.values() if v > 0)

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                if temps[left] <= t_min:
                    window['min'] -= 1
                elif temps[left] > t_min and temps[left] <= t_max:
                    window['aver'] -= 1
                elif temps[left] > t_max:
                    window['max'] -= 1
                have = sum(1 for v in window.values() if v > 0)
                left += 1
        l, r = res
        print(res)
        return temps[l:r + 1] if res_len != float("inf") else ""


if __name__ == "__main__":      
   
    data_csv = "climate_analysis/DailyDelhiClimateTrain.csv"
    t_min = 10
    t_max = 16
    humid_min = 65
    start = time.time()
    sol = Solution()
    result = sol.LongestWindow(data_csv, t_min, t_max)
    print("Result:", result)
    end = time.time()
    print(f"{end - start:.6f}") ## время в секундах