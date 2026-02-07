from flask import Flask, render_template, request
from forms import CinepolisForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cinepolis_secret'

@app.route('/cinepolis', methods=['GET', 'POST'])
def cinepolis():
    form = CinepolisForm()
    total = 0
    error = None
    PRECIO_BOLETA = 12000 # [cite: 22]

    if request.method == 'POST' and form.validate():
        n_compradores = form.compradores.data
        n_boletas = form.boletas.data
        max_permitido = n_compradores * 7 # [cite: 22]

        if n_boletas > max_permitido:
            error = f"No se pueden comprar más de 7 boletas por persona (Máx: {max_permitido})"
        else:
            subtotal = n_boletas * PRECIO_BOLETA
            
            # Descuento por cantidad [cite: 23, 25]
            if n_boletas > 5:
                subtotal *= 0.85
            elif 3 <= n_boletas <= 5:
                subtotal *= 0.90
            
            # Descuento Tarjeta Cineco [cite: 27]
            if form.tarjeta.data == 'S':
                subtotal *= 0.90
                
            total = round(subtotal, 2)

    return render_template('cinepolis.html', form=form, total=total, error=error)

if __name__ == '__main__':
    app.run(debug=True)