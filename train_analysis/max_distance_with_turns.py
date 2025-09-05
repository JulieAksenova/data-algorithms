import pandas as pd
import time
import ast


class Solution:
     def read(self, list_p: str, k: int):
          df = pd.read_csv(list_p) 

          df['POLYLINE'] = df['POLYLINE'].apply(ast.literal_eval)  
          df['trajectory'] = df["POLYLINE"].apply(self.coords_to_directions)     
          maxi = 0
          for i in range(0, len(df['trajectory'])):
               if len(df['trajectory'][i]) > maxi:
                    maxi = len(df['trajectory'][i])
               long = self.maxDistance(df['trajectory'][i], k)
               print(i, long)
          

     def maxDistance(self, s: str, k: int):
          ans = 0
          north = south = east = west = 0
          for it in s:
               if it == "N":
                    north += 1
               elif it == "S":
                    south += 1
               elif it == "E":
                    east += 1
               elif it == "W":
                    west += 1
               times1 = min(north, south, k) 
               times2 = min(east, west, k - times1)  
               ans = max(ans, self.count(north, south, times1) + self.count(east, west, times2))
          return ans

     def count(self, dis1:int, dis2: int, times: int):
          return (abs(dis1 - dis2) + times * 2)     
     
     def coords_to_directions(self, coords):
          directions = "" 
          n = len(coords)

          diff_la, diff_lo = [], []
          for i in range (1, n):
               diff_la.append(coords[i][0] - coords[i - 1][0])
               diff_la.append(coords[i][1] - coords[i - 1][1])

          for i in range(1, len(coords)):
               lat_diff = coords[i][0] - coords[i-1][0]
               lon_diff = coords[i][1] - coords[i-1][1]

               if abs(lat_diff) > abs(lon_diff):
                    if lat_diff > 0:
                         directions += "N"
                    else:
                         directions += "S"
               else:
                    if lon_diff > 0:
                         directions += "E"
                    else:
                         directions += "W"

          return directions

     

if __name__ == "__main__":
     list_pol = "train.csv"
     k = 2
     start = time.time()
     sol = Solution()
     result = sol.read(list_pol, k)
     print(result)
     end = time.time()
     print(f"{end - start:.6f}")