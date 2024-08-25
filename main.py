from database_handler import DatabaseHandler
from file_manager import FileHandler
from report_generator import ReportGenerator

def main():
    # Initialize handlers
    db_handler = DatabaseHandler('sample.db')
    file_handler = FileHandler()
    report_generator = ReportGenerator()

    try:
        # Execute query and fetch data
        rows = db_handler.execute_query("SELECT * FROM data")
        column_names = db_handler.fetch_column_names()

        # Convert to list of dictionaries
        result = [dict(zip(column_names, row)) for row in rows]

        # Save JSON and CSV data
        file_handler.save_json('data.json', result)
        file_handler.save_csv('data.csv', result, column_names)

        # Generate and save report
        report = report_generator.generate_report(result)
        file_handler.save_report('report.txt', report)

        print("Report generated: report.txt")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        db_handler.close_connection()

if __name__ == "__main__":
    main()
