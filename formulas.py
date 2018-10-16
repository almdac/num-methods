from sympy import Symbol

def eulerFormula(f, yn, tn, h):
    y = Symbol('y')
    t = Symbol('t')
    fn = f.evalf(subs={y: yn, t: tn})
    return yn+(fn*h)

def backwardEulerFormula(f, yn, tn1, h):
    y = Symbol('y')
    t = Symbol('t')
    fn1 = f.evalf(subs={y: eulerFormula(f, yn, tn1-h, h), t: tn1})
    return yn+(fn1*h)