import json
import requests
''' Program to find the weather of any city '''

#base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid=eb005e534aed278632f85a66a668ccf0"

def get(url):
	resp = requests.get(url)
	return resp.json()

def lookup(name):
	with open("codes.json") as obj:
		data = json.load(obj)

	for indc in range(len(data)):
		if data[indc]["name"] == name:
			return data[indc]["alpha-2"]
	else:
		return "Please enter a valid country name"


print("Find the weather of any city!")
print()

while True:
	print("1. Find weather")
	print("2. Find country code")
	print("3. Quit")
	choice = int(input("Enter choice: "))

	if choice==1:
		print()
		print("Which format would you like to get the weather in?")
		print("1. Kelvin")
		print("2. Celsius")
		print("3. Fahrenheit")
		print()

		choice_form = int(input("Enter format: "))
		city = input("Enter your city name: ")
		country_code = input("Enter ISO 3166 alpha-2 code of your country: ")

		base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid=eb005e534aed278632f85a66a668ccf0"

		if choice_form ==1:
			query_url = base_url
			data = get(query_url)
			area = data['name']
			country = data['sys']['country']
			cond = data['weather'][0]['main']
			temp = data['main']['temp']
			humid = data['main']['humidity']
			min_temp = data['main']['temp_min']
			max_temp = data['main']['temp_max']

			print("City name: ",area)
			print("Country: ",country)
			print("Condition: ",cond)
			print(f"Temperature: {temp}"+"°K")
			print(f"Humidity: {humid}"+"%")
			print(f"Minimum Temperature: {min_temp}"+"°K")
			print(f"Maximum Temperature: {max_temp}"+"°K")
			print()
		elif choice_form == 2:
			query_url = base_url + "&units=metric"
			data = get(query_url)
			area = data['name']
			country = data['sys']['country']
			cond = data['weather'][0]['main']
			temp = data['main']['temp']
			humid = data['main']['humidity']
			min_temp = data['main']['temp_min']
			max_temp = data['main']['temp_max']

			print("City name: ",area)
			print("Country: ",country)
			print("Condition: ",cond)
			print(f"Temperature: {temp}"+"°C")
			print(f"Humidity: {humid}"+"%")
			print(f"Minimum Temperature: {min_temp}"+"°C")
			print(f"Maximum Temperature: {max_temp}"+"°C")
			print()
		else:
			query_url = base_url + "&units=imperial"
			data = get(query_url)
			area = data['name']
			country = data['sys']['country']
			cond = data['weather'][0]['main']
			temp = data['main']['temp']
			humid = data['main']['humidity']
			min_temp = data['main']['temp_min']
			max_temp = data['main']['temp_max']

			print("City name: ",area)
			print("Country: ",country)
			print("Condition: ",cond)
			print(f"Temperature: {temp}"+"°F")
			print(f"Humidity: {humid}"+"%")
			print(f"Minimum Temperature: {min_temp}"+"°F")
			print(f"Maximum Temperature: {max_temp}"+"°F")
			print()
	elif choice==2:
		country_name = input("Enter your country name to get ISO 3166 alpha-2 code of your country: ")
		print("Code: ",lookup(country_name))
	elif choice==3:
		break
	else:
		print("Please enter a valid choice!")