from flask import Flask, render_template, request, jsonify

app = Flask(__name__)   # creating an object with any name

@app.route('/', methods=['GET', 'POST']) # To render Homepage #whatever code written below @app.route it launches dat thru d particular server wer dese things are running
def home_page():
    return render_template('input.html')   #goes to index html page wer we can give input

@app.route('/math', methods=['POST'])  # This will be called from UI  # post -data is not exposed
def math_operation():      #creating a calculator
    if (request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])   # request.form takes a request for an operation from form(contains numbers which are given as input)
        num2 = int(request.form['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'Sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'Difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'Product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'Quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return render_template('output.html',result=result) # rndr_tmplt launches a web page wer result is displayed

# @app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
# def math_operation_via_postman():
#     if (request.method=='POST'):
#         operation=request.json['operation']      # data input given thru JSon from postman
#         num1=int(request.json['num1'])       #3 inputs -operation ,num1 n num2 and is expection a result in json
#         num2 = int(request.json['num2'])
#         if(operation=='add'):
#             r=num1+num2
#             result= 'sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
#         if (operation == 'subtract'):
#             r = num1 - num2
#             result = 'difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
#         if (operation == 'multiply'):
#             r = num1 * num2
#             result = 'product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
#         if (operation == 'divide'):
#             r = num1 / num2
#             result = 'quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
#         return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)  #To execute