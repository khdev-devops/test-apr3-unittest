from calculator import add, subtract
from hamcrest import assert_that, equal_to

# Testfunktionerna är korrekta, men namnen är otydliga.
# TODO: Byt ut namne till något som tydligt visar vad som testas.
#
# referens: https://enterprisecraftsmanship.com/posts/you-naming-tests-wrong/

def test_1():
    result = add(2, 3)
    assert_that(result, equal_to(5))

def test_2():
    result = subtract(5, 3)
    assert_that(result, equal_to(2))