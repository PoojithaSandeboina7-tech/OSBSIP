# BMI Calculator – OASIS INFOBYTE Task 2

## 📌 Project Description

This project is a Python-based BMI (Body Mass Index) Calculator developed as part of the OASIS INFOBYTE Python Programming Internship.

The program takes the user's weight and height, calculates their BMI, and classifies the result into a standard BMI category.

## 🎯 Objective

The main objective of this project is to create a simple Python application that can:

* Accept weight and height from the user
* Calculate BMI
* Classify the BMI result
* Validate user input
* Display helpful error messages for invalid input

## 🛠️ Technologies Used

* Python
* `input()`
* `float()`
* Conditional statements (`if`, `elif`, `else`)
* `try-except` error handling

## 🧮 BMI Formula

```text
BMI = Weight (kg) / Height² (m)
```

## 📊 BMI Categories

| BMI Range    | Category    |
| ------------ | ----------- |
| Below 18.5   | Underweight |
| 18.5 – 24.9  | Normal      |
| 25 – 29.9    | Overweight  |
| 30 and above | Obese       |

## ✨ Features

* Weight input in kilograms
* Height input in meters
* BMI calculation
* BMI rounded to 2 decimal places
* BMI category classification
* Validation for non-numeric input
* Validation for negative or zero values
* User-friendly error messages

## ▶️ How to Run

1. Make sure Python is installed on your computer.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python bmi_calculator.py
```

5. Enter your weight and height when prompted.

## 🧪 Example Output

```text
===== BMI CALCULATOR =====
Enter your weight in kg: 60
Enter your height in meters: 1.65
Your BMI is: 22.04
Category: Normal
```

## ❌ Input Validation Example

For invalid input:

```text
Enter your weight in kg: abc
Error: Please enter numbers only.
```

For negative values:

```text
Enter your weight in kg: -60
Enter your height in meters: -1.65
Error: Weight and height must be positive values.
```

## 📁 Project Structure

```text
Python-Task2-BMICalculator/
│
├── bmi_calculator.py
└── README.md
```

## 👩‍💻 Internship

**Organization:** OASIS INFOBYTE
**Track:** Python Programming
**Task:** Task 2 – BMI Calculator
**Tier:** Beginner
