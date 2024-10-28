import unittest
from server.storage_provider import StorageProvider
from user.challenge_nonce_generator import ChallengeNonceGenerator

class TestVerificationPhase(unittest.TestCase):
    def setUp(self):
        self.storage_provider = StorageProvider()
        self.nonce_generator = ChallengeNonceGenerator()

    def test_generate_proof(self):
        block_id = 'block1'
        data = 'test_data'
        self.storage_provider.store_data_block(block_id, data)
        nonce = self.nonce_generator.generate_nonce()
        proof = self.storage_provider.generate_proof(nonce, block_id)
        self.assertIsNotNone(proof)
