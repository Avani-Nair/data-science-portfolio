def calculation(num):  # function for the calculations

    num_list = list(str(num))  # converting the number to a list, as the digits need to be swapped

    num_list[0], num_list[-1] = num_list[-1], num_list[0]  # swapping the first and last digit in the list

    swapped = int("".join(num_list))  # joining back the digits and converting into an integer

    difference = abs(num - swapped)  # calculating the difference between the number given by the user and its swapped number

    swap_difference = list(str(difference))  # converting the difference into a list

    swap_difference[0], swap_difference[-1] = swap_difference[-1], swap_difference[0]  # swapping the first and last digit in the list

    swapped_difference = int("".join(swap_difference))  # joining back the digits and converting it into an integer

    result = difference + swapped_difference  # adding the difference and the swapped difference

    return swapped, difference, swapped_difference, result  # returns the calculated values

while True:  # main program loop which can be repeated multiple times
    user = input("Enter a 3-digit or 4-digit number: ")  # asks the user for the input
    if user.isdigit():  # checks if the user input only contains digits

        if len(user) == 3 or len(user) == 4:  # checks the length of the digit, that is 3 or 4

            if abs(int(user[0]) - int(user[-1])) >= 1:  # checks if the difference between the 1st and last digit is at least 1
                num = int(user)  # converts the user input which is a string to an integer
                swapped, difference, swapped_difference, result = calculation(num)  # calling the function

                # prints all the results
                print("The swapped number is: ", swapped)
                print("The differenced value is: ", difference)
                print("The reversed difference is: ", swapped_difference)
                print("The output value is: ", result, "************")

            else:  # prints error message if the 3 or 4 digit numbers are not valid
                if len(user) == 3:
                    print("Your number is not a valid 3-digit number, Please try again!")

                else:
                    print("Your number is not a valid 4-digit number, Please try again!")



        elif len(user) == 2:   # prints error message if the user input is not 3 or 4 digit numbers
            print(user, " is a 2 digit number!")

        elif len(user) == 1:
            print(user, " is a 1 digit number!")

        elif len(user) > 4:
            print(user, "is more than 4 digits!")

    else:  # prints error message if the user inputs are not digits
        print("Please enter digits only!")

    again = input("Do you want to try again? (If yes, enter 1; otherwise, enter 0.)" )   # asks the user if they want to try again
    print()

    if again == "0":  # if the user does not want to continue they enter 0, exit the loop and end the program
        break

