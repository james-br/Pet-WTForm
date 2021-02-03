from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, Email, Length, URL, NumberRange
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)



class Pet(db.Model):
    """ Pet Model """
    __tablename__ = "pet"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default="/static/pet.jpg")
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Creates a default image or returns new image"""
        return self.photo_url or DEFAULT_IMAGE
    
class PetForm(FlaskForm):

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo Url", validators=[Optional(), URL()])
    age = FloatField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[ Length(min=10)])
    available = BooleanField("Available?")


class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")
