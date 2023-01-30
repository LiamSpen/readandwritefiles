import csv

with open("EmployeePay.csv", 'r') as Employee_Pay:
    Employee_Pay = csv.reader(Employee_Pay)

    for line in Employee_Pay:
        print(line)
