import pytest
from testcase import InsufficientAmount,Wallet
@pytest.fixture
def empty_wallet():
    return Wallet()
@pytest.fixture
def wallet():
    return Wallet(20)
def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance==0
def test_setting_test_default_initial_amount(wallet):
    assert wallet.balance==20
def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert  wallet.balance==100
def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance==10
def test_wallet_cash_raises_exception_of_insufficient_balance(empty_wallet):
     with pytest.raises(InsufficientAmount):
         empty_wallet.spend_cash(100)```````````````````````````````````````````````````````````````````````````````````````````````````

