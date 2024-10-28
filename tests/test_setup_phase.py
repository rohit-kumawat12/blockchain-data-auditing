import unittest
from blockchain.utils import BlockchainUtils

class TestSetupPhase(unittest.TestCase):
    def setUp(self):
        self.blockchain = BlockchainUtils("http://127.0.0.1:8545")

    def test_record_data_hash(self):
        data_hash = b'test_data_hash'
        metadata = b'test_metadata'
        tx_hash = self.blockchain.record_data_hash(data_hash, metadata)
        self.assertIsNotNone(tx_hash)
