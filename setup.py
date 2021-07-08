from cashier import Cashier
from customer import Customer


def create_env(number_of_cashiers, number_of_customers, mintime=30, maxtime=60, speed=2):

    cashier_instances = []
    customer_queue = []

    for i in range(number_of_cashiers):
        position = i + 1
        mintime = mintime
        maxtime = maxtime
        cashier_instances.append(Cashier(position, mintime, maxtime))

    for i in range(number_of_customers):
        speed = speed
        customer_queue.append(Customer(speed))

    return cashier_instances, customer_queue
