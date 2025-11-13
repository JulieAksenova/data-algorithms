import pandas as pd
import time
from typing import List
import math
import bisect

class Solution:
    def climateWindow(self, temp_date: List[List[int]], k: int) -> int:

        df = pd.read_csv(temp_date)
        df['dt'] = pd.to_datetime(df['dt'])
        df['year'] = df['dt'].dt.year
        grouped = df.groupby(['year', 'Country'])['AverageTemperature'].mean().reset_index()
        matrix = grouped.pivot(index='year', columns='Country', values='AverageTemperature')
        ##matrix_clean = matrix.dropna()

        ##countries = ['Albania', 'Andorra']
        ##matrix_AA = matrix[countries]


        m, n = len(matrix), matrix.shape[1]
        result = -math.inf

        for left in range(235, 237):
            row_sums = [0] * m

            for right in range(left, 237):
                for i in range(m):
                    row_sums[i] += float(matrix.iloc[i,right])

                print('---------------------------')
                print(row_sums)

                prefix = 0
                prefixes = [0]

                for s in row_sums:
                    if len(prefixes) > 1 and pd.isna(s):
                        prefixes = [0]
                    elif pd.notna(s):
                        prefix += s
                        
                        target = prefix - k

                        idx = bisect.bisect_left(prefixes, target)
                        if idx < len(prefixes):
                            candidate = prefix - prefixes[idx]

                            if candidate > result:
                                result = candidate
                                print(left, right, result)
                                

                        bisect.insort(prefixes, prefix)

    

        return result


if __name__ == "__main__":      
   
    temp_date = "climate_analysis/GlobalLandTemperaturesByCountry.csv"
    k = 500000000
    nums = [1,2,3]
    matrix = [[1,0,1],[0,-2,3]]
    start = time.time()
    sol = Solution()
    result = sol.climateWindow(temp_date, k)
    print("Result:", result)
    end = time.time()
    print(f"{end - start:.6f}") ## время в секундах