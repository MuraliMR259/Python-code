import json
import csv

with open('orders_data.json') as json_file:
    data = json.load(json_file)

fname1 = "Customers.csv"

with open(fname1,"w") as json_file:
    csv_file = csv.writer(json_file)
    csv_file.writerow(["CustomerID","First Name","Last Name","Customer Email"])
    for item in data["items"]:
        csv_file.writerow([item["customer_id"],item["customer_firstname"],item["customer_lastname"],item["customer_email"]])

fname1 = "Customers.csv"

with open(fname1,"w") as json_file:
    csv_file = csv.writer(json_file)
    csv_file.writerow(["CustomerID","First Name","Last Name","Customer Phone","Customer Email"])
    for item in data["items"]:
        csv_file.writerow([item["customer_id"],item["customer_firstname"],item["customer_lastname"],item["billing_address"]["telephone"],item["customer_email"]])

fname2 = "Customer Address.csv"

with open(fname2,"w") as json_file:
    csv_file = csv.writer(json_file)
    csv_file.writerow(["CustomerID","AddressID","Address Type","Street Address","City","Region","Country","Postcode"])
    for item in data["items"]:
        csv_file.writerow([item["customer_id"],item["entity_id"],item["billing_address"]["address_type"],item["billing_address"]["street"][0],item["billing_address"]["city"],item["billing_address"]["region"],item["billing_address"]["country_id"],item["billing_address"]["postcode"]])
