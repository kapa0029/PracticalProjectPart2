from persistence.DataPersistence import DataPersistence
from presentation.UserInterface import UserInterface

# Program by Sneha Ka Patel | 041076617 | kapa0029@algonquinlive.com

# Create an instance of DataPersistence with the database connection details
# Replace 'your_host', 'your_user', 'your_password', and 'your_database'
# with your actual MySQL server details and database name.
persistence = DataPersistence(host='localhost', user='root', password='rudraBhatt#123', database='travelq')

# Read records from the database using the DataPersistence instance
records = persistence.read_records()

# Finally, an instance of UserInterface is created,
# passing the records list and persistence object.
user_interface = UserInterface()

# Start the user interface
user_interface.display_menu()
