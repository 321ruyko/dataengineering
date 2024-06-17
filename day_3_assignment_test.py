import pytest
from day_3_assignment_shoppingcart import *
@pytest.fixture()
def shopping():
    return Shopping()
def test_menu(shopping):
    assert shopping.menu()=="1.View the Item \n2.Add to cart \n3.Update the list \n4.Remove from list\n5.Exit and print"
def test_viewproduct(shopping):
    assert shopping.view()==f' {len(stock)} items '
def test_addcart_noitemfound(shopping):
    assert shopping.addtocart('car')=='******No item Found****'
def test_addcart_itemalreadyexist(shopping):
    print("***To know the item already exist add Pen***")
    shopping.addtocart(input('Enter the item to add '))
    assert shopping.addtocart('Pen')=='******Item already exist in cart****'
def test_additemtocart_positivecheck(shopping):
    print("***To check  it accept only positive value use negative number or character***")
    assert shopping.addtocart('Pencil')=="***Only add positive number***"
def test_updateitem_exist(shopping):
    print('***enter an item except Pen to check whether the item exist in cart or not***')
    assert shopping.updatecart('Book')=='******No item Found****'
def test_updatecart_positivecheck(shopping):
    print("To check  updatecart cart accept only positive value use negative number")
    assert shopping.updatecart('Pen')=="***Only add positive number***"
def test_removecart_noitem(shopping):
    print("***enter an item except to check whether the item exist in cart or not***")
    assert shopping.removecart('car') == '******No item Found****'
def test_addtocart_success(shopping):
    print('***checking the item added sucessfully or not***')
    assert shopping.addtocart("Paper")=='Added to cart'
def test_updatecart_success(shopping):
    print('***checking the cart item updated or not***')
    assert shopping.updatecart("Paper")=='Quantity updated'
def test_viewcart_items(shopping):
    print("***checking cart items***")
    assert shopping.viewcart(cart,stock)==f'your cart contains {len(cart)} items'
def test_exitcart(shopping):
    print("***Exit or not***")
    assert shopping.exitcart()=='exited>>'


