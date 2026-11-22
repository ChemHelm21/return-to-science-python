# DAY 07 - Structured Sample Analyzer


def calculate_concentration(mass_g,volume_ml):
    molar_mass = 58.44
    volume_l = volume_ml / 1000
    return mass_g / (molar_mass * volume_l)

# Data sets

samples = [
    {"id": "NaCl-001", "mass_g": 5.844, "volume_ml": 500},
    {"id": "NaCl-002", "mass_g": 2.922, "volume_ml": 500},
    {"id": "NaCl-003", "mass_g": 11.688, "volume_ml": 250}
]

concentrations = []

print("Structured Sample Analyzer")
print("")
# Data validity check and sample concentrations

valid_samples = 0

if samples == []:
    print("No samples available for statistical analysis.")
else:
    for number, sample in enumerate(samples, start=1):
        if sample["mass_g"] >= 0 and sample["volume_ml"] > 0:

            concentration = calculate_concentration(sample["mass_g"], sample["volume_ml"])
            sample["concentration_mol_l"] = concentration
            concentrations.append(concentration)
            print(f"Sample {number}. - {sample['id']}: {concentration:.3f} mol/L")
            valid_samples += 1
        elif sample["mass_g"] < 0 and sample["volume_ml"] <= 0:
            print(f"Sample {number}. - {sample['id']}: Mass is negative, and volume zero or less.")
        elif sample["mass_g"] < 0:
            print(f"Sample {number}. - {sample['id']}: Mass is negative.")
        else:
            print(f"Sample {number}. - {sample['id']}: Volume zero or less.")

    print("")
    print(f"valid samples: {valid_samples}")
    print("")

# Statistics

    if valid_samples > 0:
        print(f"Mean concentration: {sum(concentrations)/len(concentrations):.3f} mol/L")
        print(f"Minimum concentration: {min(concentrations):.3f} mol/L")
        print(f"Maximum concentration: {max(concentrations):.3f} mol/L")
    else:
        print("No valid samples available for statistical analysis.")