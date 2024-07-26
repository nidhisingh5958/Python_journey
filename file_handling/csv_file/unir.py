import csv
def pro7():
             fields = []
             rows = []
             with open('university_records.csv', newline='') as f:
                          data = csv.reader(f)
                          fields = next(data)
                          print('Field names are:')
             for field in fields:
                          print(field, '\t')
                          print()
                          print('Data of CSV File:')
             for i in data:
                          print('\t'.join(i))
                          print('\nTotal no. of rows: %d'%(data.line_num))
                          f.close()
pro7()
