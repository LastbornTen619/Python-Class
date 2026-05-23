# app/backend/logic.py

def calculate_tip(bill_amount, tip_percentage):
    try:
        bill = float(bill_amount)
        tip_percent = float(tip_percentage) / 100
        return bill * tip_percent
    except ValueError:
        return "Invalid Input"