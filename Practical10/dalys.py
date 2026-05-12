import os
import pandas as pd
import matplotlib.pyplot as plt


os.chdir("D:/学校/学习/IBI2526/IbI1_2025-26/IBI1_2025-26/Practical10")
print("Current working directory:", os.getcwd())
print("Forder content:", os.listdir())

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print("Columns:", dalys_data.columns.tolist())

print("\n--- Head of data ---")
print(dalys_data.head(5))

print("\n--- Data info ---")
dalys_data.info()

print("\n--- Describe ---")
print(dalys_data.describe())

print("\n--- First 10 rows, Year and DALYs columns (iloc) ---")
print(dalys_data.iloc[0:10, [2, 3]])

# 要求注释：Afghanistan 前10年最大 DALYs 是哪一年
afghan_first10 = dalys_data.iloc[0:10][dalys_data["Entity"] == "Afghanistan"]
max_year_afghan = afghan_first10.loc[afghan_first10["DALYs"].idxmax(), "Year"]
print(f"Maximum DALYs in first 10 years for Afghanistan was in year: {max_year_afghan}")  

zimbabwe_bool = dalys_data["Entity"] == "Zimbabwe"
zimbabwe_data = dalys_data.loc[zimbabwe_bool, ["Year", "DALYs"]]
print("\n--- All years for Zimbabwe ---")
print(zimbabwe_data)

# 要求注释：Zimbabwe 第一年和最后一年
first_year_zim = zimbabwe_data["Year"].min()
last_year_zim = zimbabwe_data["Year"].max()
print(f"Zimbabwe data from year {first_year_zim} to {last_year_zim}")   

recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]

max_country = recent_data.loc[recent_data["DALYs"].idxmax(), "Entity"]
min_country = recent_data.loc[recent_data["DALYs"].idxmin(), "Entity"]

print(f"\nCountry with highest DALYs in 2019: {max_country}")
print(f"Country with lowest DALYs in 2019: {min_country}")  



country_data = dalys_data.loc[dalys_data["Entity"] == max_country, ["Year", "DALYs"]]

plt.figure(figsize=(10, 6))
plt.plot(country_data["Year"], country_data["DALYs"], 'b-o', linewidth=2, markersize=4)
plt.title(f'DALYs over time in {max_country} (highest in 2019)')
plt.xlabel('Year')
plt.ylabel('DALYs per 100,000 population')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'{max_country}_DALYs_trend.png', dpi=150)   # 保存图片，方便提交



# Question: What was the distribution of DALYs across all countries in 2019?
recent_2019 = dalys_data.loc[dalys_data["Year"] == 2019, "DALYs"]

plt.figure(figsize=(10, 6))
plt.hist(recent_2019, bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of DALYs across all countries in 2019')
plt.xlabel('DALYs per 100,000 population')
plt.ylabel('Number of countries')
plt.grid(True, alpha=0.3)
plt.savefig('DALYs_distribution_2019.png', dpi=150)



print("\n Extra question plot saved as DALYs_distribution_2019.png")