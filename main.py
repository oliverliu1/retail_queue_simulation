from cashier import Cashier
from customer import Customer
from overall_process import overall_process, check_if_busy
from user_input import user_input, user_input_helper

overall_process(*user_input(*user_input_helper()))
