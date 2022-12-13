from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def hello_worl():

   return render_template("index.html") 
