import json
import difflib #library to try to match words with approximate names
from difflib import SequenceMatcher
from difflib import get_close_matches
#help(json.load)
data = json.load(open("data.json"))
type(data)
#print(data["rain"])

def translate(w):
    w = w.lower()
    if w in data:
        return w + ": " + data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        key = get_close_matches(w, data.keys())[0]
        print("Did you mean %s instead? [Y]es" % key)
        useri = input()
        if(useri == "y"):
            return data[key]
        else:
            return "Word not found."
    else: #error handling for missing word
        return w + ": " + "Word does not exist. Please check again."

word = input("Enter word: ")

print(translate(word))

#Sequence matcher user:
#SequenceMatcher(None, "rainn", "rain").ratio()
#get_close_matches
#help(get_close_matches) in terminal to view arguments
