from sympy import Symbol

y = Symbol('y')
t = Symbol('t')

def eulerFormula(f, yn, tn, h):
    fn = f.evalf(subs={y: yn, t: tn})
    return yn+(fn*h)

def backwardEulerFormula(f, yn, tn1, h):
    fn1 = f.evalf(subs={y: eulerFormula(f, yn, tn1-h, h), t: tn1})
    return yn+(fn1*h)

def improvedEulerFormula(f, yn, tn, h):
    fn = f.evalf(subs={y: yn, t: tn})
    fn1 = f.evalf(subs={y: eulerFormula(f, yn, tn, h), t: tn+h})
    return yn + (fn+fn1)*(h/2)