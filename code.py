import csv      #the built-in csv module in python is imported so that it can be used to manipulate the excel files used in the program
import turtle       #the python turtle library is imported into the program so that it an be used to generate the graphics required in creating the dashboard
from csv import writer      #the writer function of the csv module is also specifically imported 

#list of global variables created to be further used in the program

screen_x = 475      
screen_y = 300      
customer_titles = None      #some variables have been given the value None as default values of the type NoneType as they will be supplied actual values in terms of dictionaries, lists, etc. later on in the program
customers = []      
products = []
product_titles = None
profit = 0      #Some variables like profit and people are given the value of 0 itself (and not None as it is not a null value but actually holds value of 0), to be used later on in the program
people = 0
cus = 0
prod = 0

#the python module turtle (imported earlier) comes in the type Screen and Turtle, Screen managing the visual screen appearance of the turtle screen and Turtle managing the Turtle that moves on the screen.

t = turtle.Turtle()     #creates a turtle named 't' by calling the Turtle function of the turtle module 

def setup():        #setup function is created in which I define the main elements of the turtle screen and turtle which need to be in a certain specific place and visual form before the program begins
    sc = turtle.Screen()        #calls the Screen function of turtle and assigns it the variable of sc so that it is easier to use the called function later on
    sc.setup(screen_x *2, screen_y*2)       #Uses the sc variable created earlier (which encompasses the called screen function from the turtle module) to create a screen of the size 950 in width (475*2) and 600 in height (300*2) using the global screen_x and screen_y variables created earlier.
    sc.bgcolor("yellow")        #Gives the turtle screen created a background color of yellow
    t.hideturtle()      #hides the turtle shape that moves on the screen so that the user cannot see as it moves to any new set position
    set_border()    #calls the set_border function which i have created later on that deals with all the lines and borders used to create the dashboard in the system.
    t.penup()   #lifts the turtle pen up so that it does not draw anything while it moves to the next position where it is meant to be set
    
    t.setposition(390 - screen_x, screen_y - 50)        #sets the position of the currently hidden turtle using the setposition function and values of 390-screen_x (475), passed as the x value of the coordinate used and screen_y (300)- 50 passed as the y value of the coordinate used. 
    t.write("Store Dashboard", font=("Arial", 20, 'normal', 'bold', 'italic', 'underline'))     #writes the title of the dashboard on the set coordinates and in the format given, i.e. its font being Arial, size 20, bold, etc.

def set_border():       #the set_border function (called in the previous setup function). Used to define the borders and lines of the dashboard separately from other screen elements in an organized manner.
    t.penup()
    t.pensize(5)        #calls the pensize function to change the size of the turtle pen to 5 so that the borders are thicker and more aesthetic
    t.setposition(-screen_x + 6, screen_y-4)        
    t.pendown()     #constant lftting and putting down of the turtle pen so that it only draws lines where needed and not everytime it moves from one position to another
    t.setposition(screen_x-10, screen_y-4)      #line 38-41 create a visible square border around the turtle screen using the setposition function and manipulating the coordinates of x and y using the variables screen_x and screen_y
    t.setposition(screen_x- 10, -screen_y + 8)
    t.setposition(-screen_x+6, -screen_y+ 8)
    t.setposition(-screen_x+ 6, screen_y + 4)
    t.penup()
    t.setposition(-screen_x + 6, screen_y - 60)     #lines 43-50 create a vertical line and horizontal accross the turtle screen to create separations in the dashboard design and make it more organized 
    t.pendown()
    t.setposition(screen_x - 10, screen_y - 60)
    t.penup()
    t.setposition(screen_x - 350, screen_y - 60)
    t.pendown()
    t.setposition(screen_x - 350, -screen_y -8)
    t.penup()

def read_data():        #I created a read_data function separately as I have several files to be read and other functions i created to manage the different functionalities of the dashboard to be called and read.
    customer_filename = turtle.textinput("Customers Filename", "Please enter customer filename")        #i have used the textinput function of the turtle module which allows the program to ask the user for an input for the name of the Customers and Products excel file that they would like the program to read, in the form of an input box whre they can type in their answer. 
    product_filename = turtle.textinput("Products Filename", "Please enter products filename")      #The boxes are assiged variables that point to their values (customer_filename and product_filename) respectively so that the values that the user inputs can be used later on with the vvariable names assigned to them
    get_customers(customer_filename)        #the get_customers and get_products functions are called which i created later on in the program, and the values the user enter for the name of the customers and products files are passed as parameters to these functions respectively so that they can be used in those functions
    get_products(product_filename)
    total_amounts_due()     #lines 57-60 call other functions that i created later on in the program and each function is responsible for its own functionality and role in the program
    total_profits()
    total_products()
    total_customers()

def create_customer_table():        #this function has been created to make a table/box which will display the names of all the current customers of the business
    margin_y = 120

    t.setposition(10 - screen_x, screen_y - 70)     #the following lines all describe coordinates of the box
    t.pendown()
    t.setposition(200 - screen_x, screen_y - 70)
    t.penup()
    
    t.setposition(10 - screen_x, screen_y - ((len(customers))*50))      #I have used len(customers))*50 to describe the height of the box which will depend on the number of customers that exist in the file
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

    t.write("Current customers", font=("Arial", 15, 'normal', 'bold', 'italic', 'underline'))       #after moving the turtle to the set coordinates in line 85, it uses the write function to enter a title for the box that was just created

    for x in customers:     #I have used a for loop to loop through customers which is a list of dictionaries of each customer along with their details. For every dictionary (so for every customer) - 
        name = x["name"]        #the name of the customer is checked through the pair of the "name" key and assigns it the variable name
        t.setposition(25 - screen_x, screen_y - margin_y)       
        t.write(name, font=("Arial", 12, 'normal'))     #writes the name of the customer, obtained from the name variable created earlier
        margin_y = margin_y + 30        #updates the margin_y variable created earlier as it is used to define the y axis and because each name will be lower than the previous one, the y coordinate changes everytime.

#Repeats the previous procedure i used to create a box and write the names of all the customers, this time to create another box besides it to write down all the names of the products that the business sells.
#Naturally, the x and y coordinates will all be different
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

    t.write("Products you are selling", font=("Arial", 15, 'normal', 'bold', 'italic', 'underline'))        #Changed title of the box from the previous to define its elements more appropriately

    for x in products:      #a similar for loop but this loops through products which is a list of dictionaries of every product and extracts the name of each product by pointing to the "name" key in every dictionary of the list.
        name = x["name"]
        t.setposition(275 - screen_x, screen_y - margin_y)
        t.write(name, font=("Arial", 12, 'normal'))     #I have given different font descriptions to the contents and title of the box so that they are able to accurately represent their role.
        margin_y = margin_y + 30

#Repeats the same process of creating a box, this time to show the names of any customers who have any amount due to the business

def create_amount_due_box():

    margin_y = 120

    t.setposition( screen_x - 300, screen_y - 70)
    t.pendown()
    t.setposition(screen_x - 90 , screen_y - 70)
    t.penup()
    
    t.setposition(screen_x - 300, screen_y - (people*60))
    t.pendown()
    t.setposition(screen_x - 90, screen_y - (people*60))
    t.penup()

    t.setposition(screen_x - 300, screen_y - 70)
    t.pendown()
    t.setposition(screen_x - 300, screen_y - (people*60))
    t.penup()

    t.setposition(screen_x - 90, screen_y - 70)
    t.pendown()
    t.setposition(screen_x - 90, screen_y - (people*60))
    t.penup()

    t.setposition(screen_x - 290, screen_y - 95)

    t.write("Amounts due by customers", font=("Arial", 15, 'normal', 'bold', 'italic', 'underline'))

    f = open("Amounts.csv")     #Opens the file Amounts.csv in python and assigns it the variable f
    for nextLine in f.readlines():      #loops through all the lines in the Amounts.csv file using the csv readlines function
        line = nextLine[:-1].split(",")     #removes the newline character from each line using [:-1] and splits every element of the line into a list, each separately identified using the separator ",".
        t.setposition(screen_x - 290, screen_y - margin_y)
        t.write(line[0], font=("Arial", 12, 'normal'))      #Writes the name of the customers in the file, which are written first, hence will be the first element of the list created earlier so are referred using their index line[0]

        t.setposition(screen_x - 200, screen_y - margin_y)      
        t.write(line[1] + " pounds", font=("Arial", 12, 'normal'))      #Changes the x coordinate of the turtle to display the second value in the list created earlier (amounts due by the customers)
        
        margin_y = margin_y + 30

#Repeats the same process of creating a box, this time to show the profit earned by the business

def create_profit_box():
    t.setposition( screen_x - 300, screen_y - (people*70))
    t.pendown()
    t.setposition(screen_x - 90 , screen_y - (people*70))
    t.penup()
    
    t.setposition(screen_x - 300, screen_y - ((people*70)+100))
    t.pendown()
    t.setposition(screen_x - 90, screen_y - ((people*70)+100))
    t.penup()

    t.setposition(screen_x - 300, screen_y - (people*70))
    t.pendown()
    t.setposition(screen_x - 300, screen_y - ((people*70)+100))
    t.penup()

    t.setposition(screen_x - 90, screen_y - (people*70))
    t.pendown()
    t.setposition(screen_x - 90, screen_y - ((people*70)+100))
    t.penup()

    t.setposition(screen_x - 230, screen_y - ((people*70)+20))
    t.write("Total profit", font=("Arial", 15, 'normal', 'bold', 'italic', 'underline'))
    t.setposition(screen_x - 290, screen_y - ((people*70)+50))
    t.write(str(profit) +" pounds", font=("Arial", 20, 'normal'))       #Displays the profit earned by the business using the global profit variable. It changes the value to string first so that it is able to concatenate it with the string " pounds".

#Repeats the same process of creating a box, this time to show the total number of customers that the business has 

def total_customers_box():
    t.setposition( 10 - screen_x, screen_y - ((len(customers)*50)+50))      
    t.pendown()
    t.setposition(200 - screen_x , screen_y - ((len(customers)*50)+50))
    t.penup()
    
    t.setposition(10 - screen_x, screen_y - ((len(customers)*50)+150))
    t.pendown()
    t.setposition(200 - screen_x, screen_y - ((len(customers)*50)+150))
    t.penup()

    t.setposition(10 - screen_x, screen_y - ((len(customers)*50)+150))
    t.pendown()
    t.setposition(10 - screen_x, screen_y - ((len(customers)*50)+50))
    t.penup()

    t.setposition(200 - screen_x, screen_y - ((len(customers)*50)+50))
    t.pendown()
    t.setposition(200 - screen_x, screen_y - ((len(customers)*50)+150))
    t.penup()

    t.setposition(25 - screen_x, screen_y - ((len(customers)*50)+70))
    t.write("Your total customers", font=("Arial", 15, 'normal', 'bold', 'italic', 'underline'))

    t.setposition(20 - screen_x, screen_y - ((len(customers)*50)+100))
    t.write(cus, font=("Arial", 20, 'normal'))      #Uses the global cus variable created earlier to diaplay the number of customers

#Repeats the same process of creating a box, this time to show the total products sold by a business

def total_products_box():
    t.setposition( 250 - screen_x, screen_y - ((len(products)*50)+50))
    t.pendown()
    t.setposition(490 - screen_x, screen_y - ((len(products)*50)+50))
    t.penup()
    
    t.setposition(250 - screen_x , screen_y - ((len(products)*50)+150))
    t.pendown()
    t.setposition(490 - screen_x, screen_y - ((len(products)*50)+150))
    t.penup()

    t.setposition(250 - screen_x, screen_y - ((len(products)*50)+150))
    t.pendown()
    t.setposition(250 - screen_x, screen_y - ((len(products)*50)+50))
    t.penup()

    t.setposition(490 - screen_x, screen_y - ((len(products)*50)+50))
    t.pendown()
    t.setposition(490 - screen_x, screen_y - ((len(products)*50)+150))
    t.penup()

    t.setposition(280 - screen_x, screen_y - ((len(customers)*50)+70))
    t.write("Your total products", font=("Arial", 15, 'normal', 'bold', 'italic', 'underline'))

    t.setposition(280 - screen_x, screen_y - ((len(customers)*50)+100))
    t.write(prod, font=("Arial", 20, 'normal'))

#I have created a readfile function which takes the parameter file_name, which will be passed by the user

def readfile(file_name):
    data = []       #creates an empty list and assigns it the variable data, to be used soon
    with open(file_name,encoding='utf-8-sig') as f:     #Opens the file name that the user gives with the variable f. it is opened like this so that it is closed once it is opened and the data within it is copied,to avoid corruption of the file.
        nextLine = f.readline()[:-1]        #removes the newline character from the first line of  file using ["-1"]
        titles = nextLine.split(",") #Splits the line into a list and names the list 'titles' as it contains the titles of what each column of the excel file represents
        for nextLine in f.readlines():      #loops through the remaining lines which contain the actual details of the file
            data.append(nextLine[:-1].split(","))       #appends each list to the bigger data list created earlier to create a list of several lists with details about every customer/product seoarate.
    
    return (titles, data)       

def get_customers(filename):  #Created a function to extract all the names of customers from the excel file, with the formal parameter to represent the actual parameter of the filename that the user will enter    
    global customer_titles      #Uses these global variables created earlier
    global customers
    customers = []      #Creates an empty list called customers, to be edited later
    customer_titles, customer_details = readfile(filename)      #calls the readfile function, passing it the filename that the user enters as the actual parameter. The readfile function returns titles and data, so this line renames these 2 variables to customer_titles and customer_details respectively  

    for customer in customer_details:       #Loops through the customer details i.e. through the list containing the details of every separate customer and for every customer - 
        c = {"name": customer[0], "address": customer[1], "product": customer[2], "quantity": int(customer[3]), "amount": int(customer[4])} #Creates a dictionary called c, containing the titles of every customer column as the key and the detail according to the extracted file as the value
        customers.append(c)     #appends the dictionary to the customer list created earlier 

#Repeats the same process used to extract the customer names from its excel files and same them in a list of dictionaries, to use the product file enetred by the user and gets its data
def get_products(filename):
    global product_titles
    global products
    products = []
    product_titles, product_details = readfile(filename)

    for product in product_details:
        p = {"name":product[0],"price":int(product[1])}
        products.append(p)

def total_amounts_due():        #Created this function to calculate the total amounts 
    global people   

    amounts = open("Amounts.csv", 'w')      #Creates a new csv file called Amounts, to which i can write the details of any customers with due amounts into
    for x in customers:
        amount_due = 0      #loops through all the customers in the customer list and creates a locat variable to represent the initial amounts due
        for y in products:      #Loops through the list with all the products at the same time
            if x["product"] == y["name"]:       #Checks that if the name of the product that a customer bough exists in the products list(which it should) so this condition should always come out as true,
                price = y["price"]      #Assigns the price of the product (from the products excel file) that checks out true and assigns it the variable price
                qty = x["quantity"]     #Assigns the quantity that the user bought (from teh customers excel file) and assigns it the variable quantity
                amount_to_pay = price * qty     #Uses the values associated with the price and quantity variables created earlier and multiplies them together to calculate the amount that the customer has to pay for a particular purchase
                amount_due = amount_to_pay - x["amount"]        #Calculates the amount due by customers by subtracting the amount paid by customers (extracted from excel file) from the amount that they had to pay. The value will be 0 if they paid in full, else greater than 0 if they did not pay the full amount yet
                if amount_due > 0:
                    csv.writer(amounts).writerow([x["name"], str(amount_due)])      #Writes the name of the name of the customer who has any value greater than 0 (hence they have some amount due), and the price they owe, to the amounts csv file created earlier
                    people = people + 1     #Uses a stepper variable to increment the variasble people each time a name is added into the amounts due flle

def total_profits():        #A function to calculate the total profits of the company using the global variable profits
    global profit
    
    for x in customers:     #for every customer in the list of customers, it checks the amount paid by the customer and adds it to the previous profit value, hence reaching to an accumulated total profit by the last customer
        profit = profit + x["amount"]

def total_customers():      #A function to calculate the total number of customer of the business by using a stepper variable which increments each time the for loop is a new c
    global cus
    for c in customers:
        cus = cus + 1

def total_products():       #A function to calculate the total number of products sold by the business by using a stepper variable which increments each time the for loop is a new p
    global prod
    for p in products:
        prod = prod + 1


if __name__ == "__main__":      #Created an if function which always results in a true value. This is needed to run all the functions created earlier at the same time 
    setup()
    read_data()
    create_customer_table()
    create_product_table()
    create_amount_due_box()
    create_profit_box()
    total_customers_box()
    total_products_box()
    turtle.mainloop()