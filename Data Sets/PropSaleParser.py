import csv
import re


with open("PropertySales.csv") as prop, \
    open("propsales.csv", "w") as nprop:
    propreader = csv.reader(prop)
    nprop.write("date,price,address\n")
    next(propreader)
    for line in propreader:
        nprop.write(','.join([line[3], line[4], ' '.join(line[9:13])]) + '\n')