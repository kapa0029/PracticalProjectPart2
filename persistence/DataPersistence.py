import mysql.connector
from modules.travelrecord import TravelRecord

class DataPersistence:
    """
    DataPersistence class handles database connectivity and operations.

    This class provides methods to create a table, read records from the database, and save records to the database.
    """

    def __init__(self, host, user, password, database):
        """
        Initialize the DataPersistence class.

        Args:
            host (str): The hostname or IP address of the MySQL server.
            user (str): The MySQL user to authenticate as.
            password (str): The password to authenticate with.
            database (str): The name of the database to use.
        """
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_table(self):
        """
        Create a table in the database if it does not exist.

        The table structure is defined to store travel records.
        """
        create_table_query = """
        CREATE TABLE IF NOT EXISTS travel_records (
            ref_number VARCHAR(255),
            title_en VARCHAR(255),
            purpose_en VARCHAR(255),
            start_date VARCHAR(255),
            end_date VARCHAR(255),
            airfare VARCHAR(255),
            other_transport VARCHAR(255),
            lodging VARCHAR(255),
            meals VARCHAR(255),
            other_expenses VARCHAR(255),
            total VARCHAR(255)
        )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def read_records(self):
        """
        Read travel records from the database and return them as a list of TravelRecord objects.

        Returns:
            list: A list of TravelRecord objects.
        """
        select_query = "SELECT * FROM travel_records"
        self.cursor.execute(select_query)
        records = [TravelRecord(row) for row in self.cursor.fetchall()]
        return records

    def save_records(self, records):
        """
        Save a list of TravelRecord objects to the database.

        Args:
            records (list): A list of TravelRecord objects to save.
        """
        self.create_table()  # Ensure the table exists

        insert_query = """
        INSERT INTO travel_records
        (ref_number, title_en, purpose_en, start_date, end_date, airfare, other_transport, lodging, meals, other_expenses, total)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        for record in records:
            values = (
                record.ref_number,
                record.title_en,
                record.purpose_en,
                record.start_date,
                record.end_date,
                record.airfare,
                record.other_transport,
                record.lodging,
                record.meals,
                record.other_expenses,
                record.total
            )
            self.cursor.execute(insert_query, values)

        self.connection.commit()
