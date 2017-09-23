import json


def is_in_district(nvert, lat, lng, testlat, testlng):
    j, c = nvert -1, 0

    for i in range(nvert):
        if (((lng[i] > testlng) != (lng[j] > testlng)) and
                (testlat < (lat[j] - lat[i]) * (testlng - lng[i])
                    / (lng[j] - lng[i]) + lat[i])):
            c = ~c
        j = i
    return c

def find_district(districts, lat, long):
    for district in districts:
        if is_in_district(len(districts[district]["lat"]),
                          districts[district]["lat"],
                          districts[district]["lng"], lat, long):
            return district[1]
    return "failed"

x = [0,4,0,4]
y = [0,0,4,4]
testx = 3
testy = 2

print(is_in_district(4, x, y, testx, testy))


# with open("Data Sets/districts.json") as districts:
#     distjson = json.load(districts)
#     lat, lng = 42.393328,-83.231589
#     print(find_district(distjson, lat, lng))

