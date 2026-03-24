# Pseudocode
# 1. Get user input for age, weight, gender, and creatinine level
# 2. Validate all of the input values and data types
# 3. Print error message if inputs are invalid
# 4. Calculate CrCl using Cockcroft-Gault formula if inputs are valid
# 5. Print the result

# Get USER INPUT (No fixed values anymore)
try:
    age = int(input("Enter your age (years): "))
    weight = float(input("Enter your weight (kg): "))
    gender = input("Enter your gender (male/female): ").lower()
    cr = float(input("Enter creatinine level (μmol/l): "))

    # Input validation
    valid = True
    error_msg = ""

    # Age: < 100 years old
    if age >= 100:
        valid = False
        error_msg += "Age must be less than 100; "

    # Weight: 20kg < weight < 80kg
    if weight <= 20 or weight >= 80:
        valid = False
        error_msg += "Weight must be between 20kg and 80kg; "

    # Creatinine: 0 < Cr < 100 μmol/l
    if cr <= 0 or cr >= 100:
        valid = False
        error_msg += "Creatinine must be between 0 and 100 μmol/l; "

    # Gender: male or female
    if gender not in ["male", "female"]:
        valid = False
        error_msg += "Gender must be male or female; "

    # Calculate and output result
    if valid:
        # Core Cockcroft-Gault formula
        crcl = ((140 - age) * weight) / (72 * cr)
        # Female correction factor
        if gender == "female":
            crcl = crcl * 0.85
        print(f"\nCreatinine Clearance (CrCl): {crcl:.2f} ml/min")
    else:
        print("\nInvalid input:", error_msg)

# Handle non-numeric input
except ValueError:
    print("\nError: Please enter valid numbers for age, weight, and creatinine!")