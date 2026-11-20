# Day 03 Validated mass calculator

molar_mass = 58.44

concentration = float(input("Enter the concentration of NaCl solution mol/L: "))
volume_ml = float(input("Enter volume (ml): "))

if concentration < 0:
    print("Error: Concentration cannot be zero!")
elif volume_ml <= 0:
    print("Error: Volume must be greater than zero.")
else:
    volume_l = volume_ml / 1000
    mass_g = concentration * molar_mass * volume_l
    print(f"Required NaCl mass: {mass_g:.3f} g")
