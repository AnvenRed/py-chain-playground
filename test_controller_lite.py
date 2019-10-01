from controller_lite import app
import pytest
import unittest

class TestController(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_full_chain(self):
        test_response = self.app.get('/chain')
        assert test_response.status == '200 OK'
        assert b'length' in test_response.data

    def test_add_block(self):
        test_response = self.app.get('/addBlock')
        assert test_response.status == '200 OK'
        # print(test_response.data)
        assert b'Block Added' in test_response.data




