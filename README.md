# GUI Calculator Application

This project is a simple GUI calculator application built using Python's Tkinter library. It provides a user-friendly interface for performing basic arithmetic operations.

## Project Structure

```
gui-calculator
├── src
│   ├── main.py               # Entry point of the application
│   ├── components
│   │   ├── buttons.py        # Defines button components
│   │   └── display.py        # Defines the display component
│   └── utils
│       └── calculator_logic.py # Contains the logic for calculations
├── requirements.txt          # Lists project dependencies
└── README.md                 # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd gui-calculator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- User-friendly interface with buttons for each digit and operation.
- Clear button to reset the input field.
- Responsive design that adjusts to different screen sizes.

## Usage

- Click on the buttons to input numbers and operations.
- Press the "=" button to evaluate the expression.
- Use the "C" button to clear the input field.

## License

This project is licensed under the MIT License.