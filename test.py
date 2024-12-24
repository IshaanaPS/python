import matplotlib.pyplot as plt
import pandas as pd

file_path='Dataset_Ques_1_4.csv'
data=pd.read_csv(file_path)

months=data['month_number']
total_profit=data['total_profit']

plt.plot(months,total_profit,linestyle="--",color="r",marker='o',linewidth=3)
plt.title("huhahahah")
plt.xlabel("months")
plt.ylabel("total profit")
plt.show()