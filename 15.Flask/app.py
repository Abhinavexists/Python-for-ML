from flask import Flask
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''

# WSGl application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to flask app"

@app.route("/index")
def hello():
    return "Welcome to index page"

if __name__ == "__main__":
    app.run(debug = True)