# Challenge 26 Intermediate
# Harder than expected.  Sorta works

import csv

# Entry must be a list format

def writedata(sheet, entry):
    sheetdata = []
    with open(sheet, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            sheetdata.append(row)
    sheetdata.append(entry)
    with open(sheet, 'w') as csvfile:
        csvwriter = csv.writer(csvfile,delimiter = ',')
        for row in sheetdata:
            csvwriter.writerow(row)

# somehow there are extra lines added to the CSV
