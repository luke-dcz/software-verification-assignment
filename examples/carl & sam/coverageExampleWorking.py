

def obvious(num):
    if num < 10:
        return "Num is less than 10"
    elif num == 10:
        return "Num is 10"
    else:
        return "Num is greater than 10"
    

def test_coverage():
    assert obvious(10) == "Num is 10"
    assert obvious(5) == "Num is less than 10"