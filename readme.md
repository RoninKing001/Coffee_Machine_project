# ☕Coffee Machine Program

<p>💻 This is a coffee machine project that needed to be designed as part of the course I am currently undertaking.</p>
<p>📖 This project is designed to pull on everything that I've learned thus far. Loops, conditionals and functions. </p>

## 1. ♨️ Makes 3 hot variations 

<p>The coffee machine will be able to make 3 different variations:</p>
<ul>
    <li>Espresso</li>
    <li>Latte</li>
    <li>Cappuccino</li>
</ul>

<p>Each type of drink requires a different amount of water, coffee and milk. They also have a different price.</p>

**Espresso:**
<ul>
    <li>Water: 50ml</li>
    <li>Coffee: 18g</li>
    <li>Price: $1.50</li>
</ul>

**Latte:**
<ul>
    <li>Water: 200ml</li>
    <li>Coffee: 24g</li>
    <li>Milk: 150ml</li>
    <li>Price: $2.50</li>
</ul>

**Cappuccino:**
<ul>
    <li>Water: 250ml</li>
    <li>Coffee: 24g</li>
    <li>Milk: 100ml</li>
    <li>Price: $3.25</li>
</ul>

<p>In addition, the coffee machine has some resources to manage. The starting resources are:</p>
<ul>
    <li>Water: 300ml</li>
    <li>Milk: 200ml</li>
    <li>Coffee: 100g</li>
</ul>

## 2. 💰 Coin operated

<p>The second feature of the machine is to be coin operated. We are going to use american coins:</p>
<p>We start with a profit count of $0.00</p>
<ul>
    <li>Penny: $0.01</li>
    <li>Nickel: $0.05</li>
    <li>Dime: $0.10</li>
    <li>Quarter: $0.25</li>
    <li>Profit: $0.00</li>
</ul>

## 3. 📑 Coffee Machine Program Requirements

1. **Prompt user by asking “What would you like to order? (espresso/latte/cappuccino/) Or type 'off' to turn the machine off:”**
    - a. Check the user’s input to decide what to do next.
    - b. The prompt should show every time action has completed, e.g. once the drink is
    dispensed. The prompt should show again to serve the next customer.

2. **Turn off the Coffee Machine by entering “off” to the prompt.**
    - a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the
    machine.

3. **Print report.**
    - a. When the user enters “report” to the prompt, a report should be generated that shows the
    current resource values.

4. **Check if resources are sufficient.**
    - a. When the user chooses a drink, the program should check if there are enough resources
    to make that drink.
    - E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not
    continue to make the drink but print: “Sorry there is not enough water.”

5. **Process coins.**
    - a. If there are sufficient resources to make the drink selected, then the program should
    prompt the user to insert coins.
    - b. Calculate the monetary value of the coins inserted. 
    - E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

6. **Check if transaction is successful.**
    - a. Check that the user has inserted enough money to purchase the drink they selected. 
    - E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program
    should say “Sorry that's not enough money. Money refunded.”.
    - b. But if the user has inserted enough money, then the cost of the drink gets added to the
    machine as the profit and this will be reflected the next time “report” is triggered.
    - c. If the user has inserted too much money, the machine should offer change.
    - E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
    places.

7. **Make Coffee.**
    - a. If the transaction is successful and there are enough resources to make the drink the user
    selected, then the ingredients to make the drink should be deducted from the coffee
    machine resources.
    - b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte
    was their choice of drink.