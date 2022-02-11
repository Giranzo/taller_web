from flask import Flask, escape, request, render_template, url_for     #importar libreria

app = Flask(__name__)       #Inicializar la app con el nombre

@app.route('/')
def hola():
    return 'Hi Penguins'    #Retorna Hi Penguins

@app.route('/coach')
def hola_coaches():
    nombre ='mi rrrrrreeeeeey, Liiiiiiider!!'
    devolver =  request.args.get('nombre', nombre)
    return f'Que tal, {escape(devolver)}'

@app.route('/inicio')   #creamos la ruta inicio
def inicio():
    return render_template('Inicio.html')

@app.route('/contacto')
def contacto():
    return render_template('Contacto.html')

app.run(debug=True)

