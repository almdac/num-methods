from formulas import *
from sympy.parsing.sympy_parser import parse_expr

def euler(params):
    y0 = float(params[0])
    t0 = float(params[1])
    h = float(params[2])
    steps = float(params[3])
    f = parse_expr(params[4])
    o = open('output.txt', 'a')

    o.write('Metodo de Euler\n')
    o.write('y( {0} ) = {1}\n'.format(t0, y0))
    o.write('h = {0}\n'.format(h))
    o.write('{0} {1}\n'.format(0, y0))

    i = 0
    yn = y0
    while i < steps:
        yn1 = eulerFormula(f, yn, t0+(i*h), h)
        o.write('{0} {1}\n'.format(i+1, yn1))
        yn = yn1
        i += 1
    o.close()

def euler_inverso(params):
    y0 = float(params[0])
    t0 = float(params[1])
    h = float(params[2])
    steps = float(params[3])
    f = parse_expr(params[4])
    o = open('output.txt', 'a')

    o.write('Metodo de Euler Inverso\n')
    o.write('y( {0} ) = {1}\n'.format(t0, y0))
    o.write('h = {0}\n'.format(h))
    o.write('{0} {1}\n'.format(0, y0))

    i = 1
    yn = y0
    while i <= steps:
        yn1 = backwardEulerFormula(f, yn, t0+(h*i), h)
        o.write('{0} {1}\n'.format(i, yn1))
        yn = yn1
        i += 1
    o.close()

def euler_aprimorado(params):
    y0 = float(params[0])
    t0 = float(params[1])
    h = float(params[2])
    steps = float(params[3])
    f = parse_expr(params[4])
    o = open('output.txt', 'a')

    o.write('Metodo de Euler Aprimorado\n')
    o.write('y( {0} ) = {1}\n'.format(t0, y0))
    o.write('h = {0}\n'.format(h))
    o.write('{0} {1}\n'.format(0, y0))

    i = 0
    yn = y0
    while i < steps:
        yn1 = improvedEulerFormula(f, yn, t0+(h*i), h)
        o.write('{0} {1}\n'.format(i+1, yn1))
        yn = yn1
        i += 1
    o.close()

def runge_kutta(params):
    pass

def adam_bashforth(params):
    pass

def adam_multon(params):
    pass

def formula_inversa(params):
    pass

def adam_bashforth_by_euler(params):
    pass

def adam_bashforth_by_euler_inverso(params):
    pass

def adam_bashforth_by_euler_aprimorado(params):
    pass

def adam_bashforth_by_runge_kutta(params):
    pass

def adam_multon_by_euler(params):
    pass

def adam_multon_by_euler_inverso(params):
    pass

def adam_multon_by_euler_aprimorado(params):
    pass
    
def adam_multon_by_runge_kutta(params):
    pass

def formula_inversa_by_euler(params):
    pass

def formula_inversa_by_euler_inverso(params):
    pass

def formula_inversa_by_euler_aprimorado(params):
    pass

def formula_inversa_by_runge_kutta(params):
    pass