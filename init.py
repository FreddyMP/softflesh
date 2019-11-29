from flask import Flask, render_template, request, Request, jsonify
import con
import model
import json
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create/", methods = ['POST'] )
def create_db():
    paquete = request.get_json("dat")
    valor = paquete['nombre']
    print(model.create_bussines(paquete['nombre']))
    print(model.registrar(paquete['nombre'], paquete['rnc'], paquete['provincia'], paquete['direccion'], paquete['telefono'], paquete['correo'], paquete['encargado']))
    print(model.create_user('SoftFlesh','Freddy','Freddy0770'))
    print(paquete['nombre'])
    return jsonify(paquete)
@app.after_request
def add_headers(response):
    response.headers.add("Access-Control-allow-origin", '*')
    response.headers.add("Access-Control-allow-Headers", 'Content-Type,Autorization')
    return response
if __name__ == '__main__':
    app.run(debug=True)
    