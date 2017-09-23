import csv
import re


# Clean up code to make usable
# with open("Data Sets/LiquorLicenses.csv") as liq, \
#      open("liquor.csv", "w") as nliq:
#     flag = 0
#     for line in liq:
#         for char in line:
#             if char == '"':
#                 flag ^= 1
#             if flag:
#                 if char == "\n":
#                     nliq.write(" ")
#                 else:
#                     nliq.write(char)
#             else:
#                 nliq.write(char)

with open("Data Sets/LiquorLicenses.csv") as liq, \
        open("liqlocs.csv", "w") as locs:
    liqreader = csv.reader(liq)
    locs.write("latitude,longitude\n")
    for line in liqreader:
        res = re.search(r'[(]{1}([-\d.]+)[,\s]+([-\d.]+)[)]{1}', line[9])
        if res:
            locs.write(res[1] + ',' + res[2] + '\n')





