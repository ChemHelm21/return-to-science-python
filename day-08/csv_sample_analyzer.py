import csv
from pathlib import Path

# DAY 08 - CSV Sample Analyzer

script_folder = Path(__file__).resolve().parent
input_path = script_folder / "samples.csv"
output_path = script_folder / "results.csv"

def calculate_concentration(mass_g, volume_ml):
    molar_mass = 58.44
    volume_l = volume_ml / 1000
    return mass_g / (molar_mass * volume_l)


concentrations = []
valid_samples = 0
sample_number = 0
results = []
fieldnames = [
    "id",
    "mass_g",
    "volume_ml",
    "concentration_mol_l"
]

print("CSV Sample Analyzer")

with open(input_path, "r", encoding="utf-8", newline="") as file:
    samples = csv.DictReader(file)

    for sample in samples:

        mass_g = float(sample["mass_g"])
        volume_ml = float(sample["volume_ml"])

        sample_number += 1

        if mass_g >= 0 and volume_ml > 0:

            concentration = calculate_concentration(mass_g, volume_ml)

            sample["concentration_mol_l"] = f"{concentration:.3f}"
            concentrations.append(concentration)
            results.append(sample)

            print(f"Sample {sample_number}. - {sample['id']}: {concentration:.3f} mol/L")

            valid_samples += 1

        elif mass_g < 0 and volume_ml <= 0:
            print(f"Sample {sample_number}. - {sample['id']}: Mass is negative, and volume zero or less.")
        elif mass_g < 0:
            print(f"Sample {sample_number}. - {sample['id']}: Mass is negative.")
        else:
            print(f"Sample {sample_number}. - {sample['id']}: Volume zero or less.")

    print("")

    # Statistics
    if sample_number == 0:
        print("No samples found in the CSV file.")


    elif valid_samples > 0:

        print("")
        print(f"valid samples: {valid_samples}")

        print(f"Mean concentration: {sum(concentrations) / len(concentrations):.3f} mol/L")
        print(f"Minimum concentration: {min(concentrations):.3f} mol/L")
        print(f"Maximum concentration: {max(concentrations):.3f} mol/L")

    else:
        print("No valid samples available for statistical analysis.")

print("")

with open(output_path, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for row in results:
        writer.writerow(row)

print(f"Results saved to {output_path}")