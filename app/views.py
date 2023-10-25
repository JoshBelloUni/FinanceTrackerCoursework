from flask import render_template, redirect, url_for
from app import app
from app import app, db
import datetime

# import for expenses
from .forms import ExpensesForm
from .models import Expenses
from app.models import Expenses

#import for incomes
from .forms import IncomesForm
from .models import Incomes
from app.models import Incomes

# home page
@app.route('/', methods=['GET', 'POST'])
def home():
    home={'description':'WORK IN PROGRESS. Finances!!! '}
    return render_template('home.html', title='Home', home=home)

# expenses page
@app.route('/expenses')
def expenses():
    # Query the Expenses table and pass the data to the template
    expenses = Expenses.query.all()

    return render_template('expenses.html',
                           title='Expenses',
                           expenses=expenses,
                           button_url=url_for('add_expense'))

# sub page to add an expense
# will be accessed by a button on the expenses page
# then will be redirected back to the expenses page
@app.route('/expenses/add_expense', methods=['GET', 'POST'])
def add_expense():
    form = ExpensesForm()

    if form.validate_on_submit():
        type = form.type.data
        cost = form.cost.data
        current_date = datetime.date.today()

        # Create a new expense object and add it to the database
        expense = Expenses(type=type, cost=cost, date=current_date)
        db.session.add(expense)
        db.session.commit()

        return redirect(url_for('expenses'))

    return render_template('add_expense.html', form=form)

# works the same as the expenses page
@app.route('/incomes')
def incomes():
    # Query the Expenses table and pass the data to the template
    incomes = Incomes.query.all()

    return render_template('incomes.html',
                           title='Incomes',
                           incomes=incomes,
                           button_url=url_for('add_income'))
                
@app.route('/incomes/add_income', methods=['GET', 'POST'])
def add_income():
    form = IncomesForm()

    if form.validate_on_submit():
        type = form.type.data
        cost = form.cost.data
        current_date = datetime.date.today()

        # Create a new income object and add it to the database
        income = Incomes(type=type, cost=cost, date=current_date)
        db.session.add(income)
        db.session.commit()

        return redirect(url_for('incomes'))

    return render_template('add_income.html', form=form)