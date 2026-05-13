# EnCasaLimpeza 🧹

Projeto extensionista — site institucional para empresa de limpeza doméstica.

## Tecnologias
- Python + Flask (backend)
- HTML/CSS/JS (frontend)
- Jinja2 (templates)
- JSON (fonte de dados dos produtos)

## Páginas do projeto

| Página     | Rota        | Status     |
|------------|-------------|------------|
| Início     | `/`         | ✅ Pronta  |
| Sobre      | `/sobre`    | ✅ Pronta  |
| Catálogo   | `/catalogo` | ✅ Pronta  |
| Contato    | `/contato`  | ✅ Pronta  |

## Como rodar

```bash
# Ative o ambiente virtual
source venv/bin/activate

# Rode o servidor
python3 app.py
```

Acesse: http://127.0.0.1:5000

## Estrutura principal

```
ProjetoExtensionistaEnCasaLimpeza/
├── app.py              ← rotas Flask e lógica principal
├── products.json       ← fonte de dados dos produtos do catálogo
├── templates/          ← páginas HTML (Jinja2)
│   ├── base.html
│   ├── inicio.html
│   ├── sobre.html
│   ├── catalogo.html
│   └── contato.html
└── static/
    └── css/
        └── global.css
```

## Catálogo

Os produtos são carregados do arquivo `products.json` e renderizados dinamicamente pela rota `/catalogo`. O filtro por categoria funciona via query string (`?categoria=Cozinha`).

## Equipe

| Dupla | Integrantes     | Responsabilidade        |
|-------|-----------------|-------------------------|
| 1     | Pedro + João    | Estrutura geral + Contato |
| 2     | Gabriel + Luis  | Catálogo + Produtos     |
| 3     | Julia + Camilla | Início + Sobre          |

> Guia de padrões e boas práticas: [GUIA_PADRAO.md](./GUIA_PADRAO.md)
