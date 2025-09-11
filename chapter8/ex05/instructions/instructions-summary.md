<!-- manual -->

In real life, customers do not choose a random cashier when they check out. They typically base their choice on at least the following two factors:

1. The length of a line of customers waiting to check out.
2. The physical proximity of a cashier.

Modify the simulation of _Exercise 4_ so that it takes account of the first factor.

In the `Cashier` class of the _cashier.py_ file, complete the following:

1. Define the `getLineLength()` method:
   - Returns the number of customers in the line.

In the `MarketModel` class of the _marketmodel.py_ file, complete the following:

1. Define the `pickCashier()` method:
   - Returns the cashier for the next customer, based on the shortest line of customers.

To test your program run the `main()` method in the _marketapp.py_ file.

Your program's output should look like the following:

```
Welcome to the Market Simulator!

Enter the total running time: 30
Enter the average processing time per customer: 3
Enter the probability of a new arrival: 1
Enter the number of cashiers: 4

----------------------------------------
CASHIER CUSTOMERS   AVERAGE     LEFT IN
        PROCESSED   WAIT TIME   LINE
   1        0          0.00        0
   2        9          0.00        0
   3       10          1.80        0
   4       10          1.80        1
```
