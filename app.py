import os
import pymysql
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def conectar_db():
        return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=int(os.getenv("DB_PORT", 3306)),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=5
        )

@app.route("/")
def pagina_home():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/contatos", methods=["GET", "POST"])
def cont():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form['telefone']
        mensagem = request.form["mensagem"]

        conexao = conectar_db()
        with conexao.cursor() as cursor:
            cursor.execute(
                "INSERT INTO tb_mensagem (nome, email, telefone, mensagem) VALUES (%s, %s, %s, %s)",
                (request.form["nome"], request.form["email"], request.form["telefone"], request.form["mensagem"])
            )
        conexao.commit()
        conexao.close()
        return redirect(url_for("cont"))
    
    return render_template('contatos.html')

@app.route("/listar")
def listar():
    conexao = conectar_db()

    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM tb_mensagem")
        mensagens = cursor.fetchall()
    conexao.close()
    return render_template("listar.html", mensagens=mensagens)

@app.route("/produtos")
def produtos():
    return render_template('produtos.html')

if __name__ == '__main__':
    app.run(debug=True)