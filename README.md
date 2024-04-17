# Python Final Project using Flask - St. Clair

This is a python project to display data from a SQLite database via a website.

## Project Structure:

- `main_website.py`: Contains the conplete flask application code along with route definitions.
- `templates/`: It's a directory contains all HTML templates for the website.
- `creating_database.py`: This .py file has all  the functions for creating database, table creation and insertion of data.
- `moviedetails.csv`: Sample CSV file which contains all data for database insertion.
- `README.md`: This file provides an overview of the project and further instructions to move ahead in project.
- `requirements.txt`: This file lists all the pre-requisite Python packages required for running the project.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/jaspreetsinghsain/group5_flask_project
    ```

2. Navigate to the project directory:

    ```bash
    cd flask-project
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python main_website.py
    ```

## Usage

- Visit [http://localhost:5000/](http://localhost:5000/) in your web browser to access the home page.
- Click on the "About" link to view information about the project.
- Click on the "Data" link to view the data displayed on the website.
