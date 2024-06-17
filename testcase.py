# import  pytest
# def capital_case(x):
#
#     if not isinstance(x,str):
#         raise TypeError("please enter the string as am argument")
#     return x.lower()
# def test_capital_case():
#     assert capital_case('semaphore')=="semaphore"
# def test_raises_exception_on_non_string_arguments():
#     with pytest.raises(TypeError):
#         capital_case(9)

class InsufficientAmount(Exception):
    pass
class Wallet(object):
    def __init__(self,initial_amount=0):
        self.balance=initial_amount;
    def spend_cash(self,amount):
            if self.balance<amount:
                raise InsufficientAmount("not enough money in {}".format(amount))
            self.balance -=amount
    def add_cash(self,amount):
            self.balance += amount
