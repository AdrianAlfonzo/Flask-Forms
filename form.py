from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields.html5 import EmailField
from wtforms.widgets import TextArea

class Datos(FlaskForm):
    nombre=StringField("Nombre", validators=[
        DataRequired(),
        Length(max=12, min=3),
    ])
    apellido=StringField("Apellido", validators=[
        DataRequired(),
        Length(max=12, min=3),
    ])
    correo=EmailField("Correo", validators=[
        DataRequired(),
        Email(),
    ])
    tel=StringField("Teléfono", validators=[
        DataRequired(),
        Length(max=12, min=3)
    ])
    direccion=StringField("Dirección", widget=TextArea(), validators=[
        Length(max=100)        
    ])

    submit = SubmitField("Enviar info")