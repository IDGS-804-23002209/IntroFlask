#importacion de flask
from flask import Flask
app= Flask(__name__)
#decorador o ruta
@app.route('/')
#funcion
def hello_world():
    frutas =["Manzana","Mango","Durazno","Fresa"]
    for i in frutas:
        return 'La fruta es: ' + i

if __name__ == '__main__':
    app.run()