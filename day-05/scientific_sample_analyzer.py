# DAY 05 - Scientific Sample Analyzer

print("Scientific Sample Analyzer")

def calculate_concentration(mass_g, volume_ml):
    molar_mass = 58.44
    volume_l = volume_ml / 1000
    concentration = mass_g / (molar_mass * volume_l)
    return concentration



# Data sets

masses_g = [5.844, 2.922, 11.688]
volumes_ml = [500, 500, 250]



# Data validity check and sample concentracions

sample_number = 0
valid_samples = 0

if len(masses_g) != len(volumes_ml):
    print("Error: Sample counts do not match.")
elif masses_g == [] and volumes_ml == []:
    print("Error: No samples available.")
else:
    for mass_g, volume_ml in zip(masses_g, volumes_ml):
        sample_number += 1
        if mass_g >= 0 and volume_ml > 0:
            print(f"{sample_number}. sample concentration: {calculate_concentration(mass_g,volume_ml):.3f} mol/L")
            valid_samples += 1
        if mass_g < 0:
            print(f"Error: {sample_number}. sample mass is negative.")
        if volume_ml <= 0:
            print(f"Error: {sample_number}. sample volume zero or less.")
    print(f"Samples processed: {sample_number}")
    print(f"Valid samples: {valid_samples}")
