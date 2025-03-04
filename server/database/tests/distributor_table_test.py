import unittest
import sqlite3
from server.database.tables.distributor_table import DistributorTable
from server.database.tables.database import Database


class TestDistributorTable(unittest.TestCase):

    def test_create(self):
        test_database = Database(dbname=':memory:')

        distributors = DistributorTable(db=test_database)
        distributors.create()

        got = distributors.select(f'''SELECT * FROM {distributors.table_name}''',[])
        want = [] # In this case, we have no data, we just want to make sure there's no error
        self.assertEqual(got, want, f"test failed: got {got}, want {want}")

    def test_seed(self):
        test_database = Database(dbname=':memory:')

        distributors = DistributorTable(db=test_database)
        distributors.create()
        distributors.seed()

        got = distributors.select(f'''SELECT distributor_name FROM {distributors.table_name} WHERE distributor_name="Bob Elliot" LIMIT 1''',[])
        want = [('Bob Elliot',)]
        self.assertEqual(got, want, f"test failed: got {got}, want {want}")


    def test_get_distributor(self):
        test_database = Database(dbname=':memory:')

        distributors = DistributorTable(db=test_database)
        distributors.create()
        distributors.seed()       

        name = "Bob Elliot"
        link_url = "https://www.bob-elliot.co.uk/"
        
        got = distributors.get_distributor(name)
        want = [('Bob Elliot', 'https://www.bob-elliot.co.uk/')]
        self.assertEqual(got, want, f"test failed: got {got}, want {want}")

    def test_drop(self):
        with self.assertRaises(sqlite3.OperationalError):
            test_database = Database(dbname=':memory:')
    
            distributors = DistributorTable(db=test_database)
            distributors.create()
            distributors.seed()
    
            got = distributors.select(f'''SELECT distributor_name FROM {distributors.table_name} WHERE distributor_name="Bob Elliot" LIMIT 1''',[])
            want = [('Bob Elliot',)]
            self.assertEqual(got, want, f"test failed: got {got}, want {want}")

            distributors.drop()
            distributors.select(f'''SELECT * FROM {distributors.table_name}''',[])

if __name__ == '__main__':
    unittest.main()
    