from formulas import *
from sympy.parsing.sympy_parser import parse_expr

def DefinedOrderMethods(params, formula, title):
    y0 = float(params[0])
    t0 = float(params[1])
    h = float(params[2])
    steps = float(params[3])
    f = parse_expr(params[4])
    o = open('output.txt', 'a')

    o.write(title)
    o.write('y( {} ) = {}\n'.format(t0, y0))
    o.write('h = {}\n'.format(h))
    o.write('{} {}\n'.format(0, y0))

    i = 0
    yn = y0
    while i < steps:
        yn1 = formula(f, yn, t0+(i*h), h)
        o.write('{} {}\n'.format(i+1, yn1))
        yn = yn1
        i += 1

    o.close()

def euler(params):
    DefinedOrderMethods(params, eulerFormula, 'Metodo de Euler\n')

def euler_inverso(params):
    DefinedOrderMethods(params, backwardEulerFormula, 'Metodo de Euler Inverso\n')

def euler_aprimorado(params):
    DefinedOrderMethods(params, improvedEulerFormula, 'Metodo de Euler Aprimorado\n')

def runge_kutta(params):
    DefinedOrderMethods(params, rungeKuttaFormula, 'Metodo de Runge-Kutta\n')

def adam_bashforth(params):
    order = params[len(params)-1]
    f = parse_expr(params[len(params)-2])
    steps = params[len(params)-3]
    h = params[len(params)-4]
    t0 = params[len(params)-5]
    points = params[0:order]

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