import time
from hypothesis import given
from hypothesis.strategies import integers

def sleep(input_number):
    time.sleep(1000)
    return input_number

@given(integers())
def test_sleep(i):
    assert sleep(i) == i

# just takes too long innit, or not.