# INF601 - Advanced Programming in Python
# Samuel Lagle
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs(name="charts", exist_ok=True)


salaries = pd.read_csv('salaries.csv', index_col=0, parse_dates=True)

salaries.plot()
plt.show()