import json

#help(json.load)
data = json.load(open("data.json"))
type(data)
#print(data["rain"])

def translate(w):
    w = w.ToLower()
    if w in data:
        return data[w]
    else: #error handling for missing word
        return "Word does not exist. Please check again."

word = input("Enter word: ")

print(translate(word))
