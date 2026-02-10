from flask import Flask, render_template, request
import os

app = Flask(__name__)

generos = [
    {"nome": "Ação", "slug": "acao", "cor": "#ff0000"},
    {"nome": "Terror", "slug": "terror", "cor": "#ff4500"},
    {"nome": "Comédia", "slug": "comedia", "cor": "#ffcc00"},
    {"nome": "Drama", "slug": "drama", "cor": "#ff00ff"},
    {"nome": "Romance", "slug": "romance", "cor": "#ff1493"},
    {"nome": "Animação", "slug": "animacao", "cor": "#00ff00"},
    {"nome": "Fantasia", "slug": "fantasia", "cor": "#9933ff"},
    {"nome": "Cinema antigo", "slug": "cinema-antigo", "cor": "#00ffff"}
]

filmes_db = {
    "acao": [{"titulo": "Drive - Tensão Máxima (1997)", "link": "https://ok.ru/videoembed/1922594835104"}],
    "terror": [
        {"titulo": "Terror no Pântano 2", "link": "https://ok.ru/videoembed/991264246391"},
        {"titulo": "Olhos famintos 1 (2001) Dublado", "link": "https://ok.ru/videoembed/383529192100"}
    ],
    "comedia": [
        {"titulo": "CJ7 o brinquedo mágico", "link": "https://ok.ru/videoembed/10147592276650"},
        {"titulo": "Kung Pow: O Mestre da Confusão", "link": "https://ok.ru/videoembed/9743619852946"},
        {"titulo": "Pelas garotas e pela glória (2009)", "link": "https://ok.ru/videoembed/6681522866916"},
        {"titulo": "Frat Party (A festa) (2009)", "link": "https://ok.ru/videoembed/6695168969223"},
        {"titulo": "Um maluco no golfe (1996)", "link": "https://ok.ru/videoembed/4207491549845"},
        {"titulo": "As Apimentadas", "link": "https://ok.ru/videoembed/559416216263"},
        {"titulo": "As Apimentadas - Mandando Ver", "link": "https://ok.ru/videoembed/8832564726368"}
    ],
    "drama": [
        {"titulo": "Notorious B.I.G. (2009)", "link": "https://ok.ru/videoembed/30186211954"},
        {"titulo": "Corra, Lola, Corra (1998)", "link": "https://ok.ru/videoembed/6370743749303"},
        {"titulo": "O Profissional (1994)", "link": "https://ok.ru/videoembed/3663969651428"},
        {"titulo": "8 Mile- Rua das ilusões (2002)", "link": "https://ok.ru/videoembed/1396647398042"}
    ],
    "romance": [{"titulo": "Benedetta (2021)", "link": "https://ok.ru/videoembed/10438247451277"}],
    "fantasia": [
        {"titulo": "Coração de tinta o livro mágico", "link": "https://ok.ru/videoembed/5243438303914"},
        {"titulo": "Edward mãos de tesoura", "link": "https://ok.ru/videoembed/1707365304907"},
        {"titulo": "Onde Vivem os Monstros", "link": "https://ok.ru/videoembed/2645490862724"},
        {"titulo": "O lar das crianças peculiares", "link": "https://ok.ru/videoembed/456581319275"},
        {"titulo": "O Mistério do Relógio na Parede", "link": "https://ok.ru/videoembed/1851630881387"},
        {"titulo": "O Labirinto do Fauno", "link": "https://ok.ru/videoembed/7406352730852"}
    ],
    "animacao": [
        {"titulo": "A Lenda dos Guardiões", "link": "https://ok.ru/videoembed/383529192100"},
        {"titulo": "Planeta do Tesouro", "link": "https://ok.ru/videoembed/1551464860379"},
        {"titulo": "Planeta 51", "link": "https://ok.ru/videoembed/7251048598034"},
        {"titulo": "A Fuga do Planeta Terra", "link": "https://ok.ru/videoembed/4899872443050"},
        {"titulo": "Reino Escondido", "link": "https://ok.ru/videoembed/1385257044634"}
    ],
    "cinema-antigo": [
        {"titulo": "Clube dos Cinco (1985)", "link": "https://ok.ru/videoembed/8473915624001"},
        {"titulo": "O Fantasma da Ópera (1989)", "link": "https://ok.ru/videoembed/4830921034296"},
        {"titulo": "A orgia da morte (1964)", "link": "https://ok.ru/videoembed/5179913472682"}
    ]
}

@app.route('/')
def index(): return render_template('index.html', generos=generos)

@app.route('/categoria/<slug>')
def categoria(slug):
    info = next((g for g in generos if g['slug'] == slug), None)
    return render_template('categoria.html', genero=info, filmes=filmes_db.get(slug, []))

@app.route('/player')
def player():
    t = request.args.get('t')
    l = request.args.get('l')
    rave_link = f"rave://open?url={l}"
    return render_template('filme.html', filme={"titulo": t, "link": l, "rave": rave_link})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
