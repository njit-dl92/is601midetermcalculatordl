import pandas as pd

class HistoryManager:
    def __init__(self):
        # Initialize an empty DataFrame with specified columns
        self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])

    def add_to_history(self, operation, operand1, operand2, result):
        # Create a new DataFrame with the new record
        new_record = pd.DataFrame({
            'operation': [operation],
            'operand1': [operand1],
            'operand2': [operand2],
            'result': [result]
        })
        # Concatenate the new record with the existing history DataFrame
        self.history = pd.concat([self.history, new_record], ignore_index=True)

    def save_history(self, filename='history.csv'):
        # Save the history DataFrame to a CSV file
        self.history.to_csv(filename, index=False)

    def load_history(self, filename='history.csv'):
        # Load history from a CSV file into the DataFrame
        self.history = pd.read_csv(filename)

    def clear_history(self):
        # Clear the history DataFrame
        self.history = pd.DataFrame(columns=['operation', 'operand1', 'operand2', 'result'])
