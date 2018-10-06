# key words: username, password, verify, email

"""
If the user's form submission is not valid, you should reject it and re-render the form
with some feedback to inform the user of what they did wrong. The following things should 
trigger an error:
 
"""
from flask import Flask, request

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
    




app.run()