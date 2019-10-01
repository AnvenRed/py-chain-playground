import unittest

from blockchain_basic import Blockchain

class TestChain(unittest.TestCase):

    def setUp(self):
        self.blockchain = Blockchain()

    def testAddTransaction(self):
        self.blockchain.add_transaction("test_transaction")
        assert len(self.blockchain.current_transactions) == 1, "Should be 1"
        self.blockchain.add_new_block(1111)

    def testThreeTransactions(self):
        assert len(self.blockchain.chain) == 1, "Chain Length Should be 1"
        for i in range(3):
            self.blockchain.add_transaction(i)
        assert len(self.blockchain.current_transactions) == 0, "Current Transactions List Should be Empty"
        assert len(self.blockchain.chain) == 2, "Chain Length Should be 2"

    def testAddBlock(self):
        self.blockchain.add_new_block(1111)
        assert len(self.blockchain.chain) == 2, "Chain Length Should be 2"
        assert self.blockchain.last_block['previous_hash'] == 1111, "Last Block Previous Hash Should be 1111"

if __name__ == '__main__':
    unittest.main()
