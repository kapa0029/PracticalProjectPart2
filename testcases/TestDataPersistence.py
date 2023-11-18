import unittest
from modules.travelrecord import TravelRecord


class TestTravelRecord(unittest.TestCase):
    """Test cases for the TravelRecord class."""

    def test_init(self):
        """Test the initialization of the TravelRecord object."""
        # Arrange
        row = ['T1', '', 'Title1', '', '', 'Purpose1', '', '2023-01-01', '2023-01-05', '', '', '100', '50', '200', '150', '25', '525']

        # Act
        travel_record = TravelRecord(row)

        # Assert
        self.assertEqual(travel_record.ref_number, 'T1')
        self.assertEqual(travel_record.title_en, 'Title1')
        self.assertEqual(travel_record.purpose_en, 'Purpose1')
        self.assertEqual(travel_record.start_date, '2023-01-01')
        self.assertEqual(travel_record.end_date, '2023-01-05')
        self.assertEqual(travel_record.airfare, '100')
        self.assertEqual(travel_record.other_transport, '50')
        self.assertEqual(travel_record.lodging, '200')
        self.assertEqual(travel_record.meals, '150')
        self.assertEqual(travel_record.other_expenses, '25')
        self.assertEqual(travel_record.total, '525')

if __name__ == '__main__':
    unittest.main()
