from cashier import Cashier
from customer import Customer

def user_input(number_of_cashiers, number_of_customers):

    cashier_instances = []
    customer_queue = []

    for i in range(number_of_cashiers):
        position = int(input('Enter cashier position: '))
        mintime = int(input('Enter cashier minimum transaction time: '))
        maxtime = int(input('Enter cashier maximum transaction time: '))
        cashier_instances.append(Cashier(position, mintime, maxtime))

    for i in range(number_of_customers):
        speed = int(input('Enter customer walking speed: '))
        customer_queue.append(Customer(speed))

    return cashier_instances, customer_queue

def user_input_helper():
    number_of_cashiers = input('Please enter the amount of cashiers you would like to model: ')
    number_of_customers = input('Please enter the amount of customers you would like to model: ')

    return int(number_of_cashiers), int(number_of_customers)
