import json
from difflib import get_close_matches
#Calculate proximity ratio
#from difflib import SequenceMatcher
#print(SequenceMatcher(a="rain", b="rainn").ratio())
dict = json.load(open("data.json"))

def get_right_word(word):
    word = word.lower()
    if word in dict:
        return (True, word)
    elif word.title() in dict:
        return (True, word.title())
    else:
        close_matches = get_close_matches(word, dict.keys(), 1, 0.8)
        if len(close_matches) > 0:
            right_word =  close_matches[0]
            user_option = input("Did you mean %s instead? Enter Y if yes, and N if no: " % right_word)
            if user_option.upper() == "Y":
                return (True, right_word)
            else:
                return (False, word)
        else:
            return (False, word)

def translate(word):
    meanings = dict[word]
    formatted = "\n".join(meanings)
    return formatted

word = input("Enter word: ")
rg = get_right_word(word)
if rg[0]:
    print(translate(rg[1]))
else:
    print("The word %s doesn't exist. Please double check it" % word)
