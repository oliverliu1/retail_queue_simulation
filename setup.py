from cashier import Cashier
from customer import Customer


# Change create_env parameter default values to change the average times
def create_env(number_of_cashiers, number_of_customers, mintime=60, maxtime=120, minspeed=1, maxspeed=3):

    cashier_instances = []
    customer_queue = []

    for i in range(number_of_cashiers):
        position = i + 1
        cashier_instances.append(Cashier(position, mintime, maxtime))

    for i in range(number_of_customers):
        customer_queue.append(Customer(minspeed, maxspeed))

    return cashier_instances, customer_queue
