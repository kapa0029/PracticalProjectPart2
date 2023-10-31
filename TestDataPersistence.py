import unittest
from persistence.DataPersistence import DataPersistence

#Program by Sneha Ka Patel

class TestDataPersistence(unittest.TestCase):
    """Test case for the DataPersistence class."""

    def test_read_records(self):
        """Test if the DataPersistence class can read records from a CSV file."""
        # Create a DataPersistence object and read records from the test CSV file
        persistence = DataPersistence('test_data.csv')
        records = persistence.read_records()
        print("Program by Sneha Ka Patel")
        # Assert the contents of the first record
        self.assertEqual(records[1].ref_number, "123")
        self.assertEqual(records[2].ref_number, "456")


if __name__ == "__main__":
    unittest.main()
