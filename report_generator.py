
import json
import random

class ReportGenerator:
    def generate_report(self, data):
        try:
            total_records = len(data)
            sample_records = random.sample(data, min(5, total_records))  

            report = f"Total Records: {total_records}\n"
            report += "\nSample Records:\n"
            for record in sample_records:
                report += json.dumps(record, indent=4) + "\n"
            report += "\nAdditional Insights:\n"
            # Add any additional insights or statistics here

            return report
        except (ValueError, KeyError, TypeError) as e:
            print(f"Error generating report: {e}")
            raise
