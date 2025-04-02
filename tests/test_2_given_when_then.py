from calculator import multiply, divide
from hamcrest import assert_that, equal_to, calling, raises

# Testfunktionerna är korrekta, men strukturen är otydlig.
# TODO: Dela upp testfunktionerna i tydliga GIVEN, WHEN och THEN.
#
# referenser: 
# - https://martinfowler.com/bliki/GivenWhenThen.html
# - https://pythontest.com/strategy/given-when-then-2/

def test_multiply_operation():
    result = multiply(4, 5)
    assert_that(result, equal_to(20))

def test_divide_operation():
    result = divide(10, 2)
    assert_that(result, equal_to(5))