from src.currency_converter import *
import pytest

def test_currency_converter():
    assert isinstance(PriceCurrencyConverterToPLN.convert_to_pln(price=10, currency='EUR', currency_rate=4.5), ConvertedPricePLN)
    assert PriceCurrencyConverterToPLN.convert_to_pln(price=10, currency='EUR', currency_rate=4.5).price_in_pln == 45
    with pytest.raises(TypeError):
        PriceCurrencyConverterToPLN.convert_to_pln(currency=10)