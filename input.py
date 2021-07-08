def get_user_input():
    number_of_cashiers = input('Please enter the amount of cashiers you would like to model: ')
    number_of_customers = input('Please enter the amount of customers you would like to model: ')

    return int(number_of_cashiers), int(number_of_customers)

# fault tolerance needed to avoid breaking because of wrong input
