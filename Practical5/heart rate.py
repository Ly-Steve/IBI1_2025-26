# Import plotting library
import matplotlib.pyplot as plt


# Heart rate data of all patients (fixed)
heart_rates = (72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64)


print("===== Task 2: Heart Rate Analysis =====")
total_patients = len(heart_rates)
mean_heart_rate = sum(heart_rates) / total_patients

print(f"There are {total_patients} patients in the dataset with a mean heart rate of {mean_heart_rate:.2f} bpm.")

# Classify heart rates
low = 0
normal = 0
high = 0
for hr in heart_rates:
    if hr < 60:
        low += 1
    elif 60 <= hr <= 120:
        normal += 1
    else:
        high += 1

# Print classification results
print("\nHeart Rate Categories:")
print(f"Low (<60 bpm): {low}")
print(f"Normal (60-120 bpm): {normal}")
print(f"High (>120 bpm): {high}")

# Find the largest category
categories = {"Low": low, "Normal": normal, "High": high}
largest = max(categories, key=categories.get)
print(f"The {largest} category contains the largest number of patients.")

# Plot pie chart
plt.figure(figsize=(6, 6))
plt.pie([low, normal, high], labels=["Low", "Normal", "High"], autopct="%1.1f%%")
plt.title('Heart Rate Distribution')
plt.show()