from datetime import datetime


class RenameFile:
    @staticmethod
    def get_filename():
        # Get the current timestamp and format it into a string
        # Format: Year-Month-Day_Hour-Minute-Second (e.g., 2025-12-02_112445)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")

        # Create the filename with the timestamp
        filename = f"screenshot_{timestamp}.png"

        return filename
