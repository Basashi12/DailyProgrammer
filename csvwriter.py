# Challenge 26 Intermediate
# Harder than expected.  Sorta works

import csv

# Entry must be a list format
# Sheet is CSV you want to add to
# Entry is data you want to add to the CSV

def writedata(sheet, entry):
    sheetdata = []
    # reading the CSV and storing the info
    with open(sheet, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            sheetdata.append(row)
    # adding entry to the info
    sheetdata.append(entry)
    # writing everything to the CSV
    with open(sheet, 'w') as csvfile:
        csvwriter = csv.writer(csvfile,delimiter = ',')
        for row in sheetdata:
            csvwriter.writerow(row)

# somehow there are extra lines added to the CSV (could be due to LibreOffice)
