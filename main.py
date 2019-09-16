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
		if data[indc]["name"].lower() == name.lower():
			return data[indc]["alpha-2"]

	return "Please enter a valid country name"

def printData(query_url,tempUnit):
	data = get(query_url)
	try:
		print(f'''
City name: {data['name']}
Country: {data['sys']['country']}
Condition: {data["weather"][0]["main"]}
Temperature: {data["main"]["temp"]}{tempUnit}
Humidity: {data["main"]["humidity"]}%
Minimum Temperature: {data["main"]["temp_min"]}{tempUnit}
Maximum Temperature: {data["main"]["temp_max"]}{tempUnit}
''')
	except KeyError:
		print("Please enter a valid city name")	

def main():
	while True:
		print('''1: Get details in Kelvin
2: Get details in Celcius
3: Get details in Fahrenheit
4: Quit''')
		choice = int(input("Enter choice: "))
		if choice == 4:	break
		else: 
			city = input("Enter your city name: ")
			country_name = input("Enter your country name: ")
			country_code = lookup(country_name)
			base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid=eb005e534aed278632f85a66a668ccf0"

			if choice ==1: 				printData(base_url, "K")
			elif choice == 2:			printData(base_url + "&units=metric", "°C")
			elif choice ==3 :			printData(base_url + "&units=imperial", "°F")
			else:						print("Please enter a valid choice!")

if __name__ =="__main__":
	main()



		
'''To make sumlimerepl work: store as python-repl.sublime-build
{
    "target": "run_existing_window_command", 
    "id": "repl_python_run",
    "file": "config/Python/Main.sublime-menu"
}
'''

