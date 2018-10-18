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
    order = int(params[len(params)-1])
    f = parse_expr(params[len(params)-2])
    steps = float(params[len(params)-3])
    h = float(params[len(params)-4])
    t0 = float(params[len(params)-5])
    ypoints = params[0:order]

    i = 0
    while i < order:
        ypoints[i] = float(ypoints[i])
        i += 1
        
    o = open('output.txt', 'a')
    o.write('Metodo de Adams-Bashforth\n')
    o.write('y( {} ) = {}\n'.format(t0, ypoints[0]))
    o.write('h = {}\n'.format(h))
    
    i = 0
    for yp in ypoints:
        o.write('{} {}\n'.format(i, yp))
        i += 1
    
    j = 0
    coeffs = []
    while j < order:
        coeffs.append(calculateAdamsBashforthCoeffs(order, j))
        j += 1

    recurrence_relation = buildRecurrenceRelation(order, h, coeffs)

    i = 0
    while i < steps:
        ynk = adamsBashforthFormula(f, ypoints, t0+(h*i), h, order, recurrence_relation)
        o.write('{} {}\n'.format(i+1+order, ynk))
        ypoints.append(ynk)
        ypoints.pop(0)
        i += 1

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