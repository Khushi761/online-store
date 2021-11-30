import csv      
import turtle


screen_x = 475
screen_y = 300
customer_titles = None
customers = []
products = []
product_titles = None
balances = None

t = turtle.Turtle()

def setup():
    sc = turtle.Screen()
    sc.setup(screen_x *2, screen_y*2)
    t.penup()
    t.hideturtle()
    t.setposition(390 - screen_x, screen_y - 50)
    t.write("Store Dashboard", font=("Arial", 20, 'normal', 'bold', 'italic', 'underline'))

def read_data():
    customer_filename = turtle.textinput("Customers Filename", "Please enter customer filename")
    product_filename = turtle.textinput("Products Filename", "Please enter products filename")
    get_customers(customer_filename)
    get_products(product_filename)
    total_amounts_due()

def create_customer_table():
    t.setposition(10 - screen_x, screen_y - 60)
    t.pendown()
    t.setposition(200 - screen_x, screen_y - 60)
    t.penup()
    
    t.setposition(10 - screen_x, screen_y - 200)
    t.pendown()
    t.setposition(200 - screen_x, screen_y - 200)
    t.penup()

    t.setposition(10 - screen_x, screen_y - 200)
    t.pendown()
    t.setposition(10 - screen_x, screen_y - 60)
    t.penup()

    t.setposition(200 - screen_x, screen_y - 60)
    t.pendown()
    t.setposition(200 - screen_x, screen_y - 200)
    t.penup()

    pass

def readfile(file_name):
    data = []
    with open(file_name,encoding='utf-8-sig') as f:
        nextLine = f.readline()[:-1]
        titles = nextLine.split(",")
        for nextLine in f.readlines():
            data.append(nextLine[:-1].split(","))
    
    return (titles, data)

def get_customers(filename):
    global customer_titles
    global customers
    customers = []
    customer_titles, customer_details = readfile(filename)        

    for customer in customer_details:
        c = {"name": customer[0], "address": customer[1], "product": customer[2], "quantity": int(customer[3]), "amount": int(customer[4])}
        customers.append(c)

def get_products(filename):
    global product_titles
    global products
    products = []
    product_titles, product_details = readfile(filename)

    for product in product_details:
        p = {"name":product[0],"price":int(product[1])}
        products.append(p)

def total_amounts_due():
    global balances

    balances = {}
    for x in customers:
        amount_due = 0     
        for y in products:
            if x["product"] == y["name"]:
                price = y["price"]
                qty = x["quantity"]
                amount_to_pay = price * qty
                amount_due = amount_to_pay - x["amount"]

        
        balances[x["name"]] = amount_due

    #print(amount_due)

# get_customers()

# print()

# get_products()

# total_amounts_due()

# print(balances)


if __name__ == "__main__":
    setup()
    #read_data()
    create_customer_table()
    turtle.mainloop()