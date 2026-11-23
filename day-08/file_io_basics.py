from pathlib import Path

# DAY 08 - File I/O Basics

script_folder = Path(__file__).resolve().parent
file_path = script_folder / "lab_notes.txt"

# Write
with open(file_path, "w", encoding="utf-8") as file:
    file.write("Code to Science\n")
    file.write("Day 08\n")
    file.write("Experiment: NaCl concentration analysis\n")

# Read
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

print(content)

