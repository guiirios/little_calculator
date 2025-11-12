🧮 My Calculator

A simple Python calculator that performs basic arithmetic operations — addition, subtraction, multiplication, and division — using flexible argument handling with *args.

🚀 Features

➕ Addition — Adds multiple numbers.

➖ Subtraction — Subtracts multiple numbers in sequence.

✖️ Multiplication — Multiplies any number of inputs.

➗ Division — Divides numbers sequentially.

💻 How It Works

This project defines a Calculator class with methods to handle mathematical operations.
It uses *args to accept any number of arguments.

Example
# Import or paste the class into your project

class Calculator:
    def add(self, *args):
        result = args[0]
        for num in args[1:]:
            result += num
        return result

    def substract(self, *args):
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

    def multiply(self, *args):
        result = args[0]
        for num in args[1:]:
            result *= num
        return result

    def divide(self, *args):
        result = args[0]
        for num in args[1:]:
            result /= num
        return result

# Create an instance and use it
cal1 = Calculator()

print(cal1.add(4, 5))          # ➜ 9
print(cal1.substract(10, 3))   # ➜ 7
print(cal1.multiply(2, 3, 4))  # ➜ 24
print(cal1.divide(100, 5, 2))  # ➜ 10.0

📁 Project Structure
my_calculator/
│
├── calculator.py      # Main class
└── README.md          # Project documentation

🧠 Concepts Used

Object-Oriented Programming (OOP) — Encapsulating functionality in a class.

*args — Handling multiple arguments dynamically.

Loops — Iterating through numbers for calculations.

🛠️ Requirements

Python 3.8 or higher

Run the script directly using:

python calculator.py

🧩 Author

Guilherme Rios (Rioz)
💡 Beginner Python project to practice classes, loops, and argument unpacking.
