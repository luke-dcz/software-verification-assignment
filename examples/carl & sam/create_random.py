import random
from hypothesis import given
from hypothesis.strategies import integers

def create_random(input_number):
    return random.randint(1, input_number + 10000)

@given(integers())
def test_create_random(i):
    if (i == 2):
        assert create_random(i) <= i
        assert create_random(i) >= 1

# depending on how large of an offset is provided the test may take longer to start failing and then continues to fail.