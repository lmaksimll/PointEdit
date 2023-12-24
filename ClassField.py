import csv

file = open('PointCsv.csv','r',encoding='utf-8')
#reader = csv.reader(file,delimiter=';',quotechar='"')
reader = csv.DictReader(file,delimiter=';',quotechar='"')

for row in reader:
    print(row)

file2 = open('PointCsv2.csv','w',encoding='utf-8',newline='')

data = [{'x' : '1', 'y' : '1'}]

writer = csv.DictWriter(file2,fieldnames=list(data[0].keys()),delimiter=';',quoting=csv.QUOTE_MINIMAL)

writer.writeheader()

for d in data:
    writer.writerow(d)
