from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods =['POST'])
def user_result():
    print "Got Post Info"
    name = request.form['your_name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    print name, location, language, comment
    return render_template("result.html", name=request.form['your_name'], location=request.form['location'], language = request.form['language'], comment = request.form['comment'])

    return redirect("/")

app.run(debug=True)