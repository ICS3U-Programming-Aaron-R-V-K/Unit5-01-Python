# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: May 05, 2025
# The program uses a function called fahrenheit to convert from fahrenheit to Celsius

import math


def fahrenheit():
    # convert celsius to fahrenheit
    celsius_str = input("Enter temperature(celsius): ")
    try:
        celsius = float(celsius_str)

        # Celsius calculation from celsius to fahrenheit
        fahrenheit = (9 / 5) * celsius + 32

        # Display the conversion
        print(f"{celsius} C = {fahrenheit} F")
    except Exception:
        print("Invalid input, Enter an integer")


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
