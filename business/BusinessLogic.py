from persistence.DataPersistence import DataPersistence


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
        print("New record added to in-memory data.")

    def edit_record(self, ref_number, field_name, new_value):
        """Edit an existing record in the in-memory data.

        Args:
            ref_number (str): The reference number of the record to edit.
            field_name (str): The name of the field to edit.
            new_value (str): The new value for the field.
        """
        for record in self.records:
            if record.ref_number == ref_number:
                if field_name == "Title (English)":
                    record.title_en = new_value
                elif field_name == "Purpose (English)":
                    record.purpose_en = new_value
                elif field_name == "Start Date":
                    record.start_date = new_value
                # Add more field edits as needed
                print("Record edited in memory.")
                return

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
