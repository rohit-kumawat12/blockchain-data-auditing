class DataIntegrityChecker:
    def __init__(self, blockchain, data_block):
        self.blockchain = blockchain
        self.data_block = data_block

    def check_integrity(self, metadata):
        data_hash = hash(self.data_block)
        return self.blockchain.get_metadata(data_hash) == metadata
