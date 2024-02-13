from hypothesis import given
from hypothesis.strategies import text
from hypothesis.strategies import integers
from hypothesis.strategies import booleans

def encode(input_string):
    if not input_string:
        return []
    count = 1
    prev = ""
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    entry = (character, count)
    lst.append(entry)
    return lst


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q

@given(text())
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s

#           Carl and sam stuff vvv
#=================================================================

# will always return one possible option but never the other, hypothesis does not check for other options since it is dynamic
def logical_error_1(input_string):
    print("bingus")
    if True:
        return input_string + "Always returned"
    else:
        return input_string + "Never returned"
    

# if given true bool will loop forever, hypothesis gets stuck in the infinite loop becuase it is dynamic
def infinite_loop(input_bool):
    count = 0
    while input_bool:
        count = count + 1
    return True

# using type comments the funciton is maked as returning an int, however it returns a string, hypothesis does not check for this thus the test passes when it shouldnt.
def type_comments(input_text) -> int:
    return input_text

# test for this function sees if output is greater or equal to the input. In the case of a negative input the output will be less than the input, 
# failing the test. Test only shows 1 of the many possible failing values, thus you would have to run the test serveral times to determine the pattern.
def double_input(input_number):
    return input_number * 2

# expore threading, APIs, scope, caching specific inputs, try find false negative

#=========================================================

@given(text())
def test_logical_error(s):
    assert logical_error_1(s) == s + "Always returned"

@given(text())
def test_type_comments(s):
    assert type_comments(s) == s

@given(integers())
def test_negative_multiply(n):
    assert double_input(n) >= n

# @given(booleans())
# def test_infinite_loop(b):
#     assert infinite_loop(b) == True
