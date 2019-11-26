from flask import Flask, render_template, request, Request
import con
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods = ['POST'] )
def create_db():
    nombre = request.form.get("nombre")
    #print(nombre)
if __name__ == '__main__':
    app.run(debug=True)
    