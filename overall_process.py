def check_if_busy(cashier_instances):
    for cashier in cashier_instances:
        if cashier.busy == True:
            return True
    return False

def overall_process(cashier_instances, customer_queue):

    timer = 0

    while customer_queue != [] or check_if_busy(cashier_instances) == True:

        for cashier in [i for i in cashier_instances if i.busy == False]:
            customer = customer_queue.pop()
            cashier.process_transaction(customer)

        for cashier in cashier_instances:
            cashier.countdown -= 1

        for cashier in cashier_instances:
            if cashier.countdown == 0:
                cashier.busy = False

        timer += 1

    print(timer)
