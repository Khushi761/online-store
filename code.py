import csv      

customers = open("Customers.csv")               #opens the required customers.csv file containing details of all customers
nextLine = customers.readline()[:-1]            #reads the very first title line 

titles = nextLine.split(sep=",")                   

print(titles)
cus = []

products = open("Products.csv")
next = products.readline()
prod = []

def customer():
    
    global customers
    global nextLine
    global cus
    global titles

    dic1 = {}

    while nextLine != "":
        nextLine = customers.readline()[:-1]
        x = nextLine.split(sep=",")
        name = 0

        for title in titles:
            if name != 5:
                dic1[title] = x[name]
                name = name + 1
            else:
                name = 0
        
            print(dic1)
            
    
        cus.append(dic1)

    print(cus)



def product():
    global products
    global next
    global prod

    while next != "":
        next = products.readline()[:-1]
        y = next.split(sep=",")
        
        dic2 = {y[0]:y[-1]}

        prod.append(dic2)
    
    #print(prod)


def total_amounts_due():
    customer()
    product()

    for x in cus:
        print()

total_amounts_due()








