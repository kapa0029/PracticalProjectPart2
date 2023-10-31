class TravelRecord:
    """Represents a travel record.

    Attributes:
        ref_number (str): The reference number for the record.
        title_en (str): The title in English.
        purpose_en (str): The purpose in English.
        start_date (str): The start date of the travel.
        end_date (str): The end date of the travel.
        airfare (str): The cost of airfare.
        other_transport (str): The cost of other transportation.
        lodging (str): The cost of lodging.
        meals (str): The cost of meals.
        other_expenses (str): Other expenses.
        total (str): The total expenses.
    """

    def __init__(self, row):
        """Initializes a TravelRecord object with data from a CSV row.

        Args:
            row (list): A list containing CSV data representing a travel record.

        The order of values in the row list should match the order of attributes in this class.
        """
        self.ref_number = row[0]
        self.title_en = row[2]
        self.purpose_en = row[5]
        self.start_date = row[7]
        self.end_date = row[8]
        self.airfare = row[11]
        self.other_transport = row[12]
        self.lodging = row[13]
        self.meals = row[14]
        self.other_expenses = row[15]
        self.total = row[16]
