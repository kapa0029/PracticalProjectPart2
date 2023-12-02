from modules.persistence.DataPersistence import DataPersistence
from datetime import datetime, date


class BusinessLogic:
    """
        BusinessLogic class manages in-memory travel records and interacts with the persistence layer.

        This class provides functionality to load, save, create, edit, and delete travel records.
        It initializes the persistence layer and loads data from the specified database during instantiation.
        """

    def __init__(self):
        """Initialize the BusinessLogic class.

        This class is responsible for managing in-memory travel records and interacting with the persistence layer.
        """
        self.records = []
        self.persistence = DataPersistence(host='localhost', user='root', password='rudraBhatt#123',
                                           database='travelq')
        self.load_data()

    def load_data(self):
        """Reload data from the dataset by reading from the CSV file."""
        if self.persistence is not None:
            self.records = self.persistence.read_records()
            print("Data reloaded successfully.")
        else:
            print("Persistence layer not initialized.")

    def save_data(self):
        """Persist the data from memory to a new CSV file."""
        if self.persistence is not None:
            self.persistence.save_records(self.records)
        else:
            print("Persistence layer not initialized.")

    def create_new_record(self, new_record):
        """Create a new record and store it in the in-memory data.

        Args:
            new_record (TravelRecord): A TravelRecord object to be added to the in-memory data.
        """
        # Append the new record to the in-memory data
        self.records.append(new_record)
        print(f"New record added: {new_record}")
        print("In-memory data:", self.records)

    def edit_record(self, ref_number, new_values):
        """Edit an existing record in the in-memory data.

        Args:
            ref_number (str): The reference number of the record to edit.
            new_values (dict): A dictionary containing field names as keys and new values as values.
        """
        record_to_edit = self.find_record_by_ref_number(ref_number)

        if record_to_edit:
            for field_name, new_value in new_values.items():
                if hasattr(record_to_edit, field_name):
                    setattr(record_to_edit, field_name, new_value)
                    print(
                        f"Field '{field_name}' updated to '{new_value}' for record with reference number {ref_number}.")
                else:
                    print(f"Field '{field_name}' not found in record structure.")
            print("Record edited in memory.")
        else:
            print("Record not found in memory.")

    def delete_record(self, index):
        """Delete a record from the data.

        Args:
            index (int): The index of the record to be deleted.
        """
        try:
            # Convert the index to an integer
            index = int(index) - 1  # Adjust for Python list indexing
            if 0 <= index < len(self.records):
                deleted_record = self.records.pop(index)
                print(f"Record with reference number {deleted_record.ref_number} has been deleted from in-memory data.")
            else:
                print("Invalid record index. No record deleted.")
        except ValueError:
            print("Invalid input. Please enter a valid record index.")

    def get_records(self):
        """Get the current list of records.

        Returns:
            list: A list of TravelRecord objects representing the in-memory travel records.
        """
        return self.records

    def search_records(self, criteria):
        """Search for records based on multiple criteria with OR operation.

        Args:
            criteria (dict): A dictionary containing search criteria.

        Returns:
            list: A list of TravelRecord objects matching any of the search criteria.
        """
        # Retrieve all records from the in-memory data
        all_in_memory_records = self.get_records()

        # Initialize an empty list to store matching records
        matching_in_memory_records = []

        # Iterate over each record in the in-memory data
        for record in all_in_memory_records:
            # Check if the record meets any of the search criteria
            if any(self._matches_criteria(record, key, value) for key, value in criteria.items()):
                matching_in_memory_records.append(record)

        return matching_in_memory_records

    def find_record_by_ref_number(self, ref_number):
        """Find a record by its reference number.

        Args:
            ref_number (str): The reference number of the record to find.

        Returns:
            TravelRecord or None: The found record or None if not found.
        """
        for record in self.records:
            if record.ref_number == ref_number:
                return record
        return None

    def delete_record_by_ref_number(self, ref_number):
        """Delete a record by its reference number.

        Args:
            ref_number (str): The reference number of the record to delete.
        """
        for record in self.records:
            if record.ref_number == ref_number:
                self.records.remove(record)
                print(f"Record with reference number {ref_number} has been deleted.")
                return
        print("Record not found.")

    def _matches_criteria(self, record, key, value):
        """Check if a record matches the specified search criteria."""
        if key == "start_date" or key == "end_date":
            # If the key is a date field, convert both the record's value and the search value to datetime objects
            record_value = getattr(record, key)
            if isinstance(record_value, date):
                record_value = record_value.strftime("%Y-%m-%d")

            record_date = datetime.strptime(record_value, "%Y-%m-%d")
            search_date = datetime.strptime(value, "%Y-%m-%d")
            return record_date == search_date
        else:
            # For non-date fields, perform a regular equality check
            return getattr(record, key) == value

