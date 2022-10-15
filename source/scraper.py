from bs4 import BeautifulSoup
from urllib.request import urlopen
 
# Input day, month, and year
year = input("enter year: ")
month = input("enter month: ")
day = input("enter date: ")
 
# Input dining hall (Douglass or Danforth)
hall = input("Enter dining station (lowercase): ")
if hall == 'douglass':
    hall = 'douglass-dining'
else:
    hall = 'danforth-dining-center'
 
# Initialize Beautiful Soup
url = "https://dining.rochester.edu/locations/" + hall + "/?date=" + year + "-" + month + "-" + day
page = urlopen(url)
html = page.read().decode("utf-8")
 
soup = BeautifulSoup(html, "html.parser")
 
# Open files
f = open("outputfile.txt", "w")
 
 
# Find all food and store in an array
 
# V1: Just store all the food in a 1D Array
# all_food = []
# for links in soup.findAll(id="content"):
#     for link in links.find_all('a', class_="show-nutrition"):
#         all_food.append(link.get_text())
#         # f.write(link.get_text() + "\n")
 
#V2: Store food in a 3D Array: Dimension 1: Time; Dimension 2: Station; Dimension 3: Food
all_food = []
all_times = []
all_stations = []
 
# content is to remove header and footer
content = soup.find(id = "content")
 
for times in content.find_all('div', class_ = "c-tabs-nav__link-inner"):
    all_times.append(times.get_text())
    all_food.append([])
 
for time in all_times:
    f.write(time + " | ")
f.write('\n')
 
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
 
for stations in all_stations:
    for station in stations:
        f.write(station + ' | ')
    f.write("\n")
 
f.write("\n")
 
for times in all_food:
    for stations in times:
        for food in stations:
            f.write(food + ' | ')
        f.write("\n")
    f.write('\n')
 
 

