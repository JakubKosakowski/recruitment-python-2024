from src.save_data import *
from src.connectors.database import *


save = SaveData()
def test_save_data_to_json():
    s1 = SaveToJson('./static/database.json', ('eur', 4.213, 42.13))
    tmp = len(s1.transaction.get_all())
    save.save_data(s1)
    assert len(s1.transaction.get_all()) == tmp + 1

def test_save_data_to_database():
    s1 = SaveToDatabase('sqlite:///static/mydb.db', ('eur', 4.213, 42.13))
    tmp = len(s1.session.query(ExchangeTransaction).all())
    save.save_data(s1)
    assert len(s1.session.query(ExchangeTransaction).all()) == tmp + 1