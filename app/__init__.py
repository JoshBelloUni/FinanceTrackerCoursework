from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db)


#from app import views, models
#import datetime
#app.app_context().push()

#current_date = datetime.date.today()
#p = models.Incomes(type="Food", cost=10.76, date=current_date)
#db.session.add(p)

#models.Incomes.query.delete()


#db.session.commit() 


 