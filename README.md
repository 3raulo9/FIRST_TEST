# Python Project

This is a Python project that includes several functions for performing various operations. The project is structured as follows:

- `tools/numbers/comp.py`: This module contains two functions:
    - `sumofdigits(num)`: This function takes a number as input and returns the sum of its digits.
    - `ispal(num)`: This function checks if a number is a palindrome (it reads the same backward as forward) and returns `True` if it is, and `False` otherwise.

- `tools/numbers/simp.py`: This module contains two functions:
    - `add_numbers(num1, num2)`: This function takes two numbers as input and returns their sum.
    - `subtract_numbers(num1, num2)`: This function takes two numbers as input and returns their difference.

- `tools/col.py`: This module contains the `myzip(it1, it2)` function, which takes two iterable objects as arguments and returns a list of tuples. Each tuple contains one element from each of the input iterables, in the same order they appear in the input.

- `main.py`: This is the main script that imports and tests all the functions. It includes an interactive menu that allows the user to choose which function they want to use and input their own values.

## How to Run

1. Clone this repository to your local machine.
2. pip freeze > requirements.txt
3. Navigate to the directory containing `main.py`.
4. Run `python main.py` to start the interactive menu.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
