from app import app
from flask import render_template 
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
  user = { 'username' : 'guest' } 
  posts = [
    {

      'author' : { 'username' : 'guest2' },
      'body' : "What beautiful weather we are having" 
    },

    {

      'author' : { 'username' : 'guest3' },
      'body' : "I know right" 
    }
  ]
  return render_template('index.html' ,title="Home", user=user, posts=posts) 



@app.route('/login')
def login():
  form= LoginForm()
  return render_template("login.html", title= "Sign In", form=form)


