from abc import ABC, abstractmethod
from src.connectors.database import ExchangeTransaction, JsonFileDatabaseConnector
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SaveRecord(ABC):
    def __init__(self, filename: str, save_data: tuple):
        self.filename = filename
        self.save_data = save_data
    
    @abstractmethod
    def save(self):
        pass


class SaveDataDict(dict):
    def __setitem__(self, key, value):
        return super().__setitem__(key, value)


class SaveToJson(SaveRecord):
    def __init__(self, filename: str, save_data: tuple):
        super().__init__(filename, save_data)
        self.transaction = JsonFileDatabaseConnector(self.filename) 

    def save(self):
        self.save_to_json()
    
    def save_to_json(self):
        save_data_dict = SaveDataDict()
        save_data_dict["id"] = len(self.transaction.get_all())+1
        save_data_dict["currency"] = self.save_data[0]
        save_data_dict["rate"] = self.save_data[1]
        save_data_dict["price_in_pln"] = self.save_data[2]
        save_data_dict["date"] = datetime.today().strftime('%Y-%m-%d')
        self.transaction.save(save_data_dict)


class SaveToDatabase(SaveRecord):
    def __init__(self, filename: str, save_data: tuple):
        super().__init__(filename, save_data)
        self.engine = create_engine('sqlite:///static/mydb.db', echo=False)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def save(self):
        self.save_to_database()

    def save_to_database(self):
        tran = ExchangeTransaction(self.save_data[0], self.save_data[1], self.save_data[2])
        self.session.add(tran)
        self.session.commit()


class SaveData:
    def __init__(self):
        pass

    def save_data(self, save_method: SaveRecord):
        save_method.save()
