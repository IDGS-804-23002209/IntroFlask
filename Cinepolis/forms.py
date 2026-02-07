from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField
from wtforms.validators import DataRequired, NumberRange

class CinepolisForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    compradores = IntegerField('Cantidad Compradores', validators=[DataRequired(), NumberRange(min=1)])
    boletas = IntegerField('Cantidad De Boletas', validators=[DataRequired(), NumberRange(min=1)])
    tarjeta = RadioField('Tarjeta Cineco', choices=[('S', 'Si'), ('N', 'No')], default='N')