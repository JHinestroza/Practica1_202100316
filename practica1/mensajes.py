from flask import jsonify

class Mensajes:
    def __init__(self):
        self.mensajes = []

    def agregar(self, mensaje):
        self.mensajes.append(mensaje)

    def obtener(self):
        return self.mensajes

    def borrar(self):
        self.mensajes = []
    
    def gestionarPeticion(self, request):
        if request.method == 'POST':
            valorLeido = request.form['valor']
            return jsonify({"usuarios":"jsjjss", "mensajes":"se han actualizado "+valorLeido+" mensajes nuevos"})
        else:
            return jsonify({"error": "no se ha podido procesar la peticion"})