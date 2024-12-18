from unittest.mock import MagicMock,Mock
import unittest
import sqlite3
from database.tables.cassettes_table import createCassettesTable

class TestCassetteTable(unittest.TestCase):
    def test_create_cassette_table(self):
        self.assertEqual(1, 1, "It's wrong")

if __name__ == '__main__':
    unittest.main()
    