amino_acid_mass = {
    'G': 57.02,
    'A': 71.04,
    'S': 87.03,
    'P': 97.05,
    'V': 99.07,
    'T': 101.05,
    'C': 103.01,
    'I': 113.08,
    'L': 113.08,
    'N': 114.04,
    'D': 115.03,
    'Q': 128.06,
    'K': 128.09,
    'E': 129.04,
    'M': 131.04,
    'H': 137.06,
    'F': 147.07,
    'R': 156.10,
    'Y': 163.06,
    'W': 186.08
}
def calculate_protein_mass(sequence):
    total_mass = 0.0
    for m in sequence:
        if m not in amino_acid_mass:
            raise ValueError(f"Error: The amino acid {m} doesn't exist")
        total_mass += amino_acid_mass[m]
    return total_mass
if __name__ == "__main__":
    test_seq = "HWE"
    try:
        mass = calculate_protein_mass(test_seq)
        print(f"The total mass of the amino acid sequence {test_seq}: {mass:.2f} amu")
    except ValueError as e:
        print(f"Program Tip: {e}")