import requests
from flask import Flask, render_template, flash, request
from functions import *
app = Flask(__name__)

@app.route('/' , methods = ['GET' , 'POST'])
def home():
    return render_template('index.html')


@app.route('/search' , methods = ['GET' , 'POST'])
def search():
    header  = ""
    places = ""
    city = ""
    place_type = ""
    if(request.method == 'POST'):
        city = request.form['city']
        place_type = request.form.get('place_type')
        places = getPlaces(city , place_type)
        header = (place_type + " In " + city)
    return render_template(
    'search.html',
    header = header,
    places = places
    )

@app.route('/about' , methods = ['GET' , 'POST'])
def about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run(debug=True)
