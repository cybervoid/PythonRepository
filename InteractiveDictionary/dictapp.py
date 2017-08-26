import json

#help(json.load)
data = json.load(open("data.json"))
type(data)
#print(data["rain"])

def translate(w):
    if w in data:
        return data[w]
    else:
        return "Word does not exist. Please check again."

word = input("Enter word: ")

print(translate(word))
