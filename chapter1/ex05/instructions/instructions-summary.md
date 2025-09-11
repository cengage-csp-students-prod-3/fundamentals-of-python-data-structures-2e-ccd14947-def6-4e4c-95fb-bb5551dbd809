The TidBit Computer Store has a credit plan for computer purchases. There is a 10% down payment and an annual interest rate of 12%. 
Monthly payments are 5% of the listed purchase price minus the down payment. Write a program that takes the purchase price as input. 
The program should display a table, with appropriate headers, of a payment schedule for the lifetime of the loan. 

Each row of the table should contain the following items: 

* The month number (beginning with 1) 
* The current total balance owed 
* The interest owed for that month 
* The amount of principal owed for that month 
* The payment for that month 
* The balance remaining after payment
* The amount of interest for a month is equal to balance * rate / 12

An example table is shown below: 

| Month | Starting Balance | Interest to Pay | Principle to Pay | Payment | Ending Balance|
| ----- | ---------------- | --------------- | ---------------- | ------- | ---------------|
| 1 | 12.00 | 0.12 | 0.48 | 0.60 | 11.40 |
| 2 | 11.40 | 0.11 | 0.49 | 0.60 | 10.80 |
| 3 | 10.80 | 0.11 | 0.49 | 0.60 | 10.20 |

> It is important that your output follow the format in the table above.  

Here are some usual facts:

Input
* purchase price

Constants
* annual interest rate = 12%
* downpayment = 10% of purchase price
* monthly payment = 5% of purchase price

The amount of principal for a month is equal to the monthly payment minus the interest owed.
