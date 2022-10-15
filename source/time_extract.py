from tokenize import Double


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
    

print(time_extract('dinner(12am-8:30am)'))
