import pandas as pd
import time


class Solution:
    def splitArray(self, list_sales: str, k: int) -> int:

        def can_split(max_sum):
            count = 1
            current_sum = 0
            names = []
            cur_names = []
            for key in sales_dict.keys():
                if current_sum + sales_dict[key] > max_sum:
                    count += 1
                    names.append(cur_names.copy() + [current_sum])
                    current_sum = sales_dict[key]
                    cur_names.clear()
                    cur_names.append(key)
                else:
                    current_sum += sales_dict[key]
                    cur_names.append(key)

            return count <= k, names
        
        df = pd.read_csv(list_sales)
        df_grouped = df[['Customer ID', 'Customer Name', 'Sales']]
        sales_dict = df_grouped.groupby('Customer Name')['Sales'].sum().to_dict()

        filtered_df = df[df['Customer Name'] == 'Alex Avila']
        
        ##sales = sales_by_customer['Sales'].tolist()
        low, high = max(sales_dict.values()), sum(sales_dict.values())

        while low < high:
            mid = (low + high) // 2
            res = can_split(mid)
            if res[0] == True:
                high = mid
            else:
                low = mid + 1


        for i in range(0, len(res[1])):
            print(str(i + 1) + " manager")
            for j in range(0, len(res[1][i]) - 1):
                print("- " + res[1][i][j])
            print("Total sales: " + str(res[1][i][-1]))
            print("==========================")
        
        return low


if __name__ == "__main__":

    list_sales = "sales_analysis/train.csv"
    k = 20
    nums = [7,2,5,10,8]
    start = time.time()
    sol = Solution()
    result = sol.splitArray(list_sales, k)
    print("Result:", result)
    end = time.time()
    print(f"{end - start:.6f}") ## время в секундах