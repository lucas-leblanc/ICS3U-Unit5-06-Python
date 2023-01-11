#!/usr/bin/env python3

# Created by: Lucas LeBlanc
# Created on: Jan 2023
# This program rounds numbers


def decimal_rounding(decimal, user_number):
    # This function rounds numbers

    # process
    answer = user_number[0] * (10**decimal)
    answer = int(answer + 0.5)
    answer = answer / (10**decimal)

    user_number[0] = answer


def main():
    # main function

    # calling functions and inputs
    user_number = []

    number_from_user = input("Enter the number you want to round: ")
    decimal = input("Enter the decimal places you want to round by: ")

    try:
        number_from_user = float(number_from_user)
        decimal = int(decimal)

        user_number.append(number_from_user)

        decimal_rounding(decimal, user_number)

        print("\nThe rounded number is {0}".format(user_number[0]))

    except Exception:
        print("\nInvalid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
