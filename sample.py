import csv
stock = {'Pen': 10, 'Pencil': 5, 'Book': 25, 'Eraser': 4, 'Sharpner': 3, 'Paper': 1}
cart = {}
class Shopping():
    def __init__(self):
        pass
    def menu(self):
        return("1.View the Item \n2.Add to cart \n3.Update the list \n4.Remove from list\n5.Exit and print")

    def view(self):
        for i in stock:
            print(i, ': ', 'Rs.', stock[i])
        return f' {len(stock)} items '


    def viewcart(self,stock,mainstock):
        for i in stock:
            print(i, stock[i], 'Qty', 'Rs', stock[i] * mainstock[i])
        return f'your cart contains {len(stock)} items'

    def addtocart(self,it,val):
        itemname = it
        if (itemname not in stock.keys()):
            return ('******No item Found****')
        elif (itemname in cart.keys()):
            return('******Item already exist in cart****')

        else:
            try:

                if (val > 0):
                    cart[itemname] = val
                    return "Added to cart"
                else:
                    return("***Only add positive number***")
            except:
                return("***Only add positive number***")
        print("****press any key from 1 to 4 or press 5 to exit****")

    def updatecart(self,it,val):
        itemname = it
        if (itemname not in stock.keys()):
            return('******No item Found****')
        elif (itemname in cart.keys()):
            try:

                if (val > 0):
                    cart[itemname] = val
                    return 'Quantity updated'
                else:
                    return("***Only add positive number***")

            except:
                return("***Only add positivenumber***")
        else:
            return('******No item Found****')

        print("****press any key from 1 to 4 or press 5 to exit****")

    print('Welcome to My Store')

    def removecart(self,it):
        itemname = it
        if (itemname not in stock.keys()):
            return('******No item Found****')
        else:
            cart.pop(itemname)
            self.viewcart(cart, stock)
        return("****press any key from 1 to 4 or press 5 to exit****")

    def exitcart(self):
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
        return('exited>>')


s=Shopping()
print(s.menu())
c = int(input("Enter the key"))
if c not in [1, 2, 3, 4]:
    print('Enter the correct key')
while (c != 5):
    if (c == 1):
        s.view()
        print("****press any key from 1 to 4 or press 5 to exit****")
    elif (c == 2):
        item = input("Enter the item").capitalize()
        try:
            qty = int(input("Enter the quantity"))
            s.addtocart(item,qty)
            s.viewcart(cart, stock)
        except:
            print("only positive numbers")

    elif (c == 3):
        item=input("Enter the item").capitalize()
        try:
            qty=int(input("Enter the quantity"))
            print(s.updatecart(item, qty))
            s.viewcart(cart, stock)
        except:
            print("only positive numbers")

        print(s.updatecart(item,qty))
        s.viewcart(cart, stock)
    elif (c == 4):
        print(s.removecart(input("Enter the item to remove").capitalize()))
    c = int(input(""))
if (c == 5):
    s.exitcart()
