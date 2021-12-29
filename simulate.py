from datetime import timedelta


def run_simulation(cashier_instances, customer_queue):

    timer = 0
    number_of_customers = len(customer_queue)

    # While the queue still has customers or while any cashier is busy
    while customer_queue != [] or check_if_busy(cashier_instances):

        # Assigns a customer to any cashier that is not busy
        for cashier in [i for i in cashier_instances if not i.busy]:
            if customer_queue != []:
                customer = customer_queue.pop()
                cashier.process_transaction(customer)

        # Decrements the countdown of every cashier
        for cashier in cashier_instances:
            cashier.countdown -= 1

        # Sets busy to False if any cashier finished their transaction
        for cashier in cashier_instances:
            if cashier.countdown == 0:
                cashier.busy = False

        timer += 1

    print(f'It took {timedelta(seconds=timer)} for {len(cashier_instances)} cashier(s) to serve {number_of_customers} customer(s).')

# Helpers

def check_if_busy(cashier_instances):
    for cashier in cashier_instances:
        if cashier.busy:
            return True
    return False
