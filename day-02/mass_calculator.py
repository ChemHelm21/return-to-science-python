# NaCl mass calculator

molar_mass = 58.44

concentrecion_text = input("Concentracion (mol/L): ")

volume_text_ml = input("Soultion volume (mL): ")

volume_l = float(volume_text_ml) / 1000

mass = float(concentrecion_text) * molar_mass * volume_l

print(f"Required NaCl mass: {mass:.3f} g")
