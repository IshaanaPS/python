import pandas as pd
import matplotlib.pyplot as plt
 
file_path = 'Dataset_Ques_1_4.csv'
data = pd.read_csv(file_path)

months = data['month_number']
total_profit = data['total_profit']

plt.plot(months, total_profit, label='Profit')
plt.title('Total Profit Over Months')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.show()