from cashier import Cashier
from customer import Customer
from overall_process import overall_process

cash1 = Cashier(1, 45, 60)
cust1 = Customer(3)
cust2 = Customer(1)

cashiers = [cash1]
customers = [cust1, cust2]

overall_process(cashiers, customers)
