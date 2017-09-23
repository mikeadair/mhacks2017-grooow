import csv

with open("../Data Sets/PARCELS.csv") as parcels, \
    open("parcels.csv", "w") as nparc:
    parcelreader = csv.reader(parcels)
    next(parcelreader)
    nparc.write("district,address,price,sale date\n")
    for line in parcelreader:
        if line[40] != '':
            nparc.write(','.join([line[5], line[8] + " " + line[12], line[39],
                                  line[40][0:11]]) + '\n')
