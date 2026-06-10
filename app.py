import os
import json
import re
from pathlib import Path

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-me')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)


def validar_formulario_contato(dados):
    erros = []

    nome = dados.get('nome', '').strip()
    if not nome:
        erros.append('Nome é obrigatório.')
    elif len(nome) < 2:
        erros.append('Nome deve ter pelo menos 2 caracteres.')
    elif len(nome) > 100:
        erros.append('Nome deve ter no máximo 100 caracteres.')

    email = dados.get('email', '').strip()
    padrao_email = r'^[^\s@]+@[^\s@]+\.[^\s@]{2,}$'
    if not email:
        erros.append('Email é obrigatório.')
    elif not re.match(padrao_email, email):
        erros.append('Email inválido. Use o formato nome@email.com')

    telefone = dados.get('telefone', '').strip()
    apenas_numeros = re.sub(r'\D', '', telefone)
    if not telefone:
        erros.append('Telefone é obrigatório.')
    elif len(apenas_numeros) < 10 or len(apenas_numeros) > 11:
        erros.append('Telefone deve ter DDD + número, com 10 ou 11 dígitos.')

    assuntos_validos = ['orcamento', 'duvidas', 'reclamacao']
    assunto = dados.get('assunto', '').strip()
    if not assunto:
        erros.append('Selecione um assunto.')
    elif assunto not in assuntos_validos:
        erros.append('Assunto inválido.')

    mensagem = dados.get('mensagem', '').strip()
    if not mensagem:
        erros.append('Mensagem é obrigatória.')
    elif len(mensagem) < 10:
        erros.append('Mensagem deve ter pelo menos 10 caracteres.')
    elif len(mensagem) > 2000:
        erros.append('Mensagem deve ter no máximo 2000 caracteres.')

    return erros


@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/catalogo')
def catalogo():
    products_path = BASE_DIR / 'products.json'
    with products_path.open('r', encoding='utf-8') as file:
        todos_produtos = json.load(file)

    categorias = [
        'Limpeza de Pisos',
        'Banheiro',
        'Cozinha',
        'Lavanderia',
        'Descartáveis',
        'Profissional',
        'Eco-Friendly'
    ]

    categoria_selecionada = request.args.get('categoria')

    if categoria_selecionada:
        produtos = [produto for produto in todos_produtos if produto['category'] == categoria_selecionada]
    else:
        produtos = todos_produtos

    return render_template(
        'catalogo.html',
        produtos=produtos,
        categorias=categorias,
        categoria_selecionada=categoria_selecionada
    )


@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        dados = request.form
        erros = validar_formulario_contato(dados)

        if erros:
            return render_template('contato.html', erros=erros, form=dados)

        destinatario = os.getenv('MAIL_DESTINATARIO')
        if not destinatario:
            erros = ['MAIL_DESTINATARIO não configurado no ambiente.']
            return render_template('contato.html', erros=erros, form=dados)

        assunto_map = {
            'orcamento': 'Orçamento',
            'duvidas': 'Dúvidas',
            'reclamacao': 'Reclamação'
        }

        assunto_txt = assunto_map.get(dados.get('assunto', ''), 'Contato pelo site')

        corpo = (
            f"Nome: {dados.get('nome')}\n"
            f"Email: {dados.get('email')}\n"
            f"Telefone: {dados.get('telefone')}\n"
            f"Assunto: {assunto_txt}\n\n"
            f"Mensagem:\n{dados.get('mensagem')}"
        )

        try:
            msg = Message(
                subject=f'Contato do site - {assunto_txt}',
                recipients=[destinatario],
                body=corpo
            )
            mail.send(msg)
            flash('Mensagem enviada com sucesso!', 'sucesso')
            return redirect(url_for('contato'))
        except Exception:
            erros = ['Não foi possível enviar a mensagem agora. Verifique a configuração do e-mail.']
            return render_template('contato.html', erros=erros, form=dados)

    return render_template('contato.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
