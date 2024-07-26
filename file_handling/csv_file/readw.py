import csv
fields = ['SNo', 'Batsman', 'Team', 'Runs' ,'Highest']
rows = [ ['1', 'K L Rahul', 'KXI', '670', '132*'], ['2', 'S Dhawan', 'DC', '618', '106*'],
         ['3', 'David Warner', 'SRH', '548', '85*'],['4', 'Shreyas Iyer', 'DC', '519', '88*'],
         ['5', 'Ishan Kishan', 'MI', '516', '99']]

filename= 'top5.csv'
with open(filename, 'w') as csvfile:
             csvwriter = csv.writer(csvfile) 
             csvwriter.writerow(fields)  
             csvwriter.writerows(rows)    

