import pathlib
from exchange_rates import get_exchange_rate
from hamcrest import assert_that, equal_to, calling, raises

# Testfunktionerna anropar funktioner så att nätverksanrop sker vilket
# gör att resultatat inte alltid är samma.
# TODO: Använd mock (i detta fallet requests-mock) för att skapa isolerade test.
#
# referens: https://github.com/jamielennox/requests-mock

mock_path = pathlib.Path(__file__).parent / "test_4_mock_reply.json"
mock_text = mock_path.read_text()

def test_get_exchange_rate_usd(requests_mock):
    # GIVEN
    # WHEN
    rate = get_exchange_rate("USD")

    # THEN
    assert_that(rate, equal_to(0.099877))

def test_get_exchange_rate_invalid_when_currency_is_missing(requests_mock):
    # GIVEN
    # WHEN
    # THEN
    assert_that(calling(get_exchange_rate).with_args("XYZ"), raises(ValueError))