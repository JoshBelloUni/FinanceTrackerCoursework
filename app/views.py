from flask import render_template, redirect, url_for, request, flash
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

# import for goal
from .forms import GoalsForm
from .models import Goal

# parent html file to format some pages
@app.route('/tmp')
def some_route():
    return render_template('non_home.html')

# home page
@app.route('/', methods=['GET', 'POST'])
def home():
    # creating the objects by querying the databases
    expenses = Expenses.query.all()
    incomes = Incomes.query.all()
    goal = Goal.query.first()

    total_expenses = 0
    total_incomes = 0
    progress = 0
    goalName = ""
    goalAmount = 0
    goal_id = 0

    for expense in expenses:
        total_expenses += expense.cost

    for income in incomes:
        total_incomes += income.cost

    if goal != None:
        goalName = goal.goal
        goalAmount = goal.amount
        goal_id = goal.Goal_id
        progress = round(((total_incomes - total_expenses) / goalAmount) * 100, 2)

    return render_template('home.html', 
                           title='Home', 
                           home=home, 
                           progress=progress,
                           total_expenses=total_expenses,
                           total_incomes=total_incomes,
                           goalName=goalName,
                           goalAmount=goalAmount,
                           goal_id=goal_id  
                           )

# --------------- EXPENSES ------------------ #
# expenses page
@app.route('/expenses')
def expenses():
    # suery the Expenses table and pass the data to the template
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
    error_message = None

    if form.validate_on_submit():
        type = form.type.data
        cost = form.cost.data
        current_date = datetime.date.today()

        # Create a new expense object and add it to the database
        expense = Expenses(type=type, cost=cost, date=current_date)
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('expenses'))
    
    
    
    return render_template('add_expense.html', 
                           form=form,
                           error_message=error_message)

@app.route('/expenses/edit_expense/<int:expense_id>', methods=['GET', 'POST'])
def edit_expense(expense_id):
    # use the id to query the id
    expense = Expenses.query.get(expense_id)
    
    # create form to update
    form = ExpensesForm(obj=expense)

    if request.method == 'POST' and form.validate():
        # this is the old data that we may want to change
        form.populate_obj(expense)

        # updating the old data
        if form.validate_on_submit():
            type = form.type.data
            cost = form.cost.data
            current_date = datetime.date.today()

            # create the object
            expense = Expenses(type=type, cost=cost, date=current_date)
            db.session.commit()

            return redirect(url_for('expenses'))

    return render_template('edit_expense.html', form=form, expense=expense)

@app.route('/expenses/delete_expense/<int:expense_id>')
def delete_expense(expense_id):

    # create the object
    expense = Expenses.query.get(expense_id)
    
    # and delete it straight after :)
    db.session.delete(expense)
    db.session.commit()

    # redirect to the same page, basically refreshing the page
    return redirect(url_for('expenses'))

# --------------- INCOME --------------------- #

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

    return render_template('add_income.html', 
                           form=form)

@app.route('/incomes/edit_income/<int:income_id>', methods=['GET', 'POST'])
def edit_income(income_id):

    income = Incomes.query.get(income_id)
    
    form = IncomesForm(obj=income)

    if request.method == 'POST' and form.validate():
        form.populate_obj(income)

        db.session.commit()

        return redirect(url_for('incomes'))

    return render_template('edit_income.html', 
                           form=form, 
                           income=income)

@app.route('/incomes/delete_income/<int:income_id>')
def delete_income(income_id):

    income = Incomes.query.get(income_id)
    
    db.session.delete(income)
    db.session.commit()

    return redirect(url_for('incomes'))

# ------------- GOAL ------------- #

@app.route('/add_goal', methods=['GET', 'POST'])
def add_goal():

    form = GoalsForm()
    goal_object = Goal.query.all()

    amount = form.amount.data
    goal = form.goal.data

    if form.validate_on_submit():

        if goal_object is None:
            goal_object = Goal(goal=goal, amount=amount)
            db.session.add(goal_object)
            db.session.commit()
            
        else:
            for goal_obj in goal_object:
                db.session.delete(goal_obj)
            
            goal_object = Goal(goal=goal, amount=amount)
            db.session.add(goal_object)
            db.session.commit()

        return redirect(url_for('home'))   

    return render_template('add_goal.html',
                           form=form)

@app.route('/remove_goal/<int:goal_id>')
def remove_goal(goal_id):

    goal = Goal.query.get(goal_id)

    db.session.delete(goal)
    db.session.commit()
    
    return redirect(url_for('home'))