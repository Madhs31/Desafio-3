from app import app
from flask import render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL

# Configuração do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'ap1'
app.config['MYSQL_PASSWORD'] = 'Fatec@123'
app.config['MYSQL_DB'] = 'api1ads'
mysql = MySQL(app)

#Senha 
senha = 'avatar'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)

# Rota para adicionar uma nova tarefa MySQL
@app.route('/add', methods=['POST'])
def add_task():
    if request.method == 'POST':
        func_id = request.form['func_id']
        nome = request.form['nome']
        nota = request.form['nota']
        opiniao = request.form['opiniao']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO formulario (func_id, nome, nota, opiniao) VALUES (%s, %s, %s, %s)", (func_id, nome, nota, opiniao))
        
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    
#formulário
@app.route('/formulario')
def formulario():
    func_id = session.get("func_id")
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM formulario")
    exams = cur.fetchall()
    cur.close()
    return render_template('formulario.html', exams=exams)

#Verifica senha
@app.route('/validate-password', methods=['POST'])
def validate_password():
    password = request.form.get('password')
    if password == senha:
        return redirect(url_for('formulario'))
    else:
        return redirect(url_for('index'))