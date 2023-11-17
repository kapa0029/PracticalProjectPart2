import mysql.connector
from modules.travelrecord import TravelRecord

class DataPersistence:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_table(self):
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
        select_query = "SELECT * FROM travel_data"
        self.cursor.execute(select_query)
        records = [TravelRecord(row) for row in self.cursor.fetchall()]
        return records

    def save_records(self, records):
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
