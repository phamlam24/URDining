import json
from bs4 import BeautifulSoup
from urllib.request import urlopen
 
# # Input day, month, and year
# year = input("enter year: ")
# month = input("enter month: ")
# day = input("enter date: ")
 
# # Input dining hall (Douglass or Danforth)
# hall = input("Enter dining station (lowercase): ")
# hall_link = ''
# if hall == 'douglass':
#     hall_link = 'douglass-dining'
# else:
#     hall_link = 'danforth-dining-center'
 
# # Initialize Beautiful Soup
# url = "https://dining.rochester.edu/locations/" + hall_link + "/?date=" + year + "-" + month + "-" + day
# page = urlopen(url)
# html = page.read().decode("utf-8")
 
# soup = BeautifulSoup(html, "html.parser")
 
# Open files
f = open("output/outputfile.json", "w")
 
 
# Find all food and store in an array
 
# V1: Just store all the food in a 1D Array
# all_food = []
# for links in soup.findAll(id="content"):
#     for link in links.find_all('a', class_="show-nutrition"):
#         all_food.append(link.get_text())
#         # f.write(link.get_text() + "\n")
 



#V2: Store food in a 3D Array: Dimension 1: Time; Dimension 2: Station; Dimension 3: Food

# for time in all_times:
#     f.write(time + " | ")
# f.write('\n')

# for stations in all_stations:
#     for station in stations:
#         f.write(station + ' | ')
#     f.write("\n")
 
# f.write("\n")
 
# for times in all_food:
#     for stations in times:
#         for food in stations:
#             f.write(food + ' | ')
#         f.write("\n")
#     f.write('\n')
 
#V3: Store all data in a dictionary in order to parse to JSON


# print(data)


#V4: Combine all together to create a massive JSON of everyday from 2022-9-1 to 2022-10-15
data = {}

def getDataOneDay(day, month, year):
    print(day)
    if(day < 10):
        day = str(0) + str(day)
    if(month < 10):
        month = str(0) + str(month)
    # Initialize Beautiful Soup
    url = "https://dining.rochester.edu/locations/" + "douglass-dining" + "/?date=" + str(year) + "-" + str(month) + "-" + str(day)
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    all_food = []
    all_times = []
    all_stations = []
    
    # content is to remove header and footer
    content = soup.find(id = "content")
    
    for times in content.find_all('div', class_ = "c-tabs-nav__link-inner"):
        all_times.append(times.get_text())
        all_food.append([])
    
    i = 0
    for times in content.find_all('div', class_ = "c-tab"):
        all_stations.append([])
        j = 0
        for stations in times.find_all('div', class_ = "menu-station"):
            all_stations[i].append(stations.find('h4').get_text())
            all_food[i].append([])
            for food in stations.find_all('a'):
                all_food[i][j].append(food.get_text())
            j += 1
        i += 1
    
    dayData = []
    mealData = {

    }
    for i in range(len(all_times)):
        cur_time = all_times[i]
        for j in range(len(all_stations[i])):
            cur_station = all_stations[i][j]
            for k in range(len(all_food[i][j])):
                cur_food = all_food[i][j][k]
                mealData = {
                    "hall": "douglass",
                    "time": cur_time,
                    "station": cur_station,
                    "dish": cur_food,
                    "rating": [],
                    "frequency": [0,0],
                }
                dayData.append(mealData)
    
    # Initialize Beautiful Soup
    url = "https://dining.rochester.edu/locations/" + "danforth-dining-center" + "/?date=" + str(year) + "-" + str(month) + "-" + str(day)
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    all_food = []
    all_times = []
    all_stations = []
    
    # content is to remove header and footer
    content = soup.find(id = "content")
    
    for times in content.find_all('div', class_ = "c-tabs-nav__link-inner"):
        all_times.append(times.get_text())
        all_food.append([])
    
    i = 0
    for times in content.find_all('div', class_ = "c-tab"):
        all_stations.append([])
        j = 0
        for stations in times.find_all('div', class_ = "menu-station"):
            all_stations[i].append(stations.find('h4').get_text())
            all_food[i].append([])
            for food in stations.find_all('a'):
                all_food[i][j].append(food.get_text())
            j += 1
        i += 1
    
    for i in range(len(all_times)):
        cur_time = all_times[i]
        for j in range(len(all_stations[i])):
            cur_station = all_stations[i][j]
            for k in range(len(all_food[i][j])):
                cur_food = all_food[i][j][k]
                mealData = {
                    "hall": "danforth",
                    "time": cur_time,
                    "station": cur_station,
                    "dish": cur_food,
                    "rating": [],
                    "frequency": [0,0],
                }
                dayData.append(mealData)
    data[str(year) + "-" + str(month) + "-" + str(day)] = dayData

for i in range(1, 31):
    getDataOneDay(i, 9, 2022)

for i in range(1, 16):
    getDataOneDay(i, 10, 2022)

f.write(json.dumps(data, indent=4))