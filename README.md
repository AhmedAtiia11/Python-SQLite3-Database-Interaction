# Project Title

**Python SQLite3 Database Interaction and Report Generation**

## Overview

This Python project demonstrates how to connect to an SQLite3 database, retrieve data, and save the results in JSON and CSV formats. Additionally, the project generates a report containing key statistics about the retrieved data.

## Features

- **Database Interaction**: Connects to an SQLite3 database and retrieves all records from a specified table.
- **Data Export**: Saves the retrieved data in both JSON and CSV formats.
- **Report Generation**: Generates a text report that includes the total number of records, sample records, and additional insights.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AhmedAtiia11/Python-SQLite3-Database-Interaction.git
    ```
   
2. **Navigate to the project directory**:
    ```bash
    cd Python-SQLite3-Database-Interaction
    ```

3. **Install the required packages**:
    Make sure you have Python 3 installed.
    sqlite3 , CSV, Json are all builtin modules

4. **Create the SQLite3 database**:
    Ensure that your SQLite3 database (`sample.db`) is set up with the correct schema and data.

## Usage

1. **Run the main script**:
    ```bash
    python main.py
    ```

2. The script will connect to the `sample.db` database, retrieve data, save it in JSON and CSV formats, and generate a report (`report.txt`).

## Project Structure

```
.
├── README.md
├── main.py
├── database_handler.py
├── file_manager.py
├── report_generator.py
├── schema.sql
└── sample.db
```

- `main.py`: The main entry point of the application.
- `database_handler.py`: Handles database connections and data retrieval.
- `file_manager.py`: Manages data conversion and export to JSON/CSV.
- `report_generator.py`: Generates a summary report based on the retrieved data.
- `schema.sql`: Contains the schema used by sqlite.
- `sample.db`: The SQLite3 database file.
