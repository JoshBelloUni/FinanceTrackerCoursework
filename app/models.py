from app import db

class Expenses(db.Model):
    Expense_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(500))
    cost = db.Column(db.Float)
    date = db.Column(db.Date)

class Incomes(db.Model):
    Income_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(500))
    cost = db.Column(db.Float)
    date = db.Column(db.Date)