class UserClient:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def upload_data(self, data_block, block_id):
        data_hash = hash(data_block)
        metadata = hash(f"metadata_{block_id}")
        self.blockchain.record_data_hash(data_hash, metadata)

    def verify_data_integrity(self, challenge_nonce, block_id):
        proof = self.blockchain.request_proof(challenge_nonce, block_id)
        return proof == hash((challenge_nonce, block_id))
