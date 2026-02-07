from flask import Flask, render_template, request
import math
import forms
from flask_wtf.csrf import CSRFProtect

from forms import CinepolisForm

app = Flask(__name__)
app.secret_key = 'clave_secreta'
csrf = CSRFProtect()



@app.route('/')
def index():
    title = "IDGS804 - Intro Flask"
    listado = ['Jimena', 'Uriel', 'Paola', 'Gabriela']
    return render_template('index.html', title=title, listado=listado)


@app.route("/hola")
def func():
    return '¡Hola, Mundo -- Hola!'


@app.route("/operasBas", methods=['GET', 'POST'])
def operas1():
    res = None
    if request.method == 'POST':
        n1 = float(request.form.get('num1'))
        n2 = float(request.form.get('num2'))

        if request.form.get('operacion') == 'sumar':
            res = n1+n2
        if request.form.get('operacion') == 'restar':
            res = n1-n2
        if request.form.get('operacion') == 'multiplicar':
            res = n1*n2                                             
        if request.form.get('operacion') == 'dividir':
            res = n1/n2        


    return render_template('operasBas.html', res=res)

@app.route("/distancia", methods=['GET', 'POST'])
def distancia():
    resultado = None

    if request.method == 'POST':
        x1 = float(request.form.get('x1'))
        y1 = float(request.form.get('y1'))
        x2 = float(request.form.get('x2'))
        y2 = float(request.form.get('y2'))

        resultado = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return render_template("distancia.html", resultado=resultado)


@app.route("/resultado", methods=['GET', 'POST'])
def resul1():
    n1 = request.form.get('num1')
    n2 = request.form.get('num2')
    return f"<h1>La suma es: {float(n1)+float(n2)}</h1>"



@app.route("/saludo1")
def saludo1():
    return render_template("saludo1.html")


@app.route("/saludo2")
def saludo2():
    return render_template("saludo2.html")


@app.route("/user/<string:user>")
def user(user):
    return f'¡Hola, {user}!'


@app.route("/numero/<int:n>")
def numero(n):
    return f'<h1>Número: {n}</h1>'


@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f'<h1>Hola, {username}! tu id es: {id}</h1>'


@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f'<h1>La suma es: {n1+n2}</h1>'


@app.route("/default")
@app.route("/default/<string:param>")
def fuc2(param="Jimena"):
    return f'<h1>Hola, {param}!</h1>'


@app.route("/operas")
def operas():
    return '''
    <form>
    <label>Name:</label>
    <input type="text" required><br>
    <label>Apellido:</label>
    <input type="text" required><br>
    <input type="submit" value="Submit">
    </form>
    '''

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    mat = 0
    nom = ''
    ape = ''
    email = ''
    alumno_clas=forms.UserForm(request.form)
    if request.method == 'POST'and alumno_clas.validate():
        mat = alumno_clas.matricula.data
        nom  = alumno_clas.nombre.data
        ape = alumno_clas.apellido.data
        email = alumno_clas.correo.data
    return render_template("alumnos.html", form=alumno_clas, mat = mat, nom = nom, ape = ape, email = email)

@app.route('/cinepolis', methods=['GET', 'POST'])
def cinepolis():
    form = CinepolisForm()
    total = 0.0
    error = None
    PRECIO_BOLETA = 12000

    if request.method == 'POST':
        if form.validate(): 
            n_boletas = form.boletas.data
            subtotal = n_boletas * PRECIO_BOLETA
            
            if n_boletas > 5:
                subtotal *= 0.85
            elif 3 <= n_boletas <= 5:
                subtotal *= 0.90
            
            if form.tarjeta.data == 'S':
                subtotal *= 0.90
                
            total = round(subtotal, 2)
        else:
            if form.errors:
                field_errors = list(form.errors.values())[0]
                error = field_errors[0]

    return render_template('cinepolis.html', form=form, total=total, error=error)

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)