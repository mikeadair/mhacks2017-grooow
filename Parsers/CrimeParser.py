import csv
import re

# # Clean up code to make usable
# with open("../Data Sets/Crime.csv") as crime, \
#      open("crime.csv", "w") as ncrime:
#     flag = 0
#     for line in crime:
#         for char in line:
#             if char == '"':
#                 flag ^= 1
#             if flag:
#                 if char == "\n":
#                     ncrime.write(" ")
#                 else:
#                     ncrime.write(char)
#             else:
#                 ncrime.write(char)

with open("crime.csv") as crime, \
    open("../Data Sets/ParsedData/crime.csv", "w") as ncrime:
    crimereader = csv.reader(crime)
    next(crimereader)
    ncrime.write("date,district,latitude,longitude\n")
    for line in crimereader:
        res = re.search(r'[(]{1}([-\d.]+)[,\s]+([-\d.]+)[)]{1}', line[14])
        if res:
            if line[11] != '':
                ncrime.write(','.join([line[7][:11], line[11][-1], res[1],
                                       res[2]]) + '\n')
