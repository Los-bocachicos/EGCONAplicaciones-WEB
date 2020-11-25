from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

tiposList = [{"id": 1, "nombre": "Back"},{"id": 2, "nombre": "Front"}]
estadosList = [{"id": 1, "nombre": "En ejecución"},{"id": 2, "nombre": "Detenida"},{"id": 3, "nombre": "Con fallos"}]
servidorList = [{"id": 1, "nombre": "US-east"},{"id": 1, "nombre": "US-west"},{"id": 3, "nombre": "Europe-east"},{"id": 4, "nombre": "Europe-west"}]

@app.route('/listarAplicaciones', methods=['GET'])
def listarAplicaciones():
  aplicacionesList = requests.get('https://egconaplicaciones-api-rfi2t332aq-uc.a.run.app/aplicaciones').json()
  return render_template('listar.html', aplicaciones=aplicacionesList)

@app.route('/crearAplicacion', methods=['GET'])
def crearAplicacion():
  return render_template('crear.html', tipos=tiposList,estados=estadosList,servidores=servidorList)

@app.route('/guardarAplicacion', methods=['POST'])
def guardarAplicacion():
  aplicacion = dict(request.values)
  print(aplicacion)
  requests.post('https://egconaplicaciones-api-rfi2t332aq-uc.a.run.app/aplicaciones', json=aplicacion)
  return listarAplicaciones()

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
