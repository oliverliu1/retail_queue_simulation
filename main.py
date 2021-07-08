from setup import create_env
from input import get_user_input
from simulate import run_simulation


def main():
    number_of_cashiers, number_of_customers = get_user_input()
    cashier_instances, customer_queue = create_env(number_of_cashiers, number_of_customers)
    run_simulation(cashier_instances, customer_queue)

if __name__ == '__main__':
    main()
