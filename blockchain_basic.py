from collections import OrderedDict
import json
import hashlib
import requests


class Blockchain:

    def __init__(self):
        # self.name = name
        self.chain = []
        self.current_transactions = []
        self.nodes = set(self.initialize_nodes())

        self.add_new_block(previous_hash='1')

    def add_transaction(self, transaction):
        self.current_transactions.append(transaction)
        if (len(self.current_transactions) == 3):
            self.add_new_block(self.hash(self.last_block))
            self.current_transactions = []

    def add_new_block(self, previous_hash):
        block = dict()
        block['index'] = len(self.chain) + 1
        block['transactions'] = self.current_transactions
        block['previous_hash'] = previous_hash

        self.current_transactions = []
        self.chain.append(block)
        return block

    def initialize_nodes(self):
        with open("C:\\Users\\avpil\\Projects\\py-chain-playground\\py-chain-playground\\nodes.json",'r') as nodeFile:
            return json.load(nodeFile)["nodes"]

    def is_valid(self, chain):
        """
        Determine if provided Blockchain is considered valid
        :param chain:
        :return: True if chain is valid, False if not
        """
        previous_block = chain[0]
        current_block_index = 1

        while current_block_index < len(chain):
            current_block = chain[current_block_index]
            print(f'{previous_block}')
            print(f'{current_block}')
            print("\n-----------\n")
            previous_block_hash = self.hash(previous_block)
            if current_block['previous_hash'] != previous_block_hash:
                return False
            previous_block = current_block
            current_block_index += 1
        return True

    def resolve_conflicts(self):
        """
        Determining Consensus
        :return: True if Consensus reached and chain replaced, False if Consensus failed and current chain kept as true
        """
        all_nodes = self.nodes

        max_length = len(self.chain)

        response = requests.get('http://localhost:5000/getChain')
        if response.status_code == 200:
            foreign_chain = response.json()
            if len(foreign_chain) > max_length and self.is_valid(foreign_chain):
                print("is true")
                self.chain = foreign_chain

        # for node in all_nodes:
        #     response = requests.get(f'{node}/getChain')
        #     if response.status_code == 200:
        #         foreign_chain = response.json()
        #         if len(foreign_chain)>len(self.chain) and self.is_valid(foreign_chain):
        #             self.chain = foreign_chain



    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

