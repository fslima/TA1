import urllib, json

arquivo = urllib.urlopen('http://localhost:8000/servico/oportunidades/abertas').read()
arq = json.loads(arquivo)
