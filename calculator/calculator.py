import pandas as pd
from history_manager import HistoryManager
from logger import setup_logging

class Calculator:
    def __init__(self):
        self.history_manager = HistoryManager()
        self.logger = setup_logging()

    def add(self, a, b):
        result = a + b
        self.logger.info(f"Add: {a} + {b} = {result}")
        self.history_manager.add_to_history('add', a, b, result)
        return result

    def subtract(self, a, b):
        result = a - b
        self.logger.info(f"Subtract: {a} - {b} = {result}")
        self.history_manager.add_to_history('subtract', a, b, result)
        return result

    def multiply(self, a, b):
        result = a * b
        self.logger.info(f"Multiply: {a} * {b} = {result}")
        self.history_manager.add_to_history('multiply', a, b, result)
        return result

    def divide(self, a, b):
        if b == 0:
            self.logger.error("Division by zero attempted")
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self.logger.info(f"Divide: {a} / {b} = {result}")
        self.history_manager.add_to_history('divide', a, b, result)
        return result

def start_repl():
    calculator = Calculator()
    while True:
        command = input("Enter command (add, subtract, multiply, divide, history, exit): ").strip()
        if command == "exit":
            break
        elif command == "history":
            print(calculator.history_manager.history)
        else:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if command == "add":
                    print(calculator.add(a, b))
                elif command == "subtract":
                    print(calculator.subtract(a, b))
                elif command == "multiply":
                    print(calculator.multiply(a, b))
                elif command == "divide":
                    print(calculator.divide(a, b))
                else:
                    print("Unknown command.")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    start_repl()
