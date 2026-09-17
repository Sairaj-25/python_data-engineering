try:
    with open("missing_file.csv","r") as f:
        data = f.read()
except FileNotFoundError:
    print("File Not Found: check the file is present at location")
finally:
    print("cleanup complete")