from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
 for i in range(1, n + 1):
    # Espaces avant les nombres
    for j in range(n - i):
        print(' ', end='')
    
    # Nombres croissants
    for j in range(1, i + 1):
        print(j, end='')
    
    # Nombres décroissants
    for j in range(i - 1, 0, -1):

    return etoiles

if __name__ == "__main__":
  app.run(debug=True) 
