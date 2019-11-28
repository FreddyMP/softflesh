from flask import Flask, render_template, request, Request, jsonify
import con
import json
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create/", methods = ['POST'] )
def create_db():
    nombre = request.get_json("datos")
    valor = nombre['nom']
    print(nombre['nom'])
    return jsonify(nombre)
   
if __name__ == '__main__':
    app.run(debug=True)
    