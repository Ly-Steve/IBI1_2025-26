# Import plotting library
import matplotlib.pyplot as plt


# Population data (millions) from 2020 to 2024 (fixed)
population = {
    "UK": {"2020": 66.7, "2024": 69.2},
    "China": {"2020": 1426, "2024": 1410},
    "Italy": {"2020": 59.4, "2024": 58.9},
    "Brazil": {"2020": 208.6, "2024": 212.0},
    "USA": {"2020": 331.6, "2024": 340.1}
}


print("===== Task 3: Population Growth Analysis =====")
growth_rates = {}

# Calculate percentage change for each country
for country, data in population.items():
    pop_2020 = data["2020"]
    pop_2024 = data["2024"]
    rate = ((pop_2024 - pop_2020) / pop_2020) * 100
    growth_rates[country] = rate
    print(f"{country} Growth Rate: {rate:.2f}%")

# Sort growth rates from highest to lowest
sorted_rates = sorted(growth_rates.items(), key=lambda x: x[1], reverse=True)
print("\nSorted Growth Rates (Highest to Lowest):")
for country, rate in sorted_rates:
    print(f"{country}: {rate:.2f}%")

# Find max increase and max decrease
max_increase = sorted_rates[0][0]
max_decrease = sorted_rates[-1][0]
print(f"\nThe country with the largest population increase is {max_increase}.")
print(f"Country with Largest Decrease: {max_decrease}")

# Plot bar chart
countries = [item[0] for item in sorted_rates]
rates = [item[1] for item in sorted_rates]

plt.figure(figsize=(8, 4))
plt.bar(countries, rates, color='seagreen')
plt.title('Population Growth Rate (2020-2024)')
plt.xlabel('Country')
plt.ylabel('Growth Rate (%)')
plt.axhline(y=0, color='black')
plt.tight_layout()
plt.show()