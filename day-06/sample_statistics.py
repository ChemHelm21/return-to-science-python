# DAY 06 - Scientific Sample Statistics

def calculate_concentration(mass_g, volume_ml):
    molar_mass = 58.44
    volume_l = volume_ml / 1000
    return mass_g / (molar_mass * volume_l)


masses_g = [5.844, 2.922, 11.688]
volumes_ml = [500, 500, 250]

# Data validity check and sample concentrations
#1: Check list lengths and empty lists
#2: Process valid samples using zip() and for
#3: Append each valid concentration to the list

sample_number = 0
valid_samples = 0
samples_concentration = []

if len(masses_g) != len(volumes_ml):
    print("Error: Sample counts do not match.")
elif masses_g == [] and volumes_ml == []:
    print("Error: No samples available.")
else:
    for mass_g, volume_ml in zip(masses_g, volumes_ml):
        sample_number += 1
        if mass_g >= 0 and volume_ml > 0:
            concentration = calculate_concentration(mass_g, volume_ml)

            print(f"{sample_number}. sample concentration: {concentration:.3f} mol/L")
            valid_samples += 1

            samples_concentration.append(concentration)
        if mass_g < 0:
            print(f"Error: {sample_number}. sample mass is negative.")
        if volume_ml <= 0:
            print(f"Error: {sample_number}. sample volume zero or less.")
    print(f"Samples processed: {sample_number}")
    print(f"Valid samples: {valid_samples}")


# Statistics
#4: Calculate mean, minimum and maximum
#5: Display the statistical summary
    if valid_samples > 0:
        mean_concentration = sum(samples_concentration) / len(samples_concentration)
        print(f"Mean of concentration: {mean_concentration:.3f} mol /L")

        min_concentration = min(samples_concentration)
        print(f"Minimum concentration: {min_concentration:.3f} mol/L")

        max_concentration = max(samples_concentration)
        print(f"Maximum concentration: {max_concentration:.3f} mol/L")
    else:
        print("No valid samples available for statistical analysis.")

