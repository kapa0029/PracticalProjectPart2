from flask import Flask, render_template, request, redirect

from modules.business.BusinessLogic import BusinessLogic
from modules.persistence.DataPersistence import DataPersistence
from modules.travelrecord import TravelRecord

app = Flask(__name__)

# Your existing instances of classes
business_logic = BusinessLogic()
data_persistence = DataPersistence(host='localhost', user='root', password='rudraBhatt#123', database='travelq')


@app.route('/')
def main_page():
    """Render the main page."""
    return render_template('main_page.html')


@app.route('/add_record', methods=['GET', 'POST'])
def add_record():
    """Handle adding a new travel record."""
    if request.method == 'POST':
        # Extract form data
        ref_number = request.form.get('ref_number')
        title_en = request.form.get('title_en')
        purpose_en = request.form.get('purpose_en')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        airfare = request.form.get('airfare')
        other_transport = request.form.get('other_transport')
        lodging = request.form.get('lodging')
        meals = request.form.get('meals')
        other_expenses = request.form.get('other_expenses')
        total = request.form.get('total')

        # Create a TravelRecord object
        new_record = TravelRecord([ref_number, '', title_en, '', '', purpose_en, '', start_date, end_date, '', '', airfare,
                                   other_transport, lodging, meals, other_expenses, total])

        # Add the record to the business logic
        business_logic.create_new_record(new_record)

        # Redirect to the main page or another appropriate page
        return redirect('/')
    else:
        # Render the add_record page
        return render_template('add_record.html')


@app.route('/search_records', methods=['GET', 'POST'])
def search_records_page():
    """Render the search records page."""
    if request.method == 'POST':
        # Extract form data for search criteria
        criteria = {}

        for field in request.form:
            value = request.form[field].strip()
            if value:
                criteria[field] = value

        # Perform the search using the BusinessLogic class
        matching_records = business_logic.search_records(criteria)

        # Render the search_results page with the matching records
        return render_template('search_results.html', records=matching_records)
    else:
        # Render the search_records page
        return render_template('search_records.html')


@app.route('/search_results', methods=['POST'])
def search_results():
    """Render the search results page."""
    # Extract search criteria from the form data
    criteria = {
        'ref_number': request.form.get('ref_number'),
        'title_en': request.form.get('title_en'),
        'purpose_en': request.form.get('purpose_en'),
        'start_date': request.form.get('start_date'),
        'end_date': request.form.get('end_date'),
        'airfare': request.form.get('airfare'),
        'other_transport': request.form.get('other_transport'),
        'lodging': request.form.get('lodging'),
        'meals': request.form.get('meals'),
        'other_expenses': request.form.get('other_expenses'),
        'total': request.form.get('total')
        # Add more criteria as needed
    }

    # Remove empty criteria
    criteria = {k: v for k, v in criteria.items() if v is not None and v != ''}

    # Call the search_records method from your business logic
    matching_records = business_logic.search_records(criteria)

    # Render the search_results page with the matching records
    return render_template('search_results.html', records=matching_records)


@app.route('/view_records')
def view_records_page():
    """Render the view records page."""
    # Get the current list of records from the business logic
    records = business_logic.get_records()

    # Render the view_records page with the records
    return render_template('view_records.html', records=records)


@app.route('/edit_record/<ref_number>', methods=['GET'])
def edit_record_page(ref_number):
    """Render the edit records page."""
    # Find the record to edit based on the reference number
    record_to_edit = business_logic.find_record_by_ref_number(ref_number)

    if record_to_edit:
        return render_template('edit_record.html', record=record_to_edit)
    else:
        return "Record not found."


@app.route('/edit_record', methods=['POST'])
def edit_record():
    # Handle the form submission for editing a record
    ref_number = request.form.get('ref_number')

    # Collect updated fields into a dictionary
    updated_fields = {}
    for field in request.form:
        updated_fields[field] = request.form.get(field).strip()

    # Update the record in the business logic
    business_logic.edit_record(ref_number, updated_fields)

    # Redirect to the main page or another appropriate page
    return redirect('/view_records')


@app.route('/delete_record/<ref_number>', methods=['GET'])
def delete_record(ref_number):
    """Render the delete records page."""
    # Delete the record based on the reference number
    business_logic.delete_record_by_ref_number(ref_number)

    # Redirect to the main page or another appropriate page
    return redirect('/view_records')


# Add a route to handle data reload
@app.route('/reload_data', methods=['POST'])
def reload_data():
    # Call the load_data method of the BusinessLogic class to reload data
    business_logic.load_data()

    # Redirect to the main page or another appropriate page
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
