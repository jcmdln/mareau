import csv
import json

def ToCSV(File, Data):
    CSV = open(File, 'w')
    WRT = csv.writer(CSV)
    for i in Data:
        WRT.writerow(i)

def ToJSON(File, Data):
    f = open(File, 'w')
    for i in Data:
        f.write(i)
