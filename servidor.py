
from flask import *
import dao

app = Flask(__name__)

app.secret_key = 'FSM310411@'

@app.route('/')
def principal():
    return render_template('principal.html')


@app.route('/cadastrarusuario', methods=['GET'])
def mostrar_pagina_cadastro():
    return render_template('cadastrarusuario.html')

@app.route('/melhores_filmes')
def mostrar_pagina_filmes():
    if 'login' in session:
        usuario = dao.listar_votos()
        return render_template('melhores_filmes.html', lista=usuario)
    else:
        return render_template('principal.html')


@app.route('/inserirusuario', methods=['POST'])
def inserir_usuario():
    login = request.form.get('login')
    senha = request.form.get('senha')
    nome = request.form.get('nome')

    if dao.inserir_usuario(login, senha, nome):
        return render_template('principal.html', msg='Usuário cadastrado com sucesso')
    else:
        return render_template('principal.html', msg='Usuário já existente')


@app.route('/login', methods=['POST', 'GET'])
def fazer_login():

    if 'login' in session:
        return render_template('iflix.html')

    if request.method == 'GET':
        return render_template('naocadastrado.html')

    login = request.form.get('username')
    senha = request.form.get('password')


    if len(dao.login(login, senha)) > 0:
        session['login'] = login
        return render_template('iflix.html')

    else:
        return render_template('principal.html')

@app.route('/logout', methods=['GET'])
def fazer_logout():
    session.pop('login')
    return render_template('principal.html')

@app.route('/vote_button', methods=['POST'])
def votar_filme():
    id = request.form.get('filme')
    dao.votar(id)
    return render_template('iflix.html')

@app.route('/listar_votos')
def listar_usuarios():

    if 'login' in session:
        votos = dao.listar_votos()
        print(votos)
        return render_template('melhores_filmes.html', lista=votos)

    if request.method == 'GET':
        return render_template('naocadastrado.html')


@app.route('/nao_cadastrado' )
def usuario_naocadastrado():
    return render_template('naocadastrado.html')

@app.route('/voltar' , methods=['GET'])
def voltar_pagina():
    return render_template('iflix.html')

if __name__ == '__main__':
    app.run(debug=True)