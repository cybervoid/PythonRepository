import json

#help(json.load)
data = json.load(open("data.json"))
type(data)
#print(data["rain"])

def translate(word):
    return data[word]

word = input("Enter word: ")

print(translate(word))
