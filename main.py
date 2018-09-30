# key words: username, password, verify, email

"""
If the user's form submission is not valid, you should reject it and re-render the form
with some feedback to inform the user of what they did wrong. The following things should 
trigger an error:

"""
from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def index():
    return render_template("signup.html")   

@app.route('/validate', methods=['POST', 'GET'])
def validate():
   
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    error = {}

    if not username:
        error = dict( username_error = "Username cannot be blank.")

    if not password:
        error = dict( password_error = "Password cannot be blank.")

    if not verify:
        error = dict( verify_error = "Verify password canno be blank")

    if " " in username:    
        error = dict( username_error = "Username cannot contain space") 

    if " " in password:    
        error = dict( password_error = "Password cannot contain space") 

    if len(username) < 3 or len(username) > 20:
        error = dict( username_error = "Username must be between 3 and 20 characters long") 

    if len(password) < 3 or len(password) > 20:
        error = dict( password_error = "Password must be between 3 and 20 characters long") 

    if password != verify:
        error = dict( password_error = "Password does not match")    

    if email:
        if " " in email:    
            error = dict( email_error = "Email cannot contain space") 

        if len(email) < 3 or len(email) > 20:
            error = dict( email_error = "Email must be between 3 and 20 characters long")

        if email.count("@") != 1:
            error = dict( email_error = "Email must contain a single @ character")

        if email.count(".") != 1:
            error = dict( email_error = "Email must contain a single . character")    

    if error:
        return render_template("signup.html", username = username, email = email, **error)
    else:
        return render_template("home.html", username = username)

app.run()