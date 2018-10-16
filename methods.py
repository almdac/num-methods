import mpmath
from sympy.parsing.sympy_parser import parse_expr

def euler(params):
    y0 = params[0]
    t0 = params[1]
    h = params[2]
    steps = params[3]
    f = parse_expr(params[4])

def euler_inverso(params):
    y0 = params[0]
    t0 = params[1]
    h = params[2]
    steps = params[3]
    f = parse_expr(params[4])

def euler_aprimorado(params):
    y0 = params[0]
    t0 = params[1]
    h = params[2]
    steps = params[3]
    f = parse_expr(params[4])

def runge_kutta(params):
    y0 = params[0]
    t0 = params[1]
    h = params[2]
    steps = params[3]
    f = parse_expr(params[4])

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