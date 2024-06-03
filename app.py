import os
import pandas as pd

# Reading the CSV file
df = pd.read_csv('diamonds.csv')

# Your analysis code here
# 1. What is the highest price of a diamond?
max_price = df['price'].max()
print("The highest price:", max_price)

# 2. What is the average price of a diamond?
avg_price = df['price'].mean()
print("The average price:", avg_price)

# 3. How many diamonds of type Ideal are there?
ideal_count = df[df['cut'] == 'Ideal'].shape[0]
print("Number of Ideal diamonds:", ideal_count)

# 4. How many different colors do the diamonds have? What are they?
unique_colors = df['color'].unique()
num_colors = len(unique_colors)
print("Number of different colors:", num_colors)
print("The colors are:", unique_colors)

# 5. What is the median carat of Premium diamonds?
premium_median_carat = df[df['cut'] == 'Premium']['carat'].median()
print("Median carat of Premium diamonds:", premium_median_carat)

# 6. Create the average carat for each cut type
average_carat_per_cut = df.groupby('cut')['carat'].mean()
print("Average carat for each cut type:")
print(average_carat_per_cut)

# 7. Create the average price for each color type
average_price_per_color = df.groupby('color')['price'].mean()
print("Average price for each color type:")
print(average_price_per_color)
