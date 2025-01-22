import psycopg2

def conectardb():

    con = psycopg2.connect(

        host='localhost',
        database = 'IFlix',
        user = 'postgres',
        password = '123'
    )
    return con

def login(user,senha):
    con = conectardb()
    cur = con.cursor()
    sq = f"SELECT * from usuario where login='{user}' and senha='{senha}'  "
    cur.execute(sq)
    saida = cur.fetchall()

    cur.close()
    con.close()

    return saida


def inserir_usuario( login, senha, nome):

    conn = conectardb()
    cur = conn.cursor()
    try:
        sql = f"INSERT INTO usuario (login, senha, nome) VALUES ('{login}','{senha}','{nome}' )"
        cur.execute(sql)

    except psycopg2.IntegrityError:
        conn.rollback()
        exito = False
    else:
        conn.commit()
        exito = True

    cur.close()
    conn.close()
    return exito


def votar( id):

    conn = conectardb()
    cur = conn.cursor()
    try:
        sql = f"UPDATE filmes SET qtdevotos = qtdevotos + 1 WHERE id='{id}'"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conn.rollback()
        exito = False
    else:
        conn.commit()
        exito = True

    cur.close()
    conn.close()
    return exito

def listar_votos():
    con = conectardb()
    cur = con.cursor()
    sq = f"SELECT * FROM filmes ORDER BY qtdevotos DESC"
    cur.execute(sq)
    saida = cur.fetchall()

    cur.close()
    con.close()
    return saida



