WORDLE_SIZE = 5
#comment whichever one you're not using, I recommend using the full words.txt since answers.txt is outdated and might miss answers
FILENAME = "words.txt"
#FILENAME = "answers.txt"

from string import ascii_lowercase

with open(FILENAME, "r") as words:
    lines = words.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip()

def charInWord(char, word):
    for c in word:
        if(char == c):
            return True
    return False

def eliminateLetter(char, words): #if there's a double letter and one is grey, it'll eliminate all single letters too
    for x in range(len(words)-1, -1, -1):
        if charInWord(char, words[x]):
            words.pop(x)
    return words

def eliminateYellow(char, pos, words):
    for x in range(len(words)-1, -1, -1):
        if (not charInWord(char, words[x])):
            words.pop(x)
        elif (words[x][pos] == char):
            words.pop(x)
    return words

def findMatch(char, i, words):
    for x in range(len(words)-1, -1, -1):
        if (words[x][i] != char):
            words.pop(x)
    return words

def runSolver():
    loop = "t"
    while (loop == "t"): 
        word = input("Enter a 5 letter word: ")
        accuracy = input("How correct was the word? 0 = grey, 1 = yellow, 2 = green: ")
        for i in range (5):
            char = word[i]
            acc = accuracy[i]
            if (acc == '0'):
                lines = eliminateLetter(char, lines)
            elif (acc == '1'):
                lines = eliminateYellow(char, i, lines)
            elif (acc == '2'):
                lines = findMatch(char, i, lines)    
        print(lines)
        loop = input("Continue? (t or f): ")

#####TESTS BEGIN HERE!!!######
from hypothesis import example, given, strategies as st
from hypothesis import register_random
#import random #OK YOU CAN'T USE RANDOM IN HYPOTHESIS IT RLY DOESN'T LIKE IT, DO NOT USE RANDOM

@st.composite
def pick_char_word(draw):
    word = draw(five_letter_word)
    char = draw(st.sampled_from(word))
    return char, word

five_letter_word = st.text(alphabet=st.characters(whitelist_categories=('Ll', 'Lu')),min_size=5, max_size=5)

@given(pick_char_word())
def test_charInWord_true(toople):
    c, word = toople
    assert charInWord(c, word) == True

#to avoid using definition in the filter expression, I blacklisted the characters that could appear in the word in c
@given(word = five_letter_word, c = st.characters(blacklist_categories=('Ll', 'Lu')))
def test_charInWord_false(c, word):
    print(c, word)
    assert charInWord(c, word) == False

if __name__ == "__main__":
    test_charInWord_true()
    test_charInWord_false()    