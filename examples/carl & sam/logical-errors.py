from hypothesis import given
from hypothesis.strategies import text
from hypothesis.strategies import integers

# will always return one possible option but never the other, hypothesis does not check for other options since it is dynamic
def logical_error_1(input_string):
    print("bingus")
    if True:
        return input_string + "Always returned"
    else:
        return input_string + "Never returned"
    

def increment(num):
    old_num = num
    server(old_num)
    new_num = old_num + 1
    return new_num

def server(num):
    print(str(num)+" sent to server")


@given(text())
def test_logical_error(s):
    assert logical_error_1(s) == s + "Always returned"

@given(integers())
def test_server(num):
    assert increment(num) == num + 1
