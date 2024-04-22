from src.connectors.local import LocalJsonLoader

def test_read_local_data():
    tmp = LocalJsonLoader('./static/example_currency_rates.json')
    assert isinstance(tmp, object)