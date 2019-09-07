import os
from config import db
from models import Person

# Data to initialize database with
PEOPLE = [
    {'fname': 'Doug', 'lname': 'Farrell'},
    {'fname': 'Kent', 'lname': 'Brockman'},
    {'fname': 'Bunny','lname': 'Easter'}
]

# Delete database file if it  already exiata currently
if os.path.exists('people.db'):
    os.remove('people.db')

db.create_all()

for person in PEOPLE:
    p = Person(lname=person['lname'],fname=person['fname'])
    db.session.add(p)

db.session.commit()