from hypothesis import given
from hypothesis.strategies import integers

# test for this function sees if output is greater or equal to the input. In the case of a negative input the output will be less than the input, 
# failing the test. Test only shows 1 of the many possible failing values, thus you would have to run the test serveral times to determine the pattern.
def double_input(input_number):
    return input_number * 2

@given(integers())
def test_negative_multiply(n):
    assert double_input(n) >= n