import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/catalogo')
def catalogo():
    with open('products.json', 'r', encoding='utf-8') as file:
        todos_produtos = json.load(file)

    categorias = [
        'Limpeza de Pisos',
        'Banheiro',
        'Cozinha',
        'Lavanderia',
        'Descartáveis',
        'Equipamentos',
        'Profissional',
        'Eco-Friendly'
    ]

    categoria_selecionada = request.args.get('categoria')

    if categoria_selecionada:
        produtos = [
            produto for produto in todos_produtos
            if produto['category'] == categoria_selecionada
        ]
    else:
        produtos = todos_produtos

    return render_template(
        'catalogo.html',
        produtos=produtos,
        categorias=categorias,
        categoria_selecionada=categoria_selecionada
    )

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)