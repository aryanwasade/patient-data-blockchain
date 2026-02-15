from flask import Flask, request, jsonify
from flask_cors import CORS
from blockchain import Blockchain

app = Flask(__name__)
CORS(app)   # VERY IMPORTANT

blockchain = Blockchain()

@app.route('/add_record', methods=['POST'])
def add_record():
    data = request.json
    blockchain.add_block(data)
    return jsonify({"message": "Medical record added to blockchain"}), 201

@app.route('/get_chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return jsonify(chain_data)

@app.route('/validate', methods=['GET'])
def validate():
    return jsonify({"Blockchain Valid": blockchain.is_chain_valid()})

if __name__ == '__main__':
    app.run(debug=True)
