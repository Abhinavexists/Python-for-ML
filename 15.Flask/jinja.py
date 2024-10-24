# Building url dynamically
# variable rule
# Jinja 2 Template Engine

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

@app.route('/submit' , methods = ['GET' , 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['email']
        message = request.form['message']
        return f"Hello {name} , email {mail} , my message is {message}!"
    return render_template('form.html')

#variable rule
@app.route('/success/<int:score>') #<> inside this is the parameter
def success(score):
    # return "The score is " +  str(score) # type casting for parameter restriction
    res = ""
    if score >= 50:
        res = "Passed"
    else:
        res = "Failed"

    return render_template('results.html',results = res)

@app.route('/successres/<int:score>') #<> inside this is the parameter
def successres(score):
    # return "The score is " +  str(score) # type casting for parameter restriction
    res = ""
    if score >= 50:
        res = "Passed"
    else:
        res = "Failed"

    exp={'score':score , "res":res}

    return render_template('result1.html',results = exp)

#if condition
@app.route('/successif/<int:score>') 
def successif(score):
     return render_template('result1.html' , results = score)

if __name__ == "__main__":
    app.run(debug = True)

'''
{{ }} expresssion to print output in html
{%...%} conditions , for loops
{#...#} this is for comments
'''