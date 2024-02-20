from hypothesis import given
from hypothesis.strategies import text

# will always return one possible option but never the other, hypothesis does not check for other options since it is dynamic
def logical_error_1(input_string):
    print("bingus")
    if True:
        return input_string + "Always returned"
    else:
        return input_string + "Never returned"
    
@given(text())
def test_logical_error(s):
    assert logical_error_1(s) == s + "Always returned"
