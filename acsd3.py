import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Dataset_Ques_1_4.csv'
data = pd.read_csv(file_path)
months = data['month_number']
total_profit = data['total_profit']

plt.plot(months, data['facecream'], label='Face Cream', marker='o')
plt.plot(months, data['facewash'], label='Face Wash', marker='x')
plt.plot(months, data['toothpaste'], label='Toothpaste', marker='s')
plt.plot(months, data['bathingsoap'], label='Bathing Soap', marker='D')
plt.plot(months, data['shampoo'], label='Shampoo', marker='*')
plt.plot(months, data['moisturizer'], label='Moisturizer', marker='^')
plt.title('Product Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.legend()
plt.grid("true")
plt.show()