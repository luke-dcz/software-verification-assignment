def charInWord(char, word):
    for c in word:
        if(char == c):
            return True
    return False

#####TESTS BEGIN HERE!!!######
def test_charInWord_true(c, word):
    assert charInWord(c, word) == True

def test_charInWord_false(c, word):
    assert charInWord(c, word) == False

if __name__ == "__main__":
    test_charInWord_true()
    test_charInWord_false()    