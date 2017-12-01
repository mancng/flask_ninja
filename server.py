from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def single(color):
    if color == "purple":
        img_str = "img/donatello.jpg"
    elif color == "blue":
        img_str = "img/leonardo.jpg"
    elif color == "orange":
        img_str = "img/michelangelo.jpg"
    elif color == "red":
        img_str = "img/raphael.jpg"
    else:
        img_str = "img/notapril.jpg"
    return render_template('single.html', img_str = img_str)

app.run(debug=True)