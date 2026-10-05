from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pagina_home():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/contato")
def contato():
    return render_template('contatos.html')

@app.route("/produtos")
def produtos():
    return render_template('produtos.html')

if __name__ == '__main__':
    app.run(debug=True)