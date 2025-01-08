from unittest.mock import MagicMock,Mock
import unittest
import sqlite3
from server.database.tables.cassettes_table import createCassettesTable

class TestCassettesTable(unittest.TestCase):
    def test_createCassettesTable(self):
        self.assertEqual(1, 1, "It's wrong")

if __name__ == '__main__':
    unittest.main()
    