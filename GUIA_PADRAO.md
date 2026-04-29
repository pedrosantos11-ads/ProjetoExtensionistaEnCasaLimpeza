# 📋 Guia de Padrão — EnCasaLimpeza
> Leia isso ANTES de criar qualquer página. Seguir esse padrão evita conflito no Git e garante que o projeto fique consistente.

---

## 🗂️ Estrutura do Projeto

```
ProjetoExtensionistaEnCasaLimpeza/
├── app.py                  ← rotas Flask (NÃO MEXA sem avisar o grupo)
├── templates/
│   ├── base.html           ← template base (NÃO MEXA)
│   ├── contato.html        ← exemplo pronto para referência
│   ├── inicio.html         ← sua página (se você for o responsável)
│   ├── sobre.html          ← sua página (se você for o responsável)
│   ├── produtos.html       ← sua página (se você for o responsável)
│   └── catalogo.html       ← sua página (se você for o responsável)
└── static/
    └── css/
        └── global.css      ← CSS global (NÃO MEXA sem avisar o grupo)
```

---

## ✅ Responsabilidades

| Página         | Arquivo a criar          | Rota no app.py |
|----------------|--------------------------|----------------|
| Início         | `templates/inicio.html`  | `/`            |
| Sobre          | `templates/sobre.html`   | `/sobre`       |
| Produtos       | `templates/produtos.html`| `/produtos`    |
| Catálogo       | `templates/catalogo.html`| `/catalogo`    |

> ⚠️ Cada pessoa cria APENAS o arquivo da sua página. Não edite arquivos dos outros.

---

## 🚀 Passo a Passo

### 1. Faça o git pull antes de qualquer coisa

```bash
git pull origin main
```

> Nunca comece a codar sem atualizar o repositório local.

---

### 2. Crie seu arquivo na pasta `templates/`

O nome do arquivo deve ser exatamente o que está na tabela acima.

---

### 3. Comece SEMPRE com essa estrutura base

```html
{% extends 'base.html' %}

{% block titulo %}EnCasaLimpeza – NOME DA SUA PÁGINA{% endblock %}

{% block estilos %}
<style>
  /* CSS específico desta página aqui */
</style>
{% endblock %}

{% block conteudo %}

  <!-- Conteúdo da sua página aqui -->

{% endblock %}
```

> ⛔ NUNCA coloque `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`, `<nav>` ou `<footer>` no seu arquivo.
> O `base.html` já tem tudo isso. Se você repetir, vai quebrar a página.

---

### 4. Regras de CSS

- CSS global → já está em `static/css/global.css` (não mexa)
- CSS da sua página → coloca dentro do `{% block estilos %}`
- Use as variáveis CSS do projeto:

```css
/* ✅ Correto */
color: var(--cor-primaria);
padding: var(--espaco-md);

/* ❌ Errado */
color: #2e7d32;
padding: 20px;
```

---

### 5. Links internos — sempre com url_for

```html
<!-- ✅ Correto -->
<a href="{{ url_for('sobre') }}">Sobre nós</a>

<!-- ❌ Errado -->
<a href="/sobre">Sobre nós</a>
```

---

### 6. Commit e push

```bash
git add templates/nome-da-sua-pagina.html
git commit -m "feat: cria página sobre"
git push origin main
```

> ⚠️ Use `git add` apenas no SEU arquivo.

---

## ❌ Erros comuns — evite esses

| Erro | Por que é problema | Como evitar |
|------|-------------------|-------------|
| Criar `<html>` dentro da página filha | Duplica a estrutura, quebra o layout | Não coloque — o `base.html` já tem |
| Espaço ou comentário antes de `{% extends %}` | O Jinja não reconhece a herança | `{% extends %}` deve ser a PRIMEIRA linha |
| Usar `href="/sobre"` em vez de `url_for` | Pode quebrar com mudança de host | Sempre use `url_for('nome_da_rota')` |
| Editar o `base.html` sem avisar | Quebra TODAS as páginas do grupo | Fale com o grupo antes |
| Commitar sem `git pull` antes | Gera conflito | Sempre `git pull` antes de começar |

---

## 📌 Referência rápida — nomes das rotas

```
inicio    → url_for('inicio')
sobre     → url_for('sobre')
produtos  → url_for('produtos')
catalogo  → url_for('catalogo')
contato   → url_for('contato')
```

---

## 💡 Dúvidas?

Olhe o arquivo `templates/contato.html` — ele já está pronto e segue todos os padrões.
Use como referência de como estruturar a sua página.

Repositório: https://github.com/pedrosantos11-ads/ProjetoExtensionistaEnCasaLimpeza
