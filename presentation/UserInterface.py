from prettytable import PrettyTable
from business.BusinessLogic import BusinessLogic
from modules.travelrecord import TravelRecord


class UserInterface:
    """Presentation layer for user interaction."""

    def __init__(self):

        """Initializes the UserInterface."""
        self.records = []
        self.business = BusinessLogic()

    def display_menu(self):
        """Display the main menu for user interaction."""
        while True:
            print()
            print("Program by Sneha Ka Patel")
            print()
            print("---> Options:")
            print("1. Reload data from the dataset")
            print("2. Persist data to a new file")
            print("3. Display records")
            print("4. Create a new record")
            print("5. Edit a record")
            print("6. Delete a record")
            print("0. Exit")
            print()
            choice = input("---> Enter your choice: ")

            if choice == "1":
                self.business.load_data()

            elif choice == "2":
                self.business.save_data()

            elif choice == "3":
                self.display_records()

            elif choice == "4":
                print("Creating a new record:")
                ref_number = input("Enter Reference Number: ")
                title_en = input("Enter Title (English): ")
                purpose_en = input("Enter Purpose (English): ")
                start_date = input("Enter Start Date: ")
                end_date = input("Enter End Date: ")
                airfare = input("Enter Airfare: ")
                other_transport = input("Enter Other Transport: ")
                lodging = input("Enter Lodging: ")
                meals = input("Enter Meals: ")
                other_expenses = input("Enter Other Expenses: ")
                total = input("Enter Total: ")

                new_record = TravelRecord(
                    [ref_number, '', title_en, '', '', purpose_en, '', start_date, end_date, '', '', airfare,
                     other_transport, lodging, meals, other_expenses, total])
                self.business.create_new_record(new_record)

            elif choice == "5":
                record_ref_number = input("Enter Reference Number of the record to edit: ")
                field_name = input("Enter the field name to edit: ")
                new_value = input(f"Enter the new value for {field_name}: ")
                self.business.edit_record(record_ref_number, field_name, new_value)

            elif choice == "6":
                index = input("Enter index number of the record to delete: ")
                self.business.delete_record(int(index))

            elif choice == "0":
                print("Program by Sneha Ka Patel")
                break

            else:
                print("Invalid choice. Try again.")
                print("Program by Sneha Ka Patel")

    def display_records(self):
        """Display travel records in a tabular format using PrettyTable."""
        # Display records from BusinessLogic's records attribute
        records = self.business.get_records()
        if records:
            # Display records using PrettyTable
            table = PrettyTable()
            table.field_names = [
                "Reference Number",
                "Title (English)",
                "Purpose (English)",
                "Start Date",
                "End Date",
                "Airfare",
                "Other Transport",
                "Lodging",
                "Meals",
                "Other Expenses",
                "Total",
            ]
            for record in records:
                table.add_row([
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
                    record.total,
                ])
            print("Program by Sneha Ka Patel")
            print(table)
        else:
            print("No records found.")
