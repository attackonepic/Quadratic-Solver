# Quadratic Equation Solver

This is a basic GUI quadratic equation solver implemented using the tkinter library in Python. It allows you to solve quadratic equations of the form `ax^2 + bx + c = 0` by providing the values for `a`, `b`, and `c`.

## Functionality

The program provides the following features:

- User-friendly graphical user interface (GUI)
- Entry fields for inputting values of `a`, `b`, and `c`
- Buttons to solve the quadratic equation and clear the input fields
- Output fields to display the solutions `x1` and `x2`
- Support for real solutions and complex solutions
- Error handling for invalid input values

## Usage

1. Launch the application. The main window titled "QES" will appear.
2. Enter valid numeric values for `a`, `b`, and `c` into their respective input fields.
3. Click the "Solve!" button to calculate the solutions.
4. If the input values are valid, the solutions will be displayed in the `x1` and `x2` output fields.
5. If any of the input values are invalid (such as non-numeric characters), the output fields will display an "Invalid input" message.
6. To clear the input and output fields, click the "Clear" button.

Note: The program will only run and provide valid solutions if all three input values (`a`, `b`, and `c`) are valid numeric values. If any of the inputs are invalid, the program will display an "Invalid input" message in the output fields.

## Dependencies

The program requires the following dependencies:

- Python 3.x
- tkinter library (included in standard Python distribution)
- math library (included in standard Python distribution)

## Running the Program

To run the program, execute the Python script in your preferred Python environment. Ensure that all dependencies are installed beforehand.

```bash
python quadratic_solver.py
