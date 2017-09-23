import csv


# Clean up code to make usable
with open("../Data Sets/Upcoming_Demolitions.csv") as demo, \
     open("temp.csv", "w") as temp, \
     open("upcomingdemos.csv", "w") as ndemo:
    flag = 0
    for line in demo:
        for char in line:
            if char == '"':
                flag ^= 1
            if flag:
                if char == "\n":
                    temp.write(" ")
                else:
                    temp.write(char)
            else:
                temp.write(char)
    temp.close()
    temp = open("temp.csv", "r")
    demoreader = csv.reader(temp)
    next(demoreader)
    ndemo.write("date,district,latitude,longitude\n")
    for line in demoreader:
        ndemo.write(line[4] + ',' + ','.join(line[6:9]) + '\n')
