import os
import random
import requests
from flask import Flask, jsonify

from backend.blockchain.blockchain import Blockchain
from backend.pubsub import PubSub

app = Flask(__name__)
blockchain = Blockchain()
pubsub = PubSub(blockchain)

@app.route('/')
def route_default():
    return 'Welcome to the blockchain'

@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())

@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_data = 'stubbed_transaction_data'

    blockchain.add_block(transaction_data)

    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)

    return jsonify(block.to_json())

@app.route('/wallet/transact', methods=['POST'])
def route_wallet_transact():
    transaction_data = request.get_json()
    transaction = transaction_pool.existing_transaction(wallet.address)
 
    if transaction:
        transaction.update(
            wallet,
            transaction_data['recipient'],
            transaction_data['amount']
        )
    else:
        transaction = Transaction(
            wallet,
            transaction_data['recipient'],
            transaction_data['amount']
        )
 
    pubsub.broadcast_transaction(transaction)
    transaction_pool.set_transaction(transaction)
 
    return jsonify(transaction.to_json())

ROOT_PORT = 5000
PORT = ROOT_PORT

if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)

    result = requests.get(f'http://127.0.0.1:{ROOT_PORT}/blockchain')
    result_blockchain = Blockchain.from_json(result.json())

    try:
        blockchain.replace_chain(result_blockchain.chain)
        print('\n -- Successfully sycnhronized the local chain')
    except Exception as e:
        print(f'\n -- Error sycnhronizing: {e}')

app.run(port=PORT)