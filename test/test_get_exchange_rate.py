from src.get_exchange_rate import *


ftc = Rate()
def test_get_exchange_rate_from_api():
    s1 = APIExchangeRate('http://api.nbp.pl/api/exchangerates/rates/A', 'USD')
    s2 = APIExchangeRate('http://api.nbp.pl/api/exchangerates/rates/A', 'FCX')
    assert ftc.get_rate(s1) != 0
    assert ftc.get_rate(s2) == 0

def test_get_exchange_rate_from_local():
    s1 = LocalExchangeRate('./static/example_currency_rates.json', 'EUR')
    s2 = LocalExchangeRate('./static/example_currency_rates.json', 'NZD')
    s3 = LocalExchangeRate('./static/example_currency_rates.json', 'CZK')
    assert ftc.get_rate(s1) != 0
    assert ftc.get_rate(s2) == 0
    assert ftc.get_rate(s3) == -1
