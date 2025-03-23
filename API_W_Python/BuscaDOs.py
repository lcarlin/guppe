from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# Configurações da API do Google Custom Search
GOOGLE_API_KEY = "AIzaSyAxy4JoHf2CasaoqL9C56OeLJnimORW6OI"
SEARCH_ENGINE_ID = "94ad3180f7a1f4e8f"

# Lista de sites pré-definidos para busca
SITES = [
"https//diario.ac.gov.br/ ",
"https//diario.imprensaoficial.al.gov.br/ ",
 "https//diofe.portal.ap.gov.br/ ",
 "http//imprensaoficial.am.gov.br/ ",
 "https//dool.egba.ba.gov.br/ ",
 "http//pesquisa.doe.seplag.ce.gov.br/doepesquisa/sead.do?page=ultimasEdicoes&cmd=11&action=Ultimas ",
 "https//dio.es.gov.br/ ",
 "https//diariooficial.abc.go.gov.br/ ",
 "https//www.diariooficial.ma.gov.br/ ",
 "https//www.iomat.mt.gov.br/ ",
 "https//www.spdo.ms.gov.br/diariodoe ",
 "https//www.jornalminasgerais.mg.gov.br/ ",
 "http//www.ioepa.com.br/ ",
 "https//auniao.pb.gov.br/doe ",
 "https//www.imprensaoficial.pr.gov.br/ ",
 "https//www.cepe.com.br/ ",
 "http//www.diariooficial.pi.gov.br/ ",
 "https//portal.ioerj.com.br/ ",
 "http//diariooficial.rn.gov.br/ ",
 "https//www.diariooficial.rs.gov.br/ ",
 "https//diof.ro.gov.br/ ",
 "https//www.imprensaoficial.rr.gov.br/ ",
 "https//doe.sea.sc.gov.br/ ",
 "https//doe.sp.gov.br/ ",
 "https//iose.se.gov.br/diario-oficial ",
 "https//diariooficial.to.gov.br/ ",
 "https//www.in.gov.br/servicos/diario-oficial-da-uniao "
]

# Página HTML básica
template = """
<!DOCTYPE html>
<html>
<head>
    <title>Busca Personalizada</title>
</head>
<body>
    <h1>Busca Personalizada</h1>
    <form action="/search" method="get">
        <input type="text" name="query" placeholder="Digite sua busca" required>
        <input type="number" name="num_results" placeholder="Número de resultados" value="10" min="1">
        <button type="submit">Buscar</button>
    </form>
    {% if results %}
        <h2>Resultados:</h2>
        <ul>
            {% for result in results %}
                <li><a href="{{ result['link'] }}" target="_blank">{{ result['title'] }}</a></li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(template)


@app.route('/search')
def search():
    query = request.args.get("query")
    num_results = int(request.args.get("num_results", 10))

    if not query:
        return "Por favor, insira um termo de busca.", 400

    # Criando a string de sites para busca
    site_filter = " OR ".join([f"site:{site}" for site in SITES])
    full_query = f"{query} {site_filter}"
    print(full_query)

    # Fazendo a busca na API do Google Custom Search
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": query,
        # "q": full_query,
        "num": num_results
    }
    response = requests.get(url, params=params)
    data = response.json()

    results = []
    if "items" in data:
        results = [{"title": item["title"], "link": item["link"], "snippet": item.get("snippet", "") } for item in data["items"]]

    return render_template_string(template, results=results)


if __name__ == '__main__':
    app.run(debug=True)
