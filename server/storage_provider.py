class StorageProvider:
    def __init__(self):
        self.data_store = {}

    def store_data_block(self, block_id, data):
        self.data_store[block_id] = data

    def generate_proof(self, challenge_nonce, block_id):
        data_block = self.data_store.get(block_id)
        proof = hash((challenge_nonce, data_block))
        return proof