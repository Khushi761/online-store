import csv      

customer_titles = None
customers = []
products = []
product_titles = None

def readfile(file_name):
    data = []
    with open(file_name,encoding='utf-8-sig') as f:
        nextLine = f.readline()[:-1]
        titles = nextLine.split(",")
        for nextLine in f.readlines():
            data.append(nextLine[:-1].split(","))
    
    return (titles, data)


def get_customers():
    global customer_titles
    global customers
    customers = []
    customer_titles, customer_details = readfile("Customers.csv")        

    for customer in customer_details:
        c = {"name": customer[0], "address": customer[1], "product": customer[2], "quantity": customer[3], "amount": int(customer[4])}
        customers.append(c)

def get_products():
    global product_titles
    global products
    products = []
    product_titles, product_details = readfile("Products.csv")

    for product in product_details:
        p = {"name":product[0],"price":int(product[1])}
        products.append(p)

get_customers()

print()

get_products()




def total_amounts_due():
    get_customers()
    get_products()

    print(customers)
    print()
    print(products)

total_amounts_due()
#     # for x in cus:
#     #     print()

# total_amounts_due()



