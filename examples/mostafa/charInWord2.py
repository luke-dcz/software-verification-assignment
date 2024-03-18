def charInWord(char, word):
    for c in word:
        if(char == c):
            return True
    return False

#####TESTS BEGIN HERE!!!######
from hypothesis import example, given, strategies as st

five_letter_word = st.text(alphabet=st.characters(whitelist_categories=('Ll', 'Lu')),min_size=5, max_size=5)


def test_charInWord_true(c, word):
    assert charInWord(c, word) == True

def test_charInWord_false(c, word):
    assert charInWord(c, word) == False

if __name__ == "__main__":
    test_charInWord_true()
    test_charInWord_false()    