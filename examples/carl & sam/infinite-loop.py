from hypothesis import given
from hypothesis.strategies import booleans

# if given true bool will loop forever, hypothesis gets stuck in the infinite loop becuase it is dynamic
def infinite_loop(input_bool):
    count = 0
    while input_bool:
        count = count + 1
    return True

@given(booleans())
def test_infinite_loop(b):
    assert infinite_loop(b) == True