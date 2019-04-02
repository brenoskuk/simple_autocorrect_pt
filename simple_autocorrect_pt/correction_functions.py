import re
import spacy
from collections import Counter

x = spacy.load("pt_core_news_sm")

# add all the punctuation marks you want.
punctuations = ".,:;?%;"


# lower all characters
def all_lower(text_input):
    return text_input.lower()


# corrects slang for unusual words in portuguese
def correct_slang(text_input):
    dic = {" n ": " não ", " ta ": " está ", " tá ": " está ", " q ": " que ", "qm": "quem", "vc ": "você ",
           "vcs ": "vocês ", "ql ": "qual ", " eh ": " é ", "td ": "tudo "}
    for key in dic.keys():
        text_input = text_input.replace(key, dic[key])
    return text_input


# used for dealing with punctuation
def removeAndReturnLastCharacter(a):
    c = a[-1]
    a = a[:-1]
    return c


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


# simple autocorrect (if word contains a number won't alter the word)
def correct_user_input(user_input):
    user_input = all_lower(user_input)
    user_input = correct_slang(user_input)
    split_input = user_input.split()
    # print(split_input)
    checked_input = ''
    for i in split_input:
        if hasNumbers(i):
            checked_input += i
        elif i[-1:] in punctuations:
            temp = removeAndReturnLastCharacter(i)
            checked_input += correction(i)
            checked_input += temp
            checked_input += " "
        else:
            checked_input += correction(i)
            checked_input += " "
    return checked_input


# autocorretor (by Peter Norvig)
def words(text):
    return re.findall(r'\w+', text.lower())


WORDS = Counter(words(open("venv/lib64/python3.6/site-packages/simple_autocorrect_pt/corpus.txt").read()) + list(x.vocab.strings))


def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N


def correction(word):
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)


def candidates(word):
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)


def edits1(word):
    "All edits that are one edit away from `word`."
    letters = 'aãâáàbcdeêéfghiíjklmnoóôpqrstuúvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
