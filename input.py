def get_user_input():
    number_of_cashiers = input('Please enter the amount of cashiers you would like to model: ')
    while not number_of_cashiers.isnumeric():
        number_of_cashiers = input('Error, please enter an integer. Enter the amount of cashiers you would like to model: ')

    number_of_customers = input('Please enter the amount of customers you would like to model: ')
    while not number_of_customers.isnumeric():
        number_of_customers = input('Error, please enter an integer. Enter the amount of customers you would like to model: ')

    return int(number_of_cashiers), int(number_of_customers)
