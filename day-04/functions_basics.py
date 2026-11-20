# Day 04 Function for calculation of concentration

def calculate_amount(mass_g):
    molar_mass = 58.44
    amount_mol = mass_g / molar_mass
    return amount_mol

masses = [5.844, 2.922, 11.688]
for i in masses:
    print(f"Amount of substance: {calculate_amount(i):.3f} mol")