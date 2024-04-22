# TODO connector for reading local source (example_currency_rates.json) with currency rates
import json

class LocalJsonLoader():
    def __init__(self, filename):
        self.filename = filename
        self.load_local_file_data(self)

    @staticmethod
    def load_local_file_data(self):
        self.local_file_data = json.load(open(self.filename))

    def get_local_file_data(self):
        return self.local_file_data
