from flask import Flask, request, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, PetForm, EditPetForm

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secretchicken"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.errorhandler(404)
def page_not_found(e):
    """Show 404 NOT FOUND page."""
    return render_template('404.html'), 404


@app.route('/')
def home_page():
    pets = Pet.query.all()
    return render_template('list.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    form= PetForm()
    if form.validate_on_submit():
        new_pet = Pet(name=form.name.data,
                        species=form.species.data,
                        photo_url=form.photo_url.data,
                        age=form.age.data,
                        notes=form.notes.data,
                        available=form.available.data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add.html', form=form)

@app.route('/<int:id>', methods=["GET", "POST"])
def display_edit(id):
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url=form.photo_url.data
        pet.notes=form.notes.data
        pet.available=form.available.data
        db.session.commit()
        flash(f"Pet {id} was updated!")
        return redirect('/')
    else:
        return render_template("display_edit.html", form=form, pet=pet)