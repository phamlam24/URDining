import json

with open('outputfile.json') as json_file:
    json_data = json.load(json_file)

def time_extract(s):
    time = []
    s1 = s.split('(')[1].replace(')', "")
    time.append(s1.split('-')[0])
    time.append(s1.split('-')[1])
    
    if 'am' in time[0]:
        time[0] = time[0].replace("am", "")
        if(":30" in time[0]):
            time[0] = time[0].replace(":30", ".5")
        time[0] = float(time[0])
        if(time[0] == 12 or time[0] == 12.5):
            time[0] = time[0] - 12
        else:
            time[0] = time[0]

    else: 
        if 'pm' in time[0]:
            time[0] = time[0].replace("pm", "")
            if(":30" in time[0]):
                time[0] = time[0].replace(":30", ".5")
            time[0] = float(time[0])
            if(time[0] == 12 or time[0] == 12.5): 
                time[0] = time[0]
            else:
                time[0] = time[0] + 12
    
    if 'am' in time[1]:
        time[1] = time[1].replace("am", "")
        if(":30" in time[1]):
            time[1] = time[1].replace(":30", ".5")
        time[1] = float(time[1])
        if(time[1] == 12 or time[1] == 12.5):
            time[1] = time[1] - 12
        else:
            time[1] = time[1]

    else:
        if 'pm' in time[1]:
            time[1] = time[1].replace("pm","")
            if(":30" in time[1]):
                time[1] = time[1].replace(":30", ".5")
            time[1] = float(time[1])
            if(time[1] == 12 or time[1] == 12.5):
                time[1] = time[1]
            else:
                time[1] = time[1] + 12

    return time

def getTimes(day,hall):
    time = []
    correctDateArray = json_data[day]
    for x in correctDateArray:
        list1 = list(x.values())
        if list1[0] == hall:
            if time_extract(list1[1]) in time:
                continue
            else:
                time.append(time_extract(list1[1]))

    return time

def getStations(day,hall,mealtime):
    stations = []
    correctDateArray = json_data[day]
    for x in correctDateArray:
        list1 = list(x.values())
        if list1[0] == hall:
            if list1[1] == mealtime:
                if list1[2] in stations:
                    continue
                else:
                    stations.append(list1[2])
    return stations

def getDish(day,hall,mealtime,station):
    dishes = []
    correctDateArray = json_data[day]
    for x in correctDateArray:
        list1 = list(x.values())
        if list1[0] == hall:
            if list1[1] == mealtime:
                if list1[2] == station:
                    if list1[3] in dishes:
                        continue
                    else:
                        dishes.append(list1[3])
    return dishes

def updateReview(day,hall,mealtime,station,dish,rating):
    correctDateArray = json_data[day]
    for x in correctDateArray:
        list1 = list(x.values())
        if list1[0] == hall:
            if list1[1] == mealtime:
                if list1[2] == station:
                    if list1[3] == dish:
                        list1[4].append(rating)

def getAverageRating(day, hall, mealtime,station,dish):
    correctDateArray = json_data[day]
    for x in correctDateArray:
        list1 = list(x.values())
        if list1[0] == hall:
            if list1[1] == mealtime:
                if list1[2] == station:
                    if list1[3] == dish:
                        return sum(list1)/len(list1)

def reset():
    for i in range (len(json_data)):
        eachDateArray = json_data[i]
        for x in eachDateArray:
            list1 = list(x.values())
            list1[4].clear()
            list1[5].clear()
            list1[5].append(0)
            list1[5].append(0)

