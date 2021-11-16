from flask import Flask, render_template, request

app = Flask(__name__) 
app.config.from_object(__name__) 

@app.route('/')
def hello():
  return render_template("index.html") 

@app.route('/welcome', methods=['POST'])
def welcome():
  newName = request.form['myName'] + " is awesome"
  return render_template("welcome.html", myName=newName)
