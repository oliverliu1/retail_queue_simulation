from copy import deepcopy

from setup import create_env
from input import get_user_input
from simulate import run_simulation_sq, run_simulation_mq


def main():
    number_of_cashiers, number_of_customers = get_user_input()
    cashier_instances_sq, customer_queue_sq = create_env(number_of_cashiers, number_of_customers)
    cashier_instances_mq, customer_queue_mq = deepcopy(cashier_instances_sq), deepcopy(customer_queue_sq)

    run_simulation_sq(cashier_instances_sq, customer_queue_sq)
    run_simulation_mq(cashier_instances_mq, customer_queue_mq)


if __name__ == '__main__':
    main()
