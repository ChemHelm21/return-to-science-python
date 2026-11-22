# Day 7 - Dictionary Explorer

samples = [
    {"id": "NaCl-001", "mass_g": 5.844, "volume_ml": 500},
    {"id": "NaCl-002", "mass_g": 2.922, "volume_ml": 500},
    {"id": "NaCl-003", "mass_g": 11.688, "volume_ml": 250}
]

print("Second sample: " + samples[1]['id'])
print(f"Second samples mass: {samples[1]['mass_g']} g")

samples[2]["volume_ml"] = 500

print("")

for number, sample in enumerate(samples, start=1):
    print(f"Sample {number} - {sample['id']}")
    print(f"Mass: {sample['mass_g']} g")
    print(f"Volume: {sample['volume_ml']} mL")
    print("")
