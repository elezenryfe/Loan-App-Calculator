from flask import Flask, render_template, flash
from flask import request
app = Flask(__name__)

@app.route('/', methods = ["POST","GET"])
def front_end():
  return render_template('front_end.html')

@app.route('/loan_calculate/', methods = ["POST","GET"])
def loan_calculate():
    alpha = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',',',';']
    if request.method == "POST":
        if request.form.get("amount") == '' or request.form.get("interest") == '' or request.form.get("periods") == '':
            return "<p>Please enter valid values</p>"
        for i in range (len(alpha)):
            if alpha[i] in request.form.get("amount") or alpha[i] in request.form.get("interest") or alpha[i] in request.form.get("periods"):
                return "<p>Please enter valid values</p>"        

        a = float(request.form.get("amount"))
        r = float(request.form.get("interest"))
        r = r/100
        r = r/12
        p = int(request.form.get("periods"))
        principal_portion = []
        interest_paid = []
        payment = (r*a)/(1-(1+r)**(-p))
        ob = []
        for i in range (1,p+1):
            ppn = payment*((1+r)**(-(1+p-i)))
            interest = payment - ppn
            principal_portion.append(ppn)
            interest_paid.append(interest)
        ob.append(a-principal_portion[0])
        for i in range (1,p):
            ob.append(ob[i-1]-principal_portion[i])
        htmlContent = "<style>table{padding: 1px; border-collapse: collapse;} tr:hover {background-color:#F5F5F5;} tr:nth-child(even) {background-color: cornsilk;} th{ background-color: bisque; color: black;}</style>"
        htmlContent = htmlContent + '<table border="1">\n<tr><th>Payment no</th><th>Payment Amount</th><th>Principle Amount Paid</th><th>Interest Amount Paid</th><th>Loan Outstanding Balance</th></tr>\n'
        j = 0
        for i in range (p):
            j = i + 1
            htmlContent = htmlContent + '<tr><td>' + str(j) + '</td><td>' + str(round(payment,2)) + '</td><td>' + str(round(principal_portion[i],2)) + '</td><td>' + str(round(interest_paid[i],2)) + '</td><td>' + str(round(ob[i],2)) + '</td></tr>\n'
        htmlContent = htmlContent + '</table>'
        return htmlContent

if __name__ == '__main__':
  app.run(debug=True)