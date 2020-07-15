import csv
import json
import urllib
import urllib.request

##iterate all records in the data
def dGenerateFE():

    with open("approved-food-establishments-as-at-1-july-2020.csv", newline='') as csvfile:
        areader = csv.reader(csvfile, delimiter=',',doublequote=False)
            #print(f)

        for row in areader:
            #count+=1
            #print(count)
            yield row


allrec = []
for row in dGenerateFE():

    if len(allrec)>9:
        break

    if len(row) != 71:
        continue
        print("hello")

    #first row
    #print(row)
    if row[0]=="\ufeffAppNo":
        allrec.append(row)
        continue
    
    #if x and y are provided, use them?    

    #69 is y
    #68 is x

    #"TradingName",[1]
    #    "Address1",[2]
    #    "Address2",[3]
    #    "Address3",[4]
    #    "Town",[5]
    #    "Postcode",[6]
    #    "Country", [7]

    srch1 = row[1]+","+  row[2]+","+row[3]+","+row[4]+","+row[5]
    srch1 = srch1.replace(" ", "%20")
    #if the post code is correct use it
    srch2 = row[6]
    srch2 = srch2.replace(" ", "%20")

    #maybe use coord by converting to long/lat


    try:

        iq = "https://us1.locationiq.com/v1/search.php?key=9135f38dfca3ca&q="+srch1+"&format=json"
        url = iq
        print(url)
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        data = response.read()
        values = json.loads(data)

        if row[6]  in values[0]["display_name"]:
            row[68]=values[0]["lat"]
            row[69]=values[0]["lon"]
            allrec.append(row)
            continue

        iq = "https://us1.locationiq.com/v1/search.php?key=9135f38dfca3ca&q="+srch2+"&format=json"
        url = iq
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        data = response.read()
        values = json.loads(data)

        row[68]=values[0]["lat"]
        row[69]=values[0]["lon"]
        allrec.append(row)
        continue
    except urllib.error.HTTPError as e:
        continue




    #url = "https://www.bgs.ac.uk/data/webservices/CoordConvert_LL_BNG.cfc?method=BNGtoLatLng&easting=586500&northing=245739"
    #req = urllib.request.Request(url)
    #response = urllib.request.urlopen(req)
    #data = response.read()
    #values = json.loads(data)

    

    allrec.append(row)

    print(len(allrec))

#now wrint a json
data = allrec
with open('dataFEll.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)





