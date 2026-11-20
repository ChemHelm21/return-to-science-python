# Day 04 - Refactored Solution Calculator

def calculate_concentration(mass_g, volume_ml):
    molar_mass = 58.44
    volume_l = volume_ml / 1000
    concentration = mass_g / (molar_mass * volume_l)
    return concentration


mass_g = float(input("Enter NaCl mass (g): "))
volume_ml = float(input("Enter volume (mL): "))

if mass_g < 0:
    print("Error: Mass cannot be negative.")
elif volume_ml <= 0:
    print("Error: Volume must be greater than zero.")
else:
    print(f"Concentretion: {calculate_concentration(mass_g, volume_ml):.3f} mol/L)"