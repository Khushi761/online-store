import csv      
import turtle
from csv import writer


screen_x = 475
screen_y = 300
customer_titles = None
customers = []
products = []
product_titles = None
balances = None
profit = 0
people = 0

t = turtle.Turtle()

def setup():
    sc = turtle.Screen()
    sc.setup(screen_x *2, screen_y*2)
    sc.bgcolor("yellow")
    t.hideturtle()
    set_border()
    t.penup()
    
    t.setposition(390 - screen_x, screen_y - 50)
    t.write("Store Dashboard", font=("Arial", 20, 'normal', 'bold', 'italic', 'underline'))

def set_border():
    t.penup()
    t.pensize(5)
    t.setposition(-screen_x + 6, screen_y-4)
    t.pendown()
    t.setposition(screen_x-10, screen_y-4)
    t.setposition(screen_x- 10, -screen_y + 8)
    t.setposition(-screen_x+6, -screen_y+ 8)
    t.setposition(-screen_x+ 6, screen_y + 4)
    t.penup()
    t.setposition(-screen_x + 6, screen_y - 60)
    t.pendown()
    t.setposition(screen_x - 10, screen_y - 60)
    t.penup()
    t.setposition(screen_x - 350, screen_y - 60)
    t.pendown()
    t.setposition(screen_x - 350, -screen_y -8)
    t.penup()

def read_data():
    customer_filename = "Customers.csv"#turtle.textinput("Customers Filename", "Please enter customer filename")
    product_filename = "Products.csv"#turtle.textinput("Products Filename", "Please enter products filename")
    get_customers(customer_filename)
    get_products(product_filename)
    total_amounts_due()
    total_amounts_due()

def create_customer_table():
    margin_y = 120

    t.setposition(10 - screen_x, screen_y - 70)
    t.pendown()
    t.setposition(200 - screen_x, screen_y - 70)
    t.penup()
    
    t.setposition(10 - screen_x, screen_y - ((len(customers))*50))
    t.pendown()
    t.setposition(200 - screen_x, screen_y - ((len(customers))*50))
    t.penup()

    t.setposition(10 - screen_x, screen_y - ((len(customers))*50))
    t.pendown()
    t.setposition(10 - screen_x, screen_y - 70)
    t.penup()

    t.setposition(200 - screen_x, screen_y - 70)
    t.pendown()
    t.setposition(200 - screen_x, screen_y - ((len(customers))*50))
    t.penup()

    t.setposition(15 - screen_x, screen_y - 95)

    t.write("Current customers", font=("Arial", 15, 'normal', 'bold', 'italic', 'underline'))

    for x in customers:
        name = x["name"]
        t.setposition(25 - screen_x, screen_y - margin_y)
        t.write(name, font=("Arial", 12, 'normal'))
        margin_y = margin_y + 30
    
def create_product_table():
    
    margin_y = 120

    t.setposition(250 - screen_x, screen_y - 70)
    t.pendown()
    t.setposition(490 - screen_x, screen_y - 70)
    t.penup()
    
    t.setposition(250 - screen_x, screen_y - ((len(products))*50))
    t.pendown()
    t.setposition(490 - screen_x, screen_y - ((len(products))*50))
    t.penup()

    t.setposition(250 - screen_x, screen_y - ((len(products))*50))
    t.pendown()
    t.setposition(250 - screen_x, screen_y - 70)
    t.penup()

    t.setposition(490 - screen_x, screen_y - 70)
    t.pendown()
    t.setposition(490 - screen_x, screen_y - ((len(products))*50))
    t.penup()

    t.setposition(255 - screen_x, screen_y - 95)

    t.write("Products you are selling", font=("Arial", 15, 'normal', 'bold', 'italic', 'underline'))

    for x in products:
        name = x["name"]
        t.setposition(275 - screen_x, screen_y - margin_y)
        t.write(name, font=("Arial", 12, 'normal'))
        margin_y = margin_y + 30

def create_amount_due_box():

    margin_y = 150

    t.setposition( screen_x - 300, screen_y - 70)
    t.pendown()
    t.setposition(screen_x - 90 , screen_y - 70)
    t.penup()
    
    t.setposition(screen_x - 300, screen_y - (people*70))
    t.pendown()
    t.setposition(screen_x - 90, screen_y - (people*70))
    t.penup()

    t.setposition(screen_x - 300, screen_y - 70)
    t.pendown()
    t.setposition(screen_x - 300, screen_y - (people*70))
    t.penup()

    t.setposition(screen_x - 90, screen_y - 70)
    t.pendown()
    t.setposition(screen_x - 90, screen_y - (people*70))
    t.penup()

    t.setposition(screen_x - 290, screen_y - 95)

    t.write("Amounts due by customers", font=("Arial", 15, 'normal', 'bold', 'italic', 'underline'))

    f = open("Amounts.csv")
    for nextLine in f.readlines():
        t.setposition(screen_x - 290, screen_y - margin_y)
        t.write(nextLine, font=("Arial", 12, 'normal'))
        nextLine = f.readline()[:-1]
        t.setposition(screen_x - 400, screen_y - margin_y)
        t.write(nextLine, font=("Arial", 12, 'normal'))
        margin_y = margin_y + 40

def create_profit_box():
    t.setposition( screen_x - 300, screen_y - 70)
    t.pendown()
    t.setposition(screen_x - 90 , screen_y - 70)
    t.penup()
    
    t.setposition(screen_x - 300, screen_y - (len(products))*40)
    t.pendown()
    t.setposition(screen_x - 90, screen_y - (len(products))*40)
    t.penup()

    t.setposition(screen_x - 300, screen_y - 70)
    t.pendown()
    t.setposition(screen_x - 300, screen_y - (len(products))*40)
    t.penup()

    t.setposition(screen_x - 90, screen_y - 70)
    t.pendown()
    t.setposition(screen_x - 90, screen_y - (len(products))*40)
    t.penup()
def total_customers_box():
    pass

def total_products_box():
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
    global people 

    data = []
    amounts = open("Amounts.csv", 'w')
    #balances = {}
    for x in customers:
        amount_due = 0     
        for y in products:
            if x["product"] == y["name"]:
                price = y["price"]
                qty = x["quantity"]
                amount_to_pay = price * qty
                amount_due = amount_to_pay - x["amount"]
                if amount_due > 0:
                    csv.writer(amounts).writerow([x["name"], str(amount_due)])
                    people = people + 1
                    print(people)

def total_profits():
    global profit
    
    for x in customers:
        profit = profit + x["amount"]

def total_customers():
    cus = 0
    for c in customers:
        cus = cus + 1

def total_products():
    prod = 0
    for p in products:
        prod = prod + 1

def total_customers():
    pass

if __name__ == "__main__":
    setup()
    read_data()
    create_customer_table()
    create_product_table()
    create_amount_due_box()
    turtle.mainloop()