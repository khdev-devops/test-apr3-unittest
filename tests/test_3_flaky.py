from stack import push, peek, clear_stack, size
from hamcrest import assert_that, equal_to

# Testfunktionerna är sköra och funkar inte alltid
# TODO: Testa att köra testet flera gånger och se till att det konsekvent går igenom

def test_peek_returns_last_pushed_string():
    # GIVEN
    # WHEN
    push("Alice")
    # THEN
    assert_that(peek(), equal_to("Alice"))

def test_size_is_two_after_pushing_two_items():
    # GIVEN
    # WHEN
    push("Bob")
    push("Charlie")
    # THEN
    assert_that(size(), equal_to(2))
