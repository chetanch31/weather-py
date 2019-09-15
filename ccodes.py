#Get country codes

import json

with open("codes.json") as obj:
	data = json.load(obj)

def lookup(name):
	for indc in range(len(data)):
		if data[indc]["name"] == name:
			return data[indc]["alpha-2"]
	else:
		return "Please enter a valid country name"

print(lookup(input("Enter a country name: ")))
