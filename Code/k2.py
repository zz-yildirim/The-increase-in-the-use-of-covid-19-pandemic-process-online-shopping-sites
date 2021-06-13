import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



graphFolder = "../Graphs/"



col_dict = {'Years': "Years",
			'NetSales': "Net Sales",
			'OperatingIncome': "Operating Income",
			'OperatingExpenses': "Operating Expenses",
       		'NetIncome': "Net Income",
       		'DilutedEarningsPerShare':
       		"Diluted Earnings Per Share"}

data = pd.read_excel(io="../Data/mis376.xlsx",
					engine="openpyxl",
					sheet_name=["Quarter1", "Quarter2", "Quarter3", "Quarter4"])


for selected_column in data["Quarter1"].keys()[1:]:

	print("selected_column: {}".format(selected_column))
	allData = [["2018"],["2019"],["2020"],["2021"]]


	for year, (key, value) in enumerate(data.items()):
		for i in range(len(value[selected_column])):
			allData[i].append(value[selected_column][i])


	df = pd.DataFrame(allData, columns=["Year", "Quarter1", "Quarter2", "Quarter3", "Quarter4"])


	df.plot(x="Year", y=["Quarter1", "Quarter2", "Quarter3", "Quarter4"], kind="bar", color=["green", "orange", "blue", "purple"], figsize=(8,8))

	plt.xlabel('Years',fontsize = 10)
	plt.ylabel(col_dict[selected_column], fontsize = 10)
	plt.title('Years vs.' + col_dict[selected_column], fontsize =15)
	plt.savefig(graphFolder + "years_vs_" + selected_column.lower() + ".png")
	plt.show()