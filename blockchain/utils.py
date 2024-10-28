from web3 import Web3

class BlockchainUtils:
    def __init__(self, rpc_url):
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.contract = None

    def load_contract(self, abi, address):
        self.contract = self.web3.eth.contract(address=address, abi=abi)

    def record_data_hash(self, data_hash, metadata):
        tx_hash = self.contract.functions.recordDataHash(data_hash, metadata).transact()
        return tx_hash
