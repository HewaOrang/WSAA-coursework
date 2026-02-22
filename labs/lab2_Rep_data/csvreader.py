# Program: csvreader.py
# This program reads in data and outputs each line as a list
# Author: Hewa Orang

import csv

FILENAME = "data.csv"
DATADIR = r"C:\Users\OrangH\Desktop\WSAA-coursework\labs\lab2_Rep_data"

with open(DATADIR + "\\" + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    Count = 0
    for line in reader:
        total += line['age'] 
        Count += 1
    print (f"average is {total/(Count)}") 

    