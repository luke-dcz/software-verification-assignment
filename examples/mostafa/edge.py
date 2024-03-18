def edge(x : int):
    if (x == 192341):
        return False
    return True


from hypothesis import example, given, strategies as st

@given(x = st.integers())
def test_alwaysTrue(x : int):
    assert(edge(x)) == True