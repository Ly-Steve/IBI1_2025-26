# Pseudocode
# 1. Initialize infected count, growth rate, total students, and days
# 2. Loop: calculate daily infections while infected < total students
# 3. Print the number of infected people each day
# 4. Print total days when all students are infected

# Initial parameters
infected = 5
growth_rate = 0.4
total_students = 91
days = 0

# Loop to simulate infection spread
while infected < total_students:
    print(f"Day {days}: Infected people = {infected}")
    # Update the number of infected people
    infected = infected * (1 + growth_rate)
    days += 1

# Print final result
print(f"Day {days}: Infected people = {infected}")
print(f"All 91 students are infected! Total days: {days}")
