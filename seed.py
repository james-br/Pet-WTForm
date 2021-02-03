from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

#Add pets

pupper = Pet(name='Pupper', species="dog", age="2", notes="Funny dog", available=True)
dancer = Pet(name='Dancer', species="dog", age="5", notes="Angry Dog", available=False)

db.session.add(pupper)
db.session.add(dancer)

db.session.commit()