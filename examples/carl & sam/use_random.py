import random
from hypothesis import given
from hypothesis.strategies import integers

def random_multiply(input_number):
    num = random.randint(1, 10)
    return input_number * num

@given(integers())
def test_random_multiply(i):
    num = random.randint(1, 10)
    assert random_multiply(i) == i * num

# expected to not work, expected test num to be different from function num however they mirror each other exactly making the test pass. Seems random numbers are global???