from hypothesis.strategies import integers
from hypothesis import given
import coverage


def obvious(num):
    if num < 10:
        return "Num is less than 10"
    elif num == 10:
        return "Num is 10"
    else:
        return "Num is greater than 10"

@given(integers())
def test_obvious(num):
    assert obvious(5) == "Num is less than 10"
    assert obvious(10) == "Num is less than 10"
    message = obvious(num)