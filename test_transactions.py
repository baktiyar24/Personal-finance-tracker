from transactions import add_income, add_expense
from fastapi.testclient import TestClient
from api_practice.app import app

client = TestClient(app)
def test_income_increase_balance():
    assert add_income(500, 200) == 700

def test_income_negative_income():
    assert add_income(500, -300) == 500

def test_income_0_balance():
    assert add_income(0, 200) == 200

def test_expense_decrease_balance():
    assert add_expense(500, 200) == 300

def test_expense_negative_expense():
    assert add_expense(500, -100) == 500

def test_expense_balance_less_than_expense():
    assert add_expense(500, 700) == 500 

def test_expense_0_expense():
    assert add_expense(500, 0) == 500