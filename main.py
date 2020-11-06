import requests
from flask import Flask, render_template, flash, request
app = Flask(__name__)

@app.route('/search' , methods = ['GET' , 'POST'])
def search():
    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True)
