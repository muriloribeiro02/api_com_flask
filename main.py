#Na linha abaixo, estou fazendo o import das bibliotecas que estarei usando
#além do flask, estou importando as extensões do flask, que está possiilitando enviar e receber informações da web

from flask import Flask, make_response, jsonify, request
from bd import Carros

#Aqui estou iniciando o codigo
app = Flask(__name__)
#Para não ordenar de a-z automaticamente
app.config['Json_SORT_KEYS'] = False


#Um endpoint com a rota carros, e o metodo GET, que está servindo para ler a minha API
@app.route('/carros', methods=['GET'])

#função que está puxando os items do "banco"
def get_carros():
    return make_response(
        jsonify(Carros)
    )

#endpoint para criar um item, metodo POST, para adicionar informações no bd
@app.route('/carros', methods=['POST'])
def create_carro():
#Aqui o request está sendo usado para enviar uma alteração para o nosso bd
    carro = request.json
    Carros.append(carro)
#O append pega um objeto e adiciona na ultima posição
    return make_response(
        jsonify(carro)
    )
#Pelo postman fiz criei um novo id, com um novo item
#Mudando de GET para POST, indo no body da aplicação, no e escrevi o novo carro do nosso bd


app.run()
