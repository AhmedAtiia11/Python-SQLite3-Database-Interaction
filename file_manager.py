
import json
import csv

class FileHandler:
    def save_json(self, file_name, data):
        try:
            with open(file_name, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except IOError as e:
            print(f"Error saving JSON data: {e}")
            raise

    def save_csv(self, file_name, data, column_names):
        try:
            with open(file_name, 'w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=column_names)
                writer.writeheader()
                writer.writerows(data)
        except IOError as e:
            print(f"Error saving CSV data: {e}")
            raise

    def save_report(self, file_name, report):
        try:
            with open(file_name, 'w') as report_file:
                report_file.write(report)
        except IOError as e:
            print(f"Error saving report: {e}")
            raise
