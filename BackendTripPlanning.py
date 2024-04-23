from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db'  
db = SQLAlchemy(app)

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    purpose = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_trip', methods=['POST'])
def save_trip():
    destination = request.form['destination']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    purpose = request.form['purpose']

    new_trip = Trip(destination=destination, start_date=start_date, end_date=end_date, purpose=purpose)
    db.session.add(new_trip)
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    db.create_all() 
    app.run(debug=True)
