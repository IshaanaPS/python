import matplotlib.pyplot as plt
import pandas as pd

file_path="Dataset_Ques_1_4.csv"
data=pd.read_csv(file_path)
facecream=data['facecream']
facewash=data['facewash']
month=data['month_number']

plt.(facecream,color="blue",edgecolor='black',bins=8)
plt.ylabel("tooth paste sales")
plt.xlabel("month")
plt.title("sales data of toothpaste")
plt.show()