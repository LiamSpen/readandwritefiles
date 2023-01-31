import csv

with open("EmployeePay.csv", 'r') as Employee_Pay:
    Employee_Pay = csv.reader(Employee_Pay)
    next(Employee_Pay)

    print("ID    First Name      Last Name       Salary          Bonus           Total Pay")
    print("-------------------------------------------------------------------------------")

    for line in Employee_Pay:
        totalPay = float(line[3]) * (1+float(line[4]))
        print(
            f"{line[0]:5s} {line[1]:15s} {line[2]:15s} {line[3]:15s} {line[4]:15s} ${round(totalPay,2)}")
