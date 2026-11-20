# Day 04 Function for calculation of concentration

def calculate_concentration(mass_g, volume_ml):
    molar_mass = 58.44
    volume_l = volume_ml / 1000
    concentration = mass_g / (molar_mass * volume_l)
    return concentration


mass = [5.844, 2.922, 11.688]
volume = [500, 500, 250]
iterate = [0, 1, 2]

for i in iterate:
    print(f"Concentration: {calculate_concentration(mass[i], volume[i]):.3f} mol/L")
