from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

generos = [
    {"nome": "Ação", "slug": "acao", "cor": "#ff0000"},
    {"nome": "Terror", "slug": "terror", "cor": "#ff4500"},
    {"nome": "Comédia", "slug": "comedia", "cor": "#ffcc00"},
    {"nome": "Drama", "slug": "drama", "cor": "#ff00ff"},
    {"nome": "Romance", "slug": "romance", "cor": "#ff1493"},
    {"nome": "Animação", "slug": "animacao", "cor": "#00ff00"},
    {"nome": "Cinema antigo", "slug": "cinema-antigo", "cor": "#00ffff"}
]

CAPA_CLUBE = "https://lh3.googleusercontent.com/d/1FhGXKN9--93jpZVkTawbsM_ROQYDm9H2"

filmes_db = {
    "acao": [{"titulo": "Drive - Tensão Máxima (1997)", "link": "https://ok.ru/video/1922594835104", "thumb": ""}],
    "comedia": [
        {"titulo": "Um maluco no golfe (1996)", "link": "https://ok.ru/video/4207491549845", "thumb": ""},
        {"titulo": "As Apimentadas", "link": "https://ok.ru/video/559416216263", "thumb": ""},
        {"titulo": "As Apimentadas - Mandando Ver", "link": "https://ok.ru/video/8832564726368", "thumb": ""}
    ],
    "drama": [
        {"titulo": "Corra, Lola, Corra (1998)", "link": "https://ok.ru/video/6370743749303", "thumb": ""},
        {"titulo": "O Profissional (1994)", "link": "https://ok.ru/video/3663969651428", "thumb": ""},
        {"titulo": "8 Mile- Rua das ilusões (2002)", "link": "https://ok.ru/video/1396647398042", "thumb": ""}
    ],
    "romance": [{"titulo": "Benedetta (2021)", "link": "https://ok.ru/video/10438247451277", "thumb": ""}],
    "cinema-antigo": [
        {"titulo": "Clube dos Cinco (1985)", "link": "https://ok.ru/videoembed/8473915624001", "thumb": CAPA_CLUBE},
        {"titulo": "O Fantasma da Ópera (1989)", "link": "https://ok.ru/video/4830921034296", "thumb": ""},
        {"titulo": "A orgia da morte (1964)", "link": "https://ok.ru/video/5179913472682", "thumb": ""}
    ]
}

@app.route('/')
def index():
    return render_template('index.html', generos=generos)

@app.route('/categoria/<slug>')
def categoria(slug):
    genero_info = next((g for g in generos if g['slug'] == slug), None)
    filmes = filmes_db.get(slug, [])
    return render_template('categoria.html', genero=genero_info, filmes=filmes)

@app.route('/player')
def player():
    titulo = request.args.get('t', 'Vídeo')
    link = request.args.get('l', '')
    return render_template('filme.html', filme={"titulo": titulo, "link": link})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
