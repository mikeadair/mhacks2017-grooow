import csv


with open("../Data Sets/DirtyDataSets/Demolitions.csv") as demos, \
    open("../Data Sets/ParsedData/demolitions.csv", "w") as ndemos:
    demosreader = csv.reader(demos)
    next(demosreader)
    ndemos.write("date,district,latitude,longitude\n")
    for line in demosreader:
        ndemos.write(','.join([line[4], line[6], line[7], line[8]]) + '\n')

