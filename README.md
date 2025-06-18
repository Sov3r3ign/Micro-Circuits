<h1>🔌 Micro Circuits</h1>
<h2>Assignment </h2>

<p>📊 The system should keep track of <b><em>stock codes, stock prices, and stock count in three separate lists.</em></b>
The stock codes should be <b>string-based 📝, the prices floating-point 💰, and the count as integer 🔢.</b>
To keep them competitive, their financial planner has advised them never to carry more than 50
types of stock (according to stock code) at a time 🚫📦.</p>

<p>➕ The system needs to have a function called <b>AddStockCode()</b> 🏷️.
This function needs to prompt the user for a stock code and price and then add these values to the others already stored in the system 🗃️.
Their advisor has also requested that no item may be priced higher than R 1000.00 ⚠️💸.</p>

<p>🔍 To find a specific stock code, a search function is required.
Create a function called <b>SearchCode</b> 🧭 to fulfill this function.
The function should receive a single string-based parameter, representing the stock code to search for 🔡.
The function must not do any unnecessary searching 🚀. As soon as the search value is found, the search process should halt 🛑.
Upon a successful search, the function must return the index in the stock code list where the value was found 🧮.
If the value was not found, display a relevant message to the command-line and return a suitable value ❌.</p>

<p>📥 Once the stock codes and prices have been added, it will be necessary to add stock to the system.
Create a function called <b>AddStockItem</b> 🧾 which will prompt the user for a stock code and the
number of items to add ➕📦.
This function should make a call to the SearchCode function to find the relevant stock item 🔁.
To ensure that stock doesn’t get old in the shop 🕰️, their financial planner has advised them that they should never have more than 100 items of any stock type (according to stock count) in the shop at a time ⚠️📉.</p>

<p>📋 From time to time, it will be necessary to check the stock list.
Create a function called <b>DisplayStockList</b> 🖥️ which will display every stock code, with its associated price, number of items in stock, and total stock value for each item 💹.
The list should also display the total value of all stock in the system 💼.
The list should be displayed with a header in a format similar to the following:</p>

 
<p>Stock code, In stock, Price,Stock value 
AAA, 10,50,500 
BBB,5,20.00,100 
Total,,600 </p>

To control the system, Micro Circuits wish to make use of a CLI-based menu with the following options:    
1. Add Stock Code
2. Add Stock Item
3. Display Stock List
4. Exit
   
<p>The menu should display continuously until the user decides to exit the program, i.e. after selecting 
options 1 to 3 and completing the activity the menu should always be re-displayed.  The program should 
only exit when option 4 is selected.</p>

