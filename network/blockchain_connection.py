from web3 import Web3

class BlockchainConnection:
    def __init__(self, rpc_url):
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))

    def connect(self):
        return self.web3.isConnected()
