import csv

from modules.travelrecord import TravelRecord


class DataPersistence:
    """Persistence layer for managing data."""
    def __init__(self, file_name):
        self.file_name = file_name
        self.records = []

    def read_records(self, num_records=100):
        """Reads travel records from the CSV file and returns them.

        Args:
            num_records (int, optional): The number of records to read. Default is 50.

        Returns:
            list: A list of TravelRecord objects.
        """
        records = []
        try:
            with open(self.file_name, 'r', newline='', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                for i, row in enumerate(csv_reader):
                    if i < num_records:
                        record = TravelRecord(row)
                        records.append(record)
                    else:
                        break
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        return records

    def save_records(self, records):

        # Program By Sneha Ka Patel


        """Saves a list of records to a new CSV file.

        Args:
            records (list): A list of TravelRecord objects to save.
        """
        fixed_file_name = "output_records.csv"  # Specify a fixed file name
        try:
            with open(fixed_file_name, 'w', newline='', encoding='utf-8') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(["Reference Number", "Title (English)", "Purpose (English)", "Start Date",
                                     "End Date", "Airfare", "Other Transport", "Lodging", "Meals", "Other Expenses",
                                     "Total"])
                for record in records:
                    csv_writer.writerow([record.ref_number, record.title_en, record.purpose_en, record.start_date,
                                         record.end_date, record.airfare, record.other_transport, record.lodging,
                                         record.meals, record.other_expenses, record.total])
            print(f"Data saved to {fixed_file_name}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
