import csv, json

class DataPipeline():
    def __init__(self, config_path):
        with open(config_path) as f:
            config = json.load(f)

        self.source = config["source"]
        self.destination = config["destination"]

    def extract_data(self):
        print(f"Extracting data from {self.source}")
        data = []

        with open(self.source, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                data.append(row)

        return data

    def transform_data(self, data):
        print("Transforming  data")

        cleaned_data = []

        for row in data:
            if row["amount"] not in [None, "", "NULL"]:
                row["amount"] = float(row["amount"])
                cleaned_data.append(row)

        return cleaned_data


    # Load the data in destination

    def load_data(self, data):
        print(f"loading{len(data)} records to {self.destination}")

        if not data:
            print("No data to write.")
            return

        with open(self.destination, 'w', newline="",encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    # Orchestrate Flow
    def run(self):
        data = self.extract_data()
        data = self.transform_data(data)
        self.load_data(data)

pipeline = DataPipeline("config.json")

pipeline.run()