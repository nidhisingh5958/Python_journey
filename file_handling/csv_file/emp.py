import csv
mydict =[{'EmpCode': '1001', 'EName': 'Shobhit', 'Post': 'Manager', 'Salary': '55000', 'Department': 'Finance'},
		{'EmpCode': '1002', 'EName': 'Manmit', 'Post': 'Clerk', 'Salary': '35000', 'Department': 'Office'},
		{'EmpCode': '1003', 'EName': 'Sujal', 'Post': 'Development Officer', 'Salary': '65000', 'Department': 'R & D'},
		{'EmpCode': '1004', 'EName': 'Gayatri', 'Post': 'System Analyst', 'Salary': '53000', 'Department': 'Software'}]
		
fields = ['EmpCode', 'EName', 'Post', 'Salary', 'Department']
filename = "emp.csv"

with open(filename, 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames = fields)
	writer.writeheader()
	writer.writerows(mydict)
