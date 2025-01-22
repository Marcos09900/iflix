from flask import *
import dao

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('principal.html')


@app.route('/cadastrarusuario', methods=['GET'])
def mostrar_pagina_cadastro():
    return render_template('cadastrarusuario.html')

@app.route('/melhores_filmes')
def mostrar_pagina_filmes():
    return render_template('melhores_filmes.html')


@app.route('/inserirusuario', methods=['POST'])
def inserir_usuario():
    login = request.form.get('login')
    senha = request.form.get('senha')
    nome = request.form.get('nome')

    if dao.inserir_usuario(login, senha, nome):
        return render_template('principal.html', msg='Usuário cadastrado com sucesso')
    else:
        return render_template('principal.html', msg='Usuário já existente')


@app.route('/login', methods=['POST'])
def fazer_login():
    login = request.form.get('username')
    senha = request.form.get('password')


    if len(dao.login(login, senha)) > 0:
        return render_template('iflix.html')
    else:
        return render_template('principal.html')

@app.route('/logout', methods=['POST'])
def fazer_logout():
    return render_template('iflix.html')


@app.route('/vote_button', methods=['POST'])
def votar_filme():
    id = request.form.get('filme')
    dao.votar(id)
    return render_template('iflix.html')

@app.route('/listar_votos')
def listar_usuarios():
    votos = dao.listar_votos()
    print(votos)
    return render_template('melhores_filmes.html', lista=votos)


app.run(debug=True)