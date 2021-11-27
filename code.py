import csv      

customer_titles = None
customers = None
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



# print()
# product_titles, products = readfile("Products.csv")
# print("Product Titles", product_titles)
# print("Products", products)

def get_customers():
    global customer_titles
    global customers
    customer_titles, customers = readfile("Customers.csv")        

    customer_details = []
    for customer in customers:
        c = {"name": customer[0], "address": customer[1], "product": customer[2], "quantity": customer[3], "amount": customer[4]}
        customer_details.append(c)
    
    #print(customer_details)


def get_products():
    global product_titles
    global products
    product_titles, product_detais = readfile("Products.csv")

    for product in product_detais:
        p = {"name":product[0],"price":product[1]}
        products.append(p)
    
    #print(products)

get_customers()

print()

get_products()

print(customers)
print()
print(products)

# def total_amounts_due():
#     customer()
#     #product()

#     # for x in cus:
#     #     print()

# total_amounts_due()



