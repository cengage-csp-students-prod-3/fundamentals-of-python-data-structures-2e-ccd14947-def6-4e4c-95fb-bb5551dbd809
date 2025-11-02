"""
File: marketmodel.py
Project 8.4

Models multiple cashiers.
"""

from cashier import Cashier
from customer import Customer
import random

class MarketModel(object):

    # def __init__(self, lengthOfSimulation, averageTimePerCus,
    #              probabilityOfNewArrival):
    #     self.probabilityOfNewArrival = probabilityOfNewArrival
    #     self.lengthOfSimulation = lengthOfSimulation
    #     self.averageTimePerCus = averageTimePerCus
    #     self.cashier = Cashier()
    def __init__(self, lengthOfSimulation, averageTimePerCus,
                 probabilityOfNewArrival, numCashiers):
        self.probabilityOfNewArrival = probabilityOfNewArrival
        self.lengthOfSimulation = lengthOfSimulation
        self.averageTimePerCus = averageTimePerCus
        self.cashiers = list()
        for count in range(numCashiers):
            self.cashiers.append(Cashier(count + 1))
   
    def runSimulation(self):
        """Run the clock for n ticks."""
        # for currentTime in range(self.lengthOfSimulation):
        #     # Attempt to generate a new customer
        #     customer = Customer.generateCustomer(
        #         self.probabilityOfNewArrival,
        #         currentTime,
        #         self.averageTimePerCus)

        #     # Send customer to cashier if successfully generated
        #     if customer != None:
        #         self.cashier.addCustomer(customer)

        #     # Tell cashier to provide another unit of service
        #     self.cashier.serveCustomers(currentTime)
        for currentTime in range(self.lengthOfSimulation):
            # Attempt to generate a new customer
            customer = Customer.generateCustomer(
                self.probabilityOfNewArrival,
                currentTime,
                self.averageTimePerCus)

            # Send customer to a randomly chosen cashier
            # if successfully generated
            if customer != None:
                random.choice(self.cashiers).addCustomer(customer)

            # Tell all cashiers to provide another unit of service
            for cashier in self.cashiers:
                cashier.serveCustomers(currentTime)

    def __str__(self):
        return "CASHIER CUSTOMERS   AVERAGE     LEFT IN\n" + \
               "        PROCESSED   WAIT TIME   LINE\n" + \
               "\n".join(map(str, self.cashiers))

