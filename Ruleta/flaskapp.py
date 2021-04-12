# -*- coding: utf-8 -*-
"""
@author: sebas
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
import random
app = Flask(__name__)
app.secret_key = "cairocoders-ednalan-06300131"
#aqui configuramos la conexion a nuestra base de datos
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin**A@localhost:5432/Crud"      
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://waufeklidhhzoy:6ff59a4260175037ec69d78df310439b86d2ee5392b982e89297fac9793cca57@ec2-34-233-0-64.compute-1.amazonaws.com:5432/dbmtq7ks27bpjv"       
  
                              
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
db = SQLAlchemy(app)
sql = '''select pid from pg_stat_activity where usename = 'waufeklidhhzoy' '''
result = db.engine.execute(sql)
for row in result:
    valor = row['pid']
    db.engine.execute( f'select pg_terminate_backend({valor})' )
  
#creamos nuestro modelo de usuarios para hacer las operaciones CRUD 
class users(db.Model):
    cedula = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    monto_disponible = db.Column(db.Integer)
    tipo_apuesta = db.Column(db.Integer)
    valor_apuesta = db.Column(db.Integer)
   

    def __init__(self, cedula, nombre, monto_disponible,tipo_apuesta,valor_apuesta):
        self.cedula = cedula
        self.nombre = nombre
        self.monto_disponible = monto_disponible
        self.tipo_apuesta = tipo_apuesta
        self.valor_apuesta  = valor_apuesta
    
def spins():
    global slots
    slots = { '0': 'green', '1': 'red', '2': 'black',
             '3': 'red', '4': 'black', '5': 'red', '6': 'black', '7': 'red',
             '8': 'black', '9': 'red', '10': 'black', '11': 'red',
             '12': 'black', '13': 'red', '14': 'black', '15': 'red',
             '16': 'black', '17': 'red', '18': 'black', '19': 'red',
             '20': 'black', '21': 'red', '22': 'black', '23': 'red',
             '24': 'black', '25': 'red', '26': 'black', '27': 'red',
             '28': 'black', '29': 'red', '30': 'black', '31': 'red',
             '32': 'black', '33': 'red', '34': 'black', '35': 'red',
             '36': 'black'}
    result = random.choice(list(slots.keys()))
    return result  
#aqui ademas de cargar el inicio se valida que no existan problemas con el servidor ya que lanzara un error al usuario
#de lo contrario si todo va bien iniciara nuestra interfaz de inicio para la gestion de usuarios
@app.route('/')
def Index():
    try:
        all_data = users.query.all()
        return render_template("index.html", employees = all_data)
    except exc.OperationalError :
        message ="Lo sentimos El servidor no se encuentra disponible"
        return redirect(url_for("show_error_post",message=message))

#aqui planteamos una url especificamente para renderizar errores
@app.route('/errorServer/<message>')
def show_error_post(message = None):
    return render_template("error.html", message = message)
#metodo de insercion a la base de datos
@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        try:
            cedula = request.form['cedula']
            nombre = request.form['nombre']
            monto_disponible = request.form['monto_disponible']
            monto_disponible = int(monto_disponible) + 15000
            tipo_apuesta = request.form['tipo_apuesta']
            valor_apuesta = request.form['valor_apuesta']
            my_data = users(cedula,nombre, str(monto_disponible),tipo_apuesta,valor_apuesta)
            db.session.add(my_data)
            db.session.commit()
            flash("Usuario registrado correctamente")    
            return redirect(url_for('Index'))
        except exc.IntegrityError:
            message ="Lo sentimos este usuario ya esta registrado"
            flash(message)
            return redirect(url_for('Index'))
        except exc.OperationalError :
            message ="Lo sentimos El servidor no se encuentra disponible"
            return redirect(url_for('show_error_post',message=message))

#metodo de actualizacion de datos 
@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = users.query.get(request.form.get('cedula'))
        my_data.cedula = request.form['cedula']
        my_data.nombre = request.form['nombre']
        my_data.monto_disponible = request.form['monto_disponible']
        my_data.tipo_apuesta = request.form['tipo_apuesta']
        my_data.valor_apuesta = request.form['valor_apuesta']
        db.session.commit()
        flash("Cliente actualizado correctamente")
        return redirect(url_for('Index'))
@app.route('/RouletteGame/',methods = ["GET", "POST"])
def RouletteGame():
    resultados_ronda = []
    resultado = int(spins())
    tipo_numero = ""
    if resultado %2 !=0:
        color = "ROJO"
        tipo_numero += "IMPAR"   
    if resultado %2 ==0:
        color = "NEGRO"
        tipo_numero += "PAR"
    all_data = users.query.all()
    jugadores = [x for x in all_data if int(x.monto_disponible) >0]
    for jugador in jugadores:
        print(int(jugador.cedula))
        if int(jugador.tipo_apuesta) %2 ==0:
            if resultado %  2 ==0:
                mensaje = (f"EL JUGADOR {jugador.nombre} HA GANADO {jugador.valor_apuesta}")
                jugador_actual = users.query.filter_by(cedula=int(jugador.cedula)).first()
                jugador_actual.monto_disponible = int(jugador_actual.monto_disponible+ jugador.valor_apuesta)
                db.session.commit()
            else:
                mensaje =(f"EL JUGADOR {jugador.nombre} HA PERDIDO {jugador.valor_apuesta}")
                jugador_actual = users.query.filter_by(cedula=int(jugador.cedula)).first()
                jugador_actual.monto_disponible = int(jugador_actual.monto_disponible - jugador.valor_apuesta)
                db.session.commit()
                
              
            resultados_ronda.append(mensaje)    
        if int(jugador.tipo_apuesta ) %2 !=0:
            if resultado % 2 !=0:
                mensaje = (f"EL JUGADOR {jugador.nombre} HA GANADO {jugador.valor_apuesta}" )
                jugador_actual = users.query.filter_by(cedula=int(jugador.cedula)).first()
                jugador_actual.monto_disponible = int(jugador_actual.monto_disponible+ jugador.valor_apuesta)
                db.session.commit()
            else:
                mensaje = (f"EL JUGADOR {jugador.nombre} HA PERDIDO {jugador.valor_apuesta}")
                jugador_actual = users.query.filter_by(cedula=int(jugador.cedula)).first()
                jugador_actual.monto_disponible = int(jugador_actual.monto_disponible - jugador.valor_apuesta)
                db.session.commit()
            resultados_ronda.append(mensaje)
        if int(jugador.monto_disponible <= 1000):
              jugador_actual = users.query.filter_by(cedula=int(jugador.cedula)).first()
              jugador_actual.valor_apuesta = jugador.monto_disponible
              db.session.commit()
            
    resultados_ronda.append(f"EL RESULTADO DE LA RULETA HA SIDO {resultado} {color} {tipo_numero}")   
    return render_template("ruleta.html",resultados_ronda=resultados_ronda)
    
#metodo para borrar datos
@app.route('/delete/<cedula>/', methods = ['GET', 'POST'])
def delete(cedula):
    my_data = users.query.get(cedula)
    db.session.delete(my_data)
    db.session.commit()
    flash("Cliente borrado correctamente")
    return redirect(url_for('Index'))
  
if __name__ == "__main__":
    app.run()
