from flask import Flask , render_template, request, redirect

app = Flask(__name__)
#--------------------------------------------------------------------------


@app.route("/")
def inicio():
    return render_template("inicio.html")





@app.route("/contactos", methods=['GET', 'POST'])
def contactos():
    if request.method == 'POST':
        # Recoger los datos del formulario
        nombre = request.form.get("nombre")
        correo = request.form.get("correo")
        mensaje = request.form.get("mensaje")
        # Renderizar la página de salida con los datos proporcionados
        return render_template("salidademensajes.html", nombre=nombre, correo=correo, mensaje=mensaje)
    # Si es una petición GET, renderizar el formulario de contacto
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

