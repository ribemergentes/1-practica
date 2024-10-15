from flask import Flask , render_template, request, redirect

app = Flask(__name__)
#--------------------------------------------------------------------------


@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/contactos")
def contactos():
    return render_template("contactos.html")

@app.route("/noticias")
def noticias():
    return render_template("noticias.html")
@app.route("/quienes_somos")
def quienessomos():
    return render_template("quienes_somos.html")
@app.route("/servicios")
def servicios():
    return render_template("servicios.html")


#---------------------------------------------------------------------
if __name__ =="__main__":
    app.run(debug=True)

