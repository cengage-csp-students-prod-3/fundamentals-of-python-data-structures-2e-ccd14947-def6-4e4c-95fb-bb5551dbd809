<!-- manual -->

The simulator’s interface asks the user to enter the average number of minutes required to process a customer. However, as written, the simulation assigns the same processing time to each customer. In real life, processing times vary around the average.

> Be sure to reuse your solution from _Programming Exercise 8.6_ as your starter file for the _customer.py_ file.

In the `Customer` class of the _customer.py_ file, complete the following:

1. Modify the `__init__` method:
   - Set the `amountOfServiceNeeded` so that it randomly generates the service times between **1** and **(serviceNeeded \* 2 + 1)**.

To test your program run the `main()` method in the _marketapp.py_ file.

> When testing the servicing time per cashier will be random rather than static
