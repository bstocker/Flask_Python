from flask import Flask
from flask import render_template

app = Flask(__name__)

if __name__ == '__main__':
  app.run(debug = True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exercices_base1')
def exercices_base1():
    return render_template('exercices_base1.html')