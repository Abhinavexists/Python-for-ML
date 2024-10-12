from flask import Flask , render_template ,request
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''

# WSGl application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask.</H1></html>"

@app.route("/index")
def hello():
    return render_template('index.html', methods = ['GET'])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form' , methods = ['GET' , 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['email']
        message = request.form['message']
        return f"Hello {name} , email {mail} , my message is {message}!"
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug = True)