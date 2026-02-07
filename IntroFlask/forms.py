from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField
from wtforms.validators import DataRequired, NumberRange

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField
from wtforms.validators import DataRequired, NumberRange, ValidationError

class CinepolisForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message="El nombre es obligatorio")])
    compradores = IntegerField('Cantidad Compradores', validators=[DataRequired(message="Este campo es obligatorio"), NumberRange(min=1)])
    boletas = IntegerField('Cantidad De Boletas', validators=[DataRequired(message="Este campo es obligatorio"), NumberRange(min=1)])
    tarjeta = RadioField('Tarjeta Cineco', choices=[('S', 'Si'), ('N', 'No')], default='N')

    def validate_boletas(self, field):
        if self.compradores.data:
            max_permitido = self.compradores.data * 7
            if field.data > max_permitido:
                raise ValidationError(f"No se pueden comprar más de 7 boletas por persona. Máximo: {max_permitido}")