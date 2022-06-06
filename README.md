# Loan-App-Calculator
a front end app using flask web framework to calculate monthly loan repayment over a period of time 

The source code makes use of Flask—a micro web framework written in Python, especially useful for developing web applications.
The first two lines import Flask, render_template, flash and request, for framework, template creation, error alerts and reading values respectively.
The default route (‘/’) is set to open the “front_end.html” file which opens in a web browser as a web page.
Once the code is executed, the command terminal displays the following message, “Running on http://127.0.0.1:5000/”. Clicking on the link opens the default route
The html code for the front-end has a “<form>” tag that is wrapped over the values that the user inputs. The ‘Calculate’ button invokes the ‘/loan_calculate/’ route in the source code and all the values within the “form” tag are sent.
The function checks if the request method is ‘POST’, since the source code aims to read the values and update the webpage, displaying the loan amortization schedule in a tabular format.
Next, the validity of the values is checked. For example: if the “Amount” value is left empty, or if the value provided is not numerical. If any of the condition is true, the webpage is updated to a new route (/loan_calculate/) and a string of message saying, “Please enter valid values” is displayed.
If the condition is false, and all three values given are valid, then the function performs the loan calculation on the following formulae.
• PAYMENTn = (Rn∗A) / [1−(1+Rn)−N]
• PPn = PAYMENTn ∗ (1 + Rn)^−(1+N−n)
• INTn = PAYMENTn − PPn
• OBn = (INTn / Rn) − PPn = OBn − PPn
Where, A = amount, N = number of loan periods, Rn = interest rate for period n, INTn = interest due for period n, PPn = principal payment due for period n, OBn = outstanding balance due after period n, PAYMENTn = amount of loan to be paid.
The variable ‘payment’ will store the constant amount to be paid every month for the duration of the loan. The lists ‘principal_portion’ and ‘interest_paid’ will store the corresponding principal and interest amount to be paid every month for the duration of the loan. The list ‘ob’ stores the outstanding balance to be paid, after every month for the duration of the loan.
Now that the values have been stored, a variable ‘htmlContent’ is created and the values are displayed in html using a tabular format. 
The ‘<style>’ tag has been used to colour the text and background. The variable ‘htmlContent’ is then appended with the column names: Payment no, Payment Amount, Principal Amount, Interest Amount and Loan Outstanding Balance.
The rows are then filled with the values in accordance to the column names. Each value in lists, ‘principal_portion’, ‘interest_paid’ and ‘ob’ are stored in each row of the ‘htmlContent’ table, along with a constant value from the ‘payment’ variable.
After the loop has finished, (the length of lists has been reached), the variable ‘htmlContent’ is then appended with a closing ‘</table>’ tag.
The variable is returned to the “front_end.html” and the variable ‘htmlContent’ is displayed.
