import json

class FileDatabase:
    def __init__(self, filename="Transaction_history.txt"):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {"bankers": [], "customers": []}

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)
