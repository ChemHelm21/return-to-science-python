
# DAY 03 - Smart Solution Calculator

molar_mass = 58.44

mass_g = float(input("Enter NaCl mass (g): "))
volume_ml = float(input("Enter volume (mL): "))

if mass_g < 0:
    print("Error: Mass cannot be negative.")
elif volume_ml <= 0:
    print("Error: Volume must be greater than zero.")
else:
    amount_mol = mass_g / molar_mass
    volume_l = volume_ml / 1000
    print(f"Concentrecion: {amount_mol / volume_l:.3f} mol/L)")
