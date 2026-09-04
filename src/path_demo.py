from pathlib import Path

base_path = Path(__file__).resolve().parent.parent

print("Base Path --> ", base_path)

data_path = base_path/"data"/"raw"

print("Data Path is ->",data_path)