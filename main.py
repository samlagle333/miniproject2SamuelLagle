# INF601 - Advanced Programming in Python
# Samuel Lagle
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns


os.makedirs(name="charts", exist_ok=True)


salaries_data = pd.read_csv('salaries.csv', index_col=0, parse_dates=True)

# Filter the data for 'Security Engineer' job title
security_engineer_data = salaries_data[salaries_data['job_title'] == 'Security Engineer']

# Group by 'work_year' and calculate the average salary in USD
average_salaries_per_year = security_engineer_data.groupby('work_year')['salary_in_usd'].mean()

# Plotting the data
plt.figure(figsize=(10,6))
plt.plot(average_salaries_per_year.index, average_salaries_per_year.values, marker='o', linestyle='-', color='b')
plt.title('Average Salary of Security Engineer per Year')
plt.xlabel('Year')
plt.ylabel('Average Salary (USD)')
plt.grid(True)
plt.xticks(average_salaries_per_year.index)  # Ensuring all years are shown on x-axis
plt.savefig('charts/salary_distribution_plot.png', dpi=300, bbox_inches='tight')
plt.clf()

# Plotting the data as an area chart
plt.figure(figsize=(10, 6))
plt.fill_between(average_salaries_per_year.index, average_salaries_per_year.values, color='skyblue', alpha=0.4)
plt.plot(average_salaries_per_year.index, average_salaries_per_year.values, marker='o', color='blue', linestyle='-')
plt.title('Average Salary of Security Engineers per Year')
plt.xlabel('Year')
plt.ylabel('Average Salary (USD)')
plt.grid(True)
plt.xticks(average_salaries_per_year.index)
plt.savefig('charts/salary_distribution_area_plot.png', dpi=300, bbox_inches='tight')
plt.clf()

# Plotting the data as a scatter chart
plt.figure(figsize=(10, 6))
plt.scatter(average_salaries_per_year.index, average_salaries_per_year.values, color='blue')
plt.title('Average Salary of Security Engineers per Year')
plt.xlabel('Year')
plt.ylabel('Average Salary (USD)')
plt.grid(True)
plt.xticks(average_salaries_per_year.index)
plt.savefig('charts/salary_distribution_scatter_plot.png', dpi=300, bbox_inches='tight')
plt.clf()

# Plotting the data as a histogram plot
plt.figure(figsize=(10, 6))
plt.hist(security_engineer_data['salary_in_usd'], bins=20, color='blue', alpha=0.7)
plt.title('Histogram of Security Engineer Salaries')
plt.xlabel('Salary (USD)')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('charts/salary_distribution_histogram_plot.png', dpi=300, bbox_inches='tight')
plt.clf()

# Plotting the data as a violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='work_year', y='salary_in_usd', data=security_engineer_data, inner='quartile')
plt.title('Salary Distribution of Security Engineers per Year (Violin Plot)')
plt.xlabel('Year')
plt.ylabel('Salary (USD)')
plt.xticks(rotation=0)
plt.grid(True)
plt.savefig('charts/salary_distribution_violin_plot.png', dpi=300, bbox_inches='tight')
plt.clf()

# Plotting the data as a strip plot
plt.figure(figsize=(10, 6))
sns.stripplot(x='work_year', y='salary_in_usd', data=security_engineer_data, jitter=True)
plt.title('Salary Distribution of Security Engineers per Year (Strip Plot)')
plt.xlabel('Year')
plt.ylabel('Salary (USD)')
plt.xticks(rotation=0)
plt.grid(True)
plt.savefig('charts/salary_distribution_strip_plot.png', dpi=300, bbox_inches='tight')
plt.clf()