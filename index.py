from flask import Flask, render_template, request
from form import Datos

app = Flask(__name__)
app.secret_key='123456'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/formulario', methods=['POST', 'GET'])
def formulariohtml():
    if request.method == 'POST':
        return "nombre={request.form['nombre']} | email={request.form['correo']} | tel={request.form['tel']} "
    return render_template('formulario01.html')

@app.route('/formulario2', methods=['POST', 'GET'])
def formularioobjeto():
    form = Datos()
    if request.method == 'POST': 
        return "nombre={request.form['nombre']} | apellido={request.form['apellido']} | correo={request.form['correo']} | tel={request.form['tel']} | direccion={request.form['direccion']}"
    return render_template('formulario2.html', form=form)

if __name__=='__main__':
    app.run(debug=True)