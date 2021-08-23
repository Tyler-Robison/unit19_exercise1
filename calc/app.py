from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def do_add():
    int_a = int(request.args['a'])
    int_b = int(request.args['b'])
    math_string = add(int_a, int_b) 
    return str(math_string)

@app.route('/sub')
def do_sub():
    int_a = int(request.args['a'])
    int_b = int(request.args['b'])
    math_string = sub(int_a, int_b) 
    return str(math_string)

@app.route('/mult')
def do_mult():
    int_a = int(request.args['a'])
    int_b = int(request.args['b'])
    math_string = mult(int_a, int_b) 
    return str(math_string)

@app.route('/div')
def do_div():
    int_a = int(request.args['a'])
    int_b = int(request.args['b'])
    math_string = div(int_a, int_b) 
    return str(math_string)            

@app.route('/math/<operation>')
def do_operation(operation):
    int_a = int(request.args['a'])
    int_b = int(request.args['b'])

    # if operation == 'add':
    #     math_string = add(int_a, int_b) 

    # if operation == 'sub':
    #     math_string = sub(int_a, int_b) 

    # if operation == 'mult':
    #     math_string = mult(int_a, int_b) 

    # if operation == 'div':
    #     math_string = div(int_a, int_b)   

    # return str(math_string)              

    math_dict = {
        'add': add,
        'sub': sub,
        'mult': mult,
        'div': div
    }

    result = math_dict[operation](int_a, int_b)
    return str(result)