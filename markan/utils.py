import csv
import json

def ToCSV(File, Data):
    print('markan: writing to', File + '...')
    f = open(File, 'w')
    w = csv.writer(f)
    w.writerow(Data[0].keys())
    for v in Data:
        w.writerow(v.values())

def ToJSON(File, Data):
    print('markan: writing to', File + '...')
    f = open(File, 'w')
    for i in Data:
        f.write(i)
