# 📋 Guia de Padrão — EnCasaLimpeza

> Leia isso ANTES de criar ou editar qualquer arquivo. Seguir esse padrão evita conflito no Git e garante consistência no projeto.

---

## 🗂️ Estrutura do Projeto

```
ProjetoExtensionistaEnCasaLimpeza/
├── app.py                  ← rotas Flask + lógica (NÃO MEXA sem avisar o grupo)
├── products.json           ← dados dos produtos do catálogo (editar aqui para mudar produtos)
├── templates/
│   ├── base.html           ← template base (NÃO MEXA)
│   ├── inicio.html
│   ├── sobre.html
│   ├── catalogo.html
│   └── contato.html        ← use como referência de estrutura
└── static/
    └── css/
        └── global.css          ← CSS global (NÃO MEXA sem avisar o grupo)
```

---

## ✅ Responsabilidades

| Página    | Arquivo                  | Rota         | Dupla responsavel  |
|-----------|--------------------------|--------------|-----------------------|
| Início    | `templates/inicio.html`  | `/`          | Julia + Camilla       |
| Sobre     | `templates/sobre.html`   | `/sobre`     | Julia + Camilla       |
| Catálogo  | `templates/catalogo.html`| `/catalogo`  | Gabriel + Luis        |
| Contato   | `templates/contato.html` | `/contato`   | Pedro + João         |

> ⚠️ Cada pessoa edita APENAS o arquivo da sua página. Não edite arquivos dos outros sem combinar.

---

## 📦 Como os produtos funcionam

Os produtos ficam em `products.json`, na raiz do projeto. **Não coloque produtos dentro do `app.py` ou do `catalogo.html`.**

Cada produto deve ter esse formato:

```json
{
  "name": "Nome do produto",
  "brand": "Marca",
  "description": "Descrição breve",
  "category": "Cozinha"
}
```

Categorias válidas:
- `Limpeza de Pisos`
- `Banheiro`
- `Cozinha`
- `Lavanderia`
- `Descartáveis`
- `Equipamentos`
- `Profissional`
- `Eco-Friendly`

> ⚠️ O campo `category` deve estar escrito EXATAMENTE igual às opções acima. Maiúsculas e acentos importam.

---

## 🚀 Passo a Passo

### 1. Atualize o repositório local antes de qualquer coisa

```bash
git pull origin main
```

> Nunca comece a codar sem atualizar primeiro.

---

### 2. Estrutura base de qualquer página

```html
{% extends 'base.html' %}

{% block titulo %}EnCasaLimpeza – NOME DA PÁGINA{% endblock %}

{% block estilos %}
<style>
  /* CSS específico desta página aqui */
</style>
{% endblock %}

{% block conteudo %}

  <!-- Conteúdo da página aqui -->

{% endblock %}
```

> ⛔ NUNCA coloque `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`, `<nav>` ou `<footer>` na página filha. O `base.html` já tem tudo isso.

---

### 3. Regras de CSS

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

### 4. Links internos — sempre com url_for

```html
<!-- ✅ Correto -->
<a href="{{ url_for('sobre') }}">Sobre nós</a>

<!-- ❌ Errado -->
<a href="/sobre">Sobre nós</a>
```

---

### 5. Commit e push

```bash
git add templates/nome-da-sua-pagina.html
git commit -m "feat: descrição do que você fez"
git push origin main
```

> ⚠️ Use `git add` apenas no SEU arquivo para evitar subir mudanças de outros por engano.

---

## ❌ Erros comuns — evite esses

| Erro | Por que é problema | Como evitar |
|------|-------------------|-------------|
| Criar `<html>` dentro da página filha | Duplica a estrutura, quebra o layout | Não coloque — o `base.html` já tem |
| Espaço ou comentário antes de `{% extends %}` | O Jinja não reconhece a herança | `{% extends %}` deve ser a PRIMEIRA linha |
| Usar `href="/sobre"` em vez de `url_for` | Pode quebrar com mudança de host | Sempre use `url_for('nome_da_rota')` |
| Editar o `base.html` sem avisar | Quebra TODAS as páginas do grupo | Fale com o grupo antes |
| Commitar sem `git pull` antes | Gera conflito | Sempre `git pull` antes de começar |
| Escrever categoria diferente no JSON | Filtro não funciona | Copie o nome exato da lista de categorias |
| Colocar produtos dentro do `app.py` | Volta para dívida técnica | Sempre edite o `products.json` |

---

## 📌 Referência rápida — nomes das rotas

```
inicio    → url_for('inicio')
sobre     → url_for('sobre')
catalogo  → url_for('catalogo')
contato   → url_for('contato')
```

---

## 💡 Dúvidas?

Olhe o arquivo `templates/contato.html` — ele já está pronto e segue todos os padrões. Use como referência.

Repositório: https://github.com/pedrosantos11-ads/ProjetoExtensionistaEnCasaLimpeza
