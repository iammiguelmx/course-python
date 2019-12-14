from flask import Flask
from flask import render_template

app = Flask(__name__) # '__main__'

@app.route('/')
def url_principal():
    return render_template('sitio.html', nombre = "Miguel")

@app.route('/acerca-de')
def url_acerca_de():
    hobbies = [
        "Programar",
        "Dormir",
        "Cantar",
        "Dormir otra vez",
        "Comer",
        "Desarollo de proyectos"
    ]
    return render_template('acerca.html', hobbies = hobbies)


@app.route('/futuro/<int:years>')
def url_futuro(years):
    mi_nombre = "Miguel"
    mi_edad = years + 50
    return render_template('sitio.html',nombre = mi_nombre, edad = mi_edad)

@app.errorhandler(404)
def url_error(error=None):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True)

