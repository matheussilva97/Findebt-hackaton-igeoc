from flask import Flask, request
from App.models import listaCliente, buscaCliente, atualizaDados
import json
from flask import Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/cliente', methods=['GET'])
def cliente():
    return Response(json.dumps(listaCliente()),  mimetype='application/json')


@app.route('/cliente/<cpf>', methods=['GET'])
def returnCliente(cpf):
    return buscaCliente(cpf)


@app.route('/cliente/<cpf>', methods=['PUT'])
def updateJson(cpf):
    content = request.get_json(silent=True)
    return atualizaDados(cpf, content)
