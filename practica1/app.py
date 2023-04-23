from flask import jsonify, Flask, request
from flask_cors import CORS
from mensajes import Mensajes
import Pila


app = Flask(__name__)
CORS(app)

miPila = Pila.Pila()

@app.route('/getInfo', methods=['GET'])
def getINFO():
    #misMensajes = Mensajes()
    return jsonify({"resp": "OK info"})

@app.route('/postentrada', methods=['POST'])
def postEntrada():
    return jsonify({"resp": {"perfilesNuevos":"se han creado 3 perfiles nuevos", "perfilesExistentes":"se han actualizado 2 perfiles nuevos", "descartados":"se han descartadas 20 palabras"}})


@app.route('/postnuevosmensajes', methods=['POST'])
def postNuevosMensajes():
    misMensajes = Mensajes()
    return misMensajes.gestionarPeticion(request)


@app.route('/postAgregar', methods=['POST'])     
def addPila():
    if request.method == 'POST':
        valorLeido = request.form['valor']
        miPila.insertar(valorLeido)
        return jsonify({"msg": f'SE AGREGO {valorLeido}'})

@app.route('/postGenerarImagen', methods=['POST'])  
def agregar():
    return jsonify({"pila": str(miPila.generarDot())})

@app.route('/getImagen')  
def getPila():
    return jsonify({"pila": miPila.printPila()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)