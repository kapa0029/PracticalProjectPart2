from modules.persistence.DataPersistence import DataPersistence
from modules.presentation.UserInterface import UserInterface

# Program by Sneha Ka Patel | 041076617 | kapa0029@algonquinlive.com


def main():
    """
    Entry point of the travel management program.

    This program connects to a MySQL database, retrieves travel records,
    and provides a user interface for managing and interacting with the data.
    """
    # Create an instance of DataPersistence with the database connection details
    # Replace 'your_host', 'your_user', 'your_password', and 'your_database'
    # with your actual MySQL server details and database name.
    try:
        # Code that may raise exceptions
        persistence = DataPersistence(host='localhost', user='root', password='rudraBhatt#123', database='travelq')
        records = persistence.read_records()
        user_interface = UserInterface(records, persistence)
        user_interface.display_menu()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
