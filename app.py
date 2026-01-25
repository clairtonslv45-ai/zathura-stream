from flask import Flask, render_template, request
import os

app = Flask(__name__)

generos = [
    {"nome": "Ação", "slug": "acao", "cor": "#ff0000"},
    {"nome": "Comédia", "slug": "comedia", "cor": "#ffcc00"},
    {"nome": "Drama", "slug": "drama", "cor": "#ff00ff"},
    {"nome": "Romance", "slug": "romance", "cor": "#ff1493"},
    {"nome": "Cinema antigo", "slug": "cinema-antigo", "cor": "#00ffff"}
]

filmes_db = {
    "comedia": [
        {"titulo": "Frat Party (A festa) (2009)", "link": "https://ok.ru/video/6695168969223", "thumb": ""}
    ]
}

@app.route('/')
def index(): return render_template('index.html', generos=generos)

@app.route('/categoria/<slug>')
def categoria(slug):
    info = next((g for g in generos if g['slug'] == slug), None)
    return render_template('categoria.html', genero=info, filmes=filmes_db.get(slug, []))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
