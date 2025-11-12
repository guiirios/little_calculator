🧮 My Calculator








A simple yet powerful calculator built in Python — made to learn, explore, and have fun with clean and dynamic code.

🌟 Overview

My Calculator is a minimalist Python project that performs essential math operations:
addition, subtraction, multiplication, and division — all wrapped inside a single, elegant class.

It’s designed to be:
🧩 educational, ✨ clean, and 💡 expandable.

⚙️ Features

➕ Addition: Sum any number of values

➖ Subtraction: Subtract in sequence

✖️ Multiplication: Multiply multiple numbers

➗ Division: Divide progressively

🧠 Supports unlimited arguments using *args

📘 Demonstrates Object-Oriented Programming (OOP)

💡 Code Example
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


# Example usage
cal1 = Calculator()

print(cal1.add(4, 5))          # ➜ 9
print(cal1.substract(10, 3))   # ➜ 7
print(cal1.multiply(2, 3, 4))  # ➜ 24
print(cal1.divide(100, 5, 2))  # ➜ 10.0

📂 Project Structure
my_calculator/
│
├── calculator.py      # Main class file
└── README.md          # Project documentation

🧠 Concepts Used
Concept	Description
🧩 Classes & Methods	Organizes the logic and keeps the code reusable
⚡ *args	Handles multiple dynamic inputs easily
🔁 Loops	Iterate through arguments for calculations
🧮 Arithmetic Logic	Core math operations implemented manually
🚀 How to Run

Make sure you have Python 3.8+ installed.

Clone or download this repository.

Run the script using:

python calculator.py

👨‍💻 About the Author

👋 Guilherme Rios (Rioz)
Python learner passionate about logic, clean code, and building cool stuff.

“Great things start with small, consistent steps.” 💭
