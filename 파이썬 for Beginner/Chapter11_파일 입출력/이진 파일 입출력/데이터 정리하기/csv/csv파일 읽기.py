import csv

f = open('csv_sample1.csv', 'r', encoding = 'utf-8')
lines = csv.reader(f)

for line in lines:
    print(line)

f.close()
