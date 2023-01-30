import csv
"""
customer_file = csv.reader(open("customers.csv"))
customer_country = csv.writer(open('customer_country.csv'))
"""
with open("customers.csv", 'r') as customer_file:
    customer_file = csv.reader(customer_file, delimiter=',')

    with open("customer_country.csv", 'w') as customer_country:
        customer_country = csv.writer(customer_country)
        next(customer_file)
        customer_country.writerow(["Full Name"] + ["Country"])

        for record in customer_file:
            customer_country.writerow(
                [record[1] + " " + record[2], record[4]])
