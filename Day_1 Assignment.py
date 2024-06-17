import csv
stock={'Pen':10,'Pencil':5,'Book':25,'Eraser':4,'Sharpner':3,'Paper':1}
cart={}
def menu():
    print("1.View the Item \n2.Add to cart \n3.Update the list \n4.Remove from list\n5.Exit and print")
def view(stock):
    for i in stock:
        print(i ,': ','Rs.',stock[i])
def viewcart(stock,mainstock):
    for i in stock:
        print(i ,stock[i],'Qty','Rs',stock[i]*mainstock[i])
def addtocart():
    itemname = input('Enter the item  to add ').capitalize()
    if (itemname not in stock.keys()):
        print('******No item Found****')
    elif (itemname in cart.keys()):
        print('******Item already exist in cart****')
        viewcart(cart, stock)
    else:
        try:
            val = int(input('Enter the quantity'))
            if (val > 0):
                cart[itemname] = val
            else:
                print("***Only add positivenumber***")
        except:
            print("***Only add positivenumber***")
    print("****press any key from 1 to 4 or press 5 to exit****")
def updatecart():
    itemname = input("Enter the item").capitalize()
    if (itemname not in stock.keys()):
        print('******No item Found****')
    elif (itemname in cart.keys()):
        try:
            val=int(input('Enter the quantity'))
            if(val>0):
                cart[itemname] = val
            else:
                print("***Only add positivenumber***")

        except:
            print("***Only add positivenumber***")
    else:
        print('******No item Found****')

    print("****press any key from 1 to 4 or press 5 to exit****")
print('Welcome to My Store')
def removecart():
    itemname = input("Enter the item to remove").capitalize()
    if (itemname not in stock.keys()):
        print('******No item Found****')
    else:
        cart.pop(itemname)
        viewcart(cart, stock)
    print("****press any key from 1 to 4 or press 5 to exit****")
def exitcart():
    total = 0
    itemnumber = 0
    with open('bill.csv', 'w', newline='') as csvfile:
        bill = csv.writer(csvfile, delimiter=' ')
        for i in cart:
            itemnumber += 1
            bill.writerow([itemnumber, i, cart[i], "Rs", stock[i], cart[i] * stock[i]])

            print(itemnumber, ".", i, "Qty", cart[i], 'Rs', cart[i] * stock[i])
            total += cart[i] * stock[i]
        bill.writerow(["Total Price", "", "", "", total])
    print("Total Price", "Rs.", total)

menu()
c=int(input("Enter the key"))
if c not in [1,2,3,4]:
    print('Enter the correct key')
while(c!=5):
    if(c==1):
        view(stock)
        print("****press any key from 1 to 4 or press 5 to exit****")
    elif(c==2):
        addtocart()
    elif(c==3):
        updatecart()
    elif (c == 4):
        removecart()
    c=int(input(""))
if(c==5):
    exitcart()