import csv 

with open("C:\Users\Home\Desktop\weather-py\all\all.csv","r") as country_list:
    country = csv.reader(country_list)

    for i in country:
        print(i[0])