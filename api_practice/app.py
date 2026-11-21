from fastapi import FastAPI
from pydantic import BaseModel, Field
from storage import load_transactions, save_transactions
from transactions import calculate_balance, add_income, add_transactions

app = FastAPI()

class Income(BaseModel):
    amount : int = Field(gt=0)

@app.get("/")
def home():
    return {"message": "Welcome to Personal Finance Tracker!"}

@app.get("/balance")
def get_balance():
    transactions = load_transactions()
    balance = calculate_balance(transactions)
    return {"balance": balance}

@app.get("/transactions")
def get_transactions():
    transactions = load_transactions()
    return {"transactions": transactions}

@app.post("/income")
def create_income(income: Income):
    transactions = load_transactions()
    balance = calculate_balance(transactions)
    balance = add_income(balance, income.amount)
    add_transactions(transactions, "income", income.amount)
    save_transactions(transactions)
    return {"balance": balance}
