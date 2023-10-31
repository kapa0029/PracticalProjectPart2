from persistence.DataPersistence import DataPersistence
from presentation.UserInterface import UserInterface

# Program by Sneha Ka Patel | 041076617 | kapa0029@algonquinlive.com

# Create an instance of DataPersistence with the CSV file name
persistence = DataPersistence('travelq.csv')

# Read records from the CSV file using the DataPersistence instance
records = persistence.read_records()

# Finally, an instance of UserInterface is created,
# passing the records list and persistence object.
user_interface = UserInterface()

# Start the user interface
user_interface.display_menu()
