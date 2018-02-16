from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def portfolio():
    return "Welcome to my portfolio! My name is Ting"

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)