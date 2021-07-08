from cashier import Cashier
from customer import Customer


def create_env(number_of_cashiers, number_of_customers, mintime=60, maxtime=120, minspeed=1, maxspeed=3):

    cashier_instances = []
    customer_queue = []

    for i in range(number_of_cashiers):
        position = i + 1
        mintime, maxtime = mintime, maxtime
        cashier_instances.append(Cashier(position, mintime, maxtime))

    for i in range(number_of_customers):
        minspeed, maxspeed = minspeed, maxspeed
        customer_queue.append(Customer(minspeed, maxspeed))

    return cashier_instances, customer_queue
