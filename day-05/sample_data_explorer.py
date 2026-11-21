# DAY 05 - Sample Data Explorer

masses_g = [5.844, 2.922, 11.688]
volumes_ml = [500, 500, 250]

sample_number = 0

# Print number of samples

if len(masses_g) != len(volumes_ml):
    print("Error: Sample counts do not match.")
elif len(masses_g) == 0:
    print("Error: No samples available.")
else:
    sample_number = len(masses_g)
    print(f"Number of samples: {sample_number}")


    # Print the first mass using indexing
    # Print the last volume using negative indexing

    print(f"First sample mass: {masses_g[0]} g")
    print(f"Last sample volume: {volumes_ml[-1]} mL")


    # Use range() to print sample numbers

    print("Sample numbers:")
    for i in range(1, sample_number + 1):
        print(i)


    # Use zip() to print mass-volume pairs

    print("Sample data:")
    for mass_g, volume_ml in zip(masses_g, volumes_ml):
        print(f"{mass_g} g - {volume_ml} mL")

