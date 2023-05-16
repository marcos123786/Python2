from flask import Flask, render_template, request

app = Flask(__name__)

#rota para a pagina principal da aplicação
@app.route('/')
def index():
    title="Curso a EAD Senac"
    return render_template('index.html',title=title)

#rota para pagina de produtod
@app.route('/cursos')
def cursos():
    return render_template('curso.html')

#rota para pagina de produto
@app.route('/contato')
def contato():
    return render_template('contato.html')

#rota para pagina de redes
@app.route('/ead')
def ead():
    return render_template('sobreEAD.html')


#enviando informações para o arquivo html (Templates)
@app.route('/login')
def login():
    titulo = 'Login de Acesso'
    descricao = 'Formulário formulário de login'
    return render_template('login.html',titulo=titulo,descricao=descricao)

#Login de usuário
@app.route('/validacao', methods=["POST"])
def validacao():
    
    if request.method == "GET":
        return render_template('app.html')
    else:
        usuario = request.form.get("user")

        if(usuario == 'gabriel.william@webba.com.br'):
            result = "<h1>Usuário Logado com sucesso!<h1>"
        else:
            result = "<h1>Ocorreu um erro no login</h1>"
    
    return result


if __name__ == '__main__':
    app.run(debug=True)