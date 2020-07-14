import csv
import json

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

    if len(row) != 71:
        continue    

    allrec.append(row)

#now wrint a json
data = allrec
with open('dataFE.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)





