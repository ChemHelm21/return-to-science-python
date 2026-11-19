# Day 2 - Interactive Solution calculator

molar_mass = 58.44

mass_text = input("Enter NaCl mass (g): ")
mass_g = float(mass_text)

volume_text = input("Enter volume (mL): ")
volume_ml = float(volume_text)

volume_l = volume_ml / 1000

amount_mol = mass_g / molar_mass

concentration = amount_mol / volume_l

print(f"Concentracion: {concentration:.3f} mol/L")