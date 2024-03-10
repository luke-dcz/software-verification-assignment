from hypothesis import given
from hypothesis.strategies import text

# using type comments the funciton is maked as returning an int, however it returns a string, hypothesis does not check for this thus the test passes when it shouldnt.
def type_comments(input_text : int) -> int:
    return input_text

@given(text())
def test_type_comments(s):
    assert type_comments(s) == s