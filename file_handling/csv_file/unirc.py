import csv
with open('university_records.csv', newline='') as f:
             data = csv.DictReader(f)
             print('Name','\t', 'CGPA')
             print('*'*50)
for i in data:
             print(i['StudentName'], '\t',i['Score'])
