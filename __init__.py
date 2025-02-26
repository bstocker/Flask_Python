from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exercices_base1')
def exercices_base1():
    return render_template('exercices_base1.html')

@app.route('/exercices_base2')
def exercices_base2():
    return render_template('exercices_base2.html')

@app.route('/exercices_base3')
def exercices_base3():
    return render_template('exercices_base3.html')

if __name__ == '__main__':
    app.run(debug=True)
