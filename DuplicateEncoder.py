import collections
def duplicate_encode(word):
    word = word.lower()
    str = ""
    results = collections.Counter(word)
    for key in word:
        if results[key] > 1:
            str= str + ")"
        else:
            str=str + "("
    return str


print(duplicate_encode("din"))