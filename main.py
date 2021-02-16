#!/usr/bin/env python
"""This is a matrix game console application
   using numpy matrix inbuilt functions"""

import numpy as np

print("**************Welcome to the Python Matrix Application ********")


def check_if_numeric(input_value, callback):
    """ check if a value is numeric and return's it """
    value = 0
    try:
        value = int(input_value)
    except ValueError:
        print("The value " + input_value + " is not numeric")
        callback()
    return value


def fetch_action(first_array, second_array):
    """this fetches the matrix values from the user"""
    method = input(
        "Select a Matrix Operation from " +
        "the list below \nA for Addition\nB for Subration \nC for Matrix" +
        " Multiplication \nD for Element by element Multiplication\n")

    if method in ['A', 'a']:
        run_addition(first_array, second_array)
    elif method in ['B', 'b']:
        run_subtraction(first_array, second_array)
    elif method in ['c', 'C']:
        run_normal_multiplication(first_array, second_array)
    elif method in ['D', 'b']:
        run_element_wise_multiplication(first_array, second_array)
    elif method in ['Exit', 'E', 'e']:
        fetch_action(first_array, second_array)
    else:
        fetch_action(first_array, second_array)


def get_phone_number():
    """ gets the phone number format and return the value to the user """
    phone_number = input("Enter Your Phone Number (XXX-XXX-XXXX) \n")

    for number in phone_number:
        check_if_numeric(number, callback=get_phone_number)

    if len(phone_number) == 10:
        print("your phone number is " +
              phone_number[:3] + "-" + phone_number[3:6] + "-" + phone_number[6:])
    else:
        if len(phone_number.split("-")) == 3 and len(phone_number.split('-')[0]) == 3 and len(
                phone_number.split("-")[1]) == 3 and len(phone_number.split("-")[2]) == 4:
            print("Your phone number is :" + phone_number)
        else:
            print("make sure the format is XXX-XXX-XXX OR 10 numeric digit")
            get_phone_number()


def get_zip_code():
    """ gets and verifies the zip code format """
    zip_code = input("Enter your zip code (XXXXX-XXXX) \n")

    if len(zip_code) == 9:
        print("Your Zip code : " + zip_code[:6] + "-" + zip_code[6:])
    else:
        print("Your Zip code is : " + zip_code)


def run_game():
    """ runs the matrix game """
    get_phone_number()

    get_zip_code()

    first_array = get_numpy_input_array("Please enter your first array ", " Your first array ")

    second_array = get_numpy_input_array("please Enter your second array", "Your second array")

    fetch_action(first_array, second_array)


def get_numpy_input_array(welcome_string, response_string):
    """ gets the input as a string and converts it to a numpy array
     using the check_if_numeric function
      and generates a print with response string """
    first_row_input = input(str(welcome_string) + " :\n")
    second_row_input = input("")
    third_row_input = input("")
    nth_array = 0
    if len(first_row_input.split(" ")) < 3 or \
            len(second_row_input.split(" ")) < 3 or len(third_row_input.split()) < 3:
        print("Please renter the matrix format : 3 2 1")

        get_numpy_input_array(welcome_string, response_string)
    else:
        for element in first_row_input.split(" "):
            check_if_numeric(element, get_numpy_input_array)
        for element in second_row_input.split(" "):
            check_if_numeric(element, get_numpy_input_array)
        for element in third_row_input.split(" "):
            check_if_numeric(element, get_numpy_input_array)

        nth_array = np.array(
            [[int(first_row_input.split(" ")[0]), int(first_row_input.split(" ")[1]),
              int(first_row_input.split(" ")[2])],
             [int(second_row_input.split(" ")[0]), int(second_row_input.split(" ")[1]),
              int(second_row_input.split(" ")[2])],
             [int(third_row_input.split(" ")[0]), int(third_row_input.split(" ")[1]),
              int(third_row_input.split(" ")[2])]]
        )
        print(nth_array)


    return nth_array


def run_addition(first_array, second_array):
    """ adds the numpy array """
    result = first_array.__add__(second_array)
    handle_matrix_result(response_string="Addition", result=result)


def run_subtraction(first_array, second_array):
    """ performs subtraction of the numpy matrix """
    result = first_array.subtract(second_array)
    handle_matrix_result(response_string="subtraction", result=result)


def run_normal_multiplication(first_array, second_array):
    """ performs multiplication of the numpy array """
    result = np.multiply(first_array, second_array)
    handle_matrix_result(response_string="Multiplication", result=result)


def run_element_wise_multiplication(first_array, second_array):
    """ performs element wise multiplication """
    result = first_array.dot(second_array)
    handle_matrix_result(response_string="Element Wise multiplication", result=result)


def handle_matrix_result(response_string, result):
    """ gets the processes results from any of the actions :multiplication;
       substration;element wise  multiplication;multiplication
    then shows the value and the action that the user choose
    gets the input as a string and converts it to a numpy array
     printing the transpose and the mean values of the rows and the columns """
    print("You Selected " + response_string + " .The result is : \n")

    print(result)

    print("The Transpose is : \n")

    print(result.transpose())

    print("The row and mean values are : \n")

    print("rows :", np.mean(result, axis=0))

    print("Columns : ", np.mean(result, axis=1))

    main()


def main():
    """ the main function for the matrix game """
    print("Do you want to play the Matrix Game ?")

    decision = input("Enter Y for Yes and N for No : ")

    if decision in ['Y', 'y']:
        run_game()
    elif decision in ['N', 'n']:
        action = input("What do you want to do ?")

        if action in ['play', 'Play']:
            run_game()
        else:
            print("unable to " + action)
            main()
    else:
        print("___Thank you for Visiting my application")


main()
