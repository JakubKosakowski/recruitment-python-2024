import json


class JsonFileDatabaseConnector:
    def __init__(self, filename) -> None:
        self.filename = filename
        self._data = self._read_data(self.filename)

    @staticmethod
    def _read_data(filename: str) -> dict:
        with open(filename, "r") as file:
            return json.load(file)

    def save(self, entity) -> int:
        id = entity["id"]
        self._data[id] = entity
        with open(self.filename, 'w') as file:
            json.dump(self._data, file, indent=4, separators=(',',': '))
        return id

    def get_all(self) -> list:
        return self._data

    def get_by_id(self, id) -> dict:
        return self._data[str(id)]
