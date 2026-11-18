# DAY 01 - NaCl Solution Calculator



#given values

mass_g = 2.922
molar_mass = 58.44
volume_1 = 0.500


# Calculate amount of substance

amount_mol = mass_g / molar_mass


# calculate concentration

concentration = amount_mol / volume_1


# Display the result

print("NaCl Solution calculator")
print("Csoncentracion:", round(concentration, 3), "mol/L")