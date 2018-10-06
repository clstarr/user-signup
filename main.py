# key words: username, password, verify, email

"""
If the user's form submission is not valid, you should reject it and re-render the form
with some feedback to inform the user of what they did wrong. The following things should 
trigger an error:

The user leaves any of the following fields empty: username, password, verify password.

The user's username or password is not valid -- for example, it contains a space character or it consists of 
less than 3 characters or more than 20 characters (e.g., a username or password of "me" would be invalid).

The user's password and password-confirmation do not match.

The user provides an email, but it's not a valid email. Note: the email field may be left empty, but if 
there is content in it, then it must be validated. 

The criteria for a valid email address in this assignment are 
that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.
 
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
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if not username:
        username_error = "Username cannot be blank."

    if " " in username:
        username_error = "Username cannot contain spaces."

    if len(username) < 3 or len(username) > 20:
        username_error = "Username cannot be less than 3 or greater than 20 characters."

    if not password:
        password_error = "Password cannot be blank."

    if " " in password:
        password_error = "Password cannot contain spaces."

    if len(password) < 3 or len(password) > 20:
        password_error = "Password cannot be less than 3 or greater than 20 characters."


    if not verify:
        verify_error = "Verify password cannot be blank."

    if len(verify) < 3 or len(verify) > 20:
        verify_error = "Verify password cannot be less than 3 or greater than 20 characters."    

    if verify != password:
        verify_error = "Verify password does not match."

    if email:
        if "@" not in email or '.'not in email: 
            email_error = "Email must contain an '@' symbol and '.'"

        if " " in email:
            email_error = "Email cannot contain spaces."

        if len(email) < 3 or len(email) > 20:
            email_error = "Email cannot be less than 3 or greater than 20 characters."

    if username_error or password_error or email_error or verify_error:
        return render_template("signup.html", username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=username, email=email)

    return render_template("home.html", username=username)


app.run()
