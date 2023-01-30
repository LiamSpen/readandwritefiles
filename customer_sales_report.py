import csv
with open("sales.csv", 'r') as sales:
    employee_file = csv.reader(sales, delimiter=',')
    firstrow = next(sales)
    secondrow = next(sales)

    total = 0
    ID = secondrow[0] + secondrow[1] + secondrow[2]
    print(ID)
    sales.seek(0)

    with open("salesreport.csv", 'w') as employee_details:
        employee_details = csv.writer(employee_details)
        next(employee_file)
        employee_details.writerow(["Customer"] + ["Total"])

        for record in employee_file:
            if str(ID) == record[0]:
                print(record[0])
                newtotal = float(record[3]) + \
                    float(record[4]) + float(record[5])
                total += newtotal
                place = record[0]
            else:
                total = format(total, '.2f')
                employee_details.writerow([place]+[str(total)])
                total = 0
                ID = record[0]
                newtotal = float(record[3]) + \
                    float(record[4]) + float(record[5])
                total += newtotal
        employee_details.writerow([place]+[str(total)])
