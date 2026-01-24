from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, IntegerField
from wtforms import validators

class UserForm(Form):
    matricula = IntegerField("Matricula", [
        validators.data_required(message="El campo es requerido")])
    nombre = StringField("Nombre", [
        validators.data_required(message="El campo es requerido")])
    apellido = StringField("Apellido", [
        validators.data_required(message="El campo es requerido")])
    correo = EmailField("Correo", [
        validators.email(message="Ingrese un correo valido")])